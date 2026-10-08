# -*- coding: utf-8 -*-
"""
engine.py — Mesin Ekstraksi & Deteksi JEJAK Kepatuhan (Purwarupa)

Implementasi RIIL dari alur "Bagian 4: Pendekatan Teknis & Data" di proposal:

  1) INPUT   : membaca teks dokumen tidak terstruktur (kontrak, slip gaji,
               data BPJS) dari dataset.py
  2) PROSES  : mengekstraksi entitas kunci dari teks bebas menggunakan
               pencocokan pola (regex) — ini adalah PENGGANTI SEMENTARA untuk
               langkah yang pada versi produksi akan memakai model bahasa
               (Claude) untuk membaca dokumen yang jauh lebih beragam
               formatnya. Regex dipilih untuk purwarupa ini karena berjalan
               tanpa API key/biaya dan cukup untuk membuktikan alur logika
               end-to-end secara jujur.
  3) OUTPUT  : mencocokkan hasil ekstraksi terhadap ambang hukum eksplisit
               (bukan model statistik), menghasilkan indikasi pelanggaran
               berjenjang lengkap dengan rujukan pasal dan skor keyakinan
               yang dikalibrasi berbeda untuk UMKM (sesuai mitigasi bias
               di Bagian 8 proposal).
"""

import re
import json
from datetime import date
from dataset import CASES

TODAY = date(2026, 1, 31)  # "hari ini" dalam simulasi, untuk hitung masa kerja
BULAN = {
    "januari": 1, "februari": 2, "maret": 3, "april": 4, "mei": 5, "juni": 6,
    "juli": 7, "agustus": 8, "september": 9, "oktober": 10, "november": 11, "desember": 12,
}


def parse_tanggal_indonesia(s):
    m = re.search(r"(\d{1,2})\s+(\w+)\s+(\d{4})", s, re.IGNORECASE)
    if not m:
        return None
    hari, bulan_nama, tahun = m.groups()
    bulan_num = BULAN.get(bulan_nama.lower())
    if not bulan_num:
        return None
    try:
        return date(int(tahun), bulan_num, int(hari))
    except ValueError:
        return None


def extract_kontrak(text):
    t = text.upper()
    if "WAKTU TIDAK TERTENTU" in t:
        status = "TETAP"
    elif "WAKTU TERTENTU" in t:
        status = "KONTRAK"
    else:
        status = "TIDAK_JELAS"

    tgl_mulai = None
    for pola in [r"sejak tanggal ([\d]{1,2}\s+\w+\s+\d{4})",
                 r"sejak\s+([\d]{1,2}\s+\w+\s+\d{4})",
                 r"mulai bekerja\s+([\d]{1,2}\s+\w+\s+\d{4})",
                 r"[Mm]asa kerja:\s*([\d]{1,2}\s+\w+\s+\d{4})"]:
        m = re.search(pola, text, re.IGNORECASE)
        if m:
            tgl_mulai = parse_tanggal_indonesia(m.group(1))
            if tgl_mulai:
                break

    return {"status_kontrak": status, "tanggal_mulai": tgl_mulai, "doc_jelas": status != "TIDAK_JELAS"}


def extract_slip(text):
    pola_list = [
        r"TOTAL DITERIMA:\s*Rp\s*([\d.]+)",
        r"[Uu]pah per bulan[^:]*:\s*Rp\s*([\d.]+)",
        r":\s*([\d.]{7,})\s*/\s*bulan",
        r":\s*([\d.]{7,})\s*$",
    ]
    for pola in pola_list:
        m = re.search(pola, text, re.MULTILINE)
        if m:
            angka = int(m.group(1).replace(".", ""))
            return {"upah_slip": angka}
    angka_semua = [int(a.replace(".", "")) for a in re.findall(r"([\d]{1,3}(?:\.\d{3}){1,3})", text)]
    if angka_semua:
        return {"upah_slip": max(angka_semua)}
    return {"upah_slip": None}


def extract_bpjs(text):
    status_m = re.search(r"Status Kerja Dilaporkan:\s*(.+)", text)
    upah_m = re.search(r"Upah Dilaporkan:\s*Rp\s*([\d.]+)", text)
    tgl_m = re.search(r"Tanggal Terdaftar:\s*([\d]{1,2}\s+\w+\s+\d{4})", text)

    status_raw = status_m.group(1).strip() if status_m else None
    if status_raw and ("TETAP" in status_raw.upper() or "PKWTT" in status_raw.upper()):
        status_norm = "TETAP"
    elif status_raw and "PKWT" in status_raw.upper():
        status_norm = "KONTRAK"
    elif status_raw and ("LEPAS" in status_raw.upper() or "HARIAN" in status_raw.upper()):
        status_norm = "LEPAS"
    else:
        status_norm = "TIDAK_DIKETAHUI"

    return {
        "status_dilaporkan_raw": status_raw,
        "status_dilaporkan": status_norm,
        "upah_dilaporkan": int(upah_m.group(1).replace(".", "")) if upah_m else None,
        "tanggal_terdaftar": parse_tanggal_indonesia(tgl_m.group(1)) if tgl_m else None,
    }


def masa_kerja_tahun(tanggal_mulai):
    if not tanggal_mulai:
        return None
    delta_hari = (TODAY - tanggal_mulai).days
    return round(delta_hari / 365.25, 1)


def deteksi_kasus(case):
    kontrak = extract_kontrak(case["kontrak_kerja_text"])
    slip = extract_slip(case["slip_gaji_text"])
    bpjs = extract_bpjs(case["data_bpjs_text"])
    masa_kerja = masa_kerja_tahun(kontrak["tanggal_mulai"])

    flags = []
    pasal_rujukan = []
    skor = 0

    if kontrak["status_kontrak"] == "TETAP" and bpjs["status_dilaporkan"] in ("KONTRAK", "LEPAS"):
        flags.append("Misklasifikasi Status Kerja")
        pasal_rujukan.append("Pasal 59 ayat (3) UU Cipta Kerja")
        skor += 55

    if kontrak["status_kontrak"] == "KONTRAK" and masa_kerja is not None and masa_kerja > 5.0:
        flags.append("PKWT Melebihi Batas Maksimal (demi hukum menjadi PKWTT)")
        pasal_rujukan.append("Pasal 8 PP No. 35/2021")
        skor += 40

    gap_pct = None
    if slip["upah_slip"] and bpjs["upah_dilaporkan"]:
        gap_pct = round((slip["upah_slip"] - bpjs["upah_dilaporkan"]) / slip["upah_slip"] * 100, 1)
        ambang_tinggi, ambang_sedang = (20, 8) if case["skala_usaha"] == "UMKM" else (15, 5)
        if gap_pct >= ambang_tinggi:
            flags.append(f"Under-Reporting Upah (selisih {gap_pct}%)")
            pasal_rujukan.append("Pasal 15 ayat (1) UU No. 24/2011 (BPJS)")
            skor += 45
        elif gap_pct >= ambang_sedang:
            flags.append(f"Under-Reporting Upah — borderline (selisih {gap_pct}%)")
            pasal_rujukan.append("Pasal 15 ayat (1) UU No. 24/2011 (BPJS)")
            skor += 25

    if not kontrak["doc_jelas"]:
        skor = min(skor, 60)

    skor = max(0, min(skor, 96))

    if not flags:
        confidence_label = "Tidak Ada Indikasi"
    elif skor >= 65:
        confidence_label = "Tinggi"
    elif skor >= 35:
        confidence_label = "Sedang"
    else:
        confidence_label = "Rendah"

    catatan = []
    if not kontrak["doc_jelas"]:
        catatan.append("Dokumen kontrak tidak menyebutkan jenis perjanjian secara eksplisit — keyakinan dibatasi, perlu klarifikasi manusia sebelum ditindaklanjuti.")
    if not flags:
        catatan.append("Tidak ditemukan inkonsistensi material antara dokumen dan data yang dilaporkan.")

    return {
        "id": case["id"],
        "perusahaan": case["perusahaan"],
        "skala_usaha": case["skala_usaha"],
        "ekstraksi": {
            "status_kontrak": kontrak["status_kontrak"],
            "tanggal_mulai": str(kontrak["tanggal_mulai"]) if kontrak["tanggal_mulai"] else None,
            "masa_kerja_tahun": masa_kerja,
            "upah_slip": slip["upah_slip"],
            "status_dilaporkan": bpjs["status_dilaporkan_raw"],
            "upah_dilaporkan": bpjs["upah_dilaporkan"],
            "selisih_upah_persen": gap_pct,
        },
        "flags": flags,
        "pasal_rujukan": sorted(set(pasal_rujukan)),
        "skor_keyakinan": skor,
        "label_keyakinan": confidence_label,
        "catatan": catatan,
    }


def main():
    hasil = [deteksi_kasus(c) for c in CASES]
    hasil_terurut = sorted(hasil, key=lambda r: r["skor_keyakinan"], reverse=True)

    print("=" * 78)
    print("JEJAK KEPATUHAN — HASIL DETEKSI PURWARUPA (DATA SIMULASI)")
    print("=" * 78)
    for r in hasil_terurut:
        print(f"\n[{r['id']}] {r['perusahaan']} ({r['skala_usaha']})")
        print(f"  Status kontrak terdeteksi : {r['ekstraksi']['status_kontrak']}  |  Dilaporkan ke BPJS: {r['ekstraksi']['status_dilaporkan']}")
        if r["ekstraksi"]["selisih_upah_persen"] is not None:
            print(f"  Upah slip vs dilaporkan   : Rp{r['ekstraksi']['upah_slip']:,} vs Rp{r['ekstraksi']['upah_dilaporkan']:,}  (selisih {r['ekstraksi']['selisih_upah_persen']}%)")
        if r["flags"]:
            print(f"  INDIKASI: {'; '.join(r['flags'])}")
            print(f"  Rujukan pasal: {', '.join(r['pasal_rujukan'])}")
        print(f"  Skor keyakinan: {r['skor_keyakinan']}%  ({r['label_keyakinan']})")
        for c in r["catatan"]:
            print(f"  Catatan: {c}")

    ringkasan = {
        "total_kasus": len(hasil),
        "prioritas_tinggi": sum(1 for r in hasil if r["label_keyakinan"] == "Tinggi"),
        "prioritas_sedang": sum(1 for r in hasil if r["label_keyakinan"] == "Sedang"),
        "prioritas_rendah": sum(1 for r in hasil if r["label_keyakinan"] == "Rendah"),
        "tidak_ada_indikasi": sum(1 for r in hasil if r["label_keyakinan"] == "Tidak Ada Indikasi"),
        "estimasi_total_selisih_upah_bulanan": sum(
            (r["ekstraksi"]["upah_slip"] - r["ekstraksi"]["upah_dilaporkan"])
            for r in hasil
            if r["ekstraksi"]["upah_slip"] and r["ekstraksi"]["upah_dilaporkan"]
            and r["ekstraksi"]["upah_slip"] > r["ekstraksi"]["upah_dilaporkan"]
        ),
    }

    print("\n" + "=" * 78)
    print("RINGKASAN")
    print("=" * 78)
    for k, v in ringkasan.items():
        print(f"  {k}: {v:,}" if isinstance(v, int) else f"  {k}: {v}")

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump({"ringkasan": ringkasan, "kasus": hasil_terurut}, f, ensure_ascii=False, indent=2, default=str)

    print("\nDisimpan ke results.json")


if __name__ == "__main__":
    main()
