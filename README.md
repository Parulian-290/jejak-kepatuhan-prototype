# JEJAK Kepatuhan

**Purwarupa mesin audit kepatuhan pemberi kerja berbasis AI untuk BPJS Kesehatan.**
Dibangun untuk Healthkathon 2026 — kategori *Efisiensi Risiko pada Pemberi Kerja*.

> Seluruh data dalam repo ini adalah **data simulasi/fiktif**. Tidak ada data peserta JKN sungguhan yang digunakan atau disimpan.

---

## Apa ini?

JEJAK Kepatuhan membaca dokumen ketenagakerjaan (kontrak kerja, slip gaji) dan
menyilangkannya dengan data yang dilaporkan ke BPJS Kesehatan, untuk menemukan
dua modus ketidakpatuhan pemberi kerja:

- **Misklasifikasi status kerja** — status kerja sebenarnya (PKWTT) dilaporkan
  sebagai status lain (tenaga lepas/PKWT) untuk menekan kewajiban iuran.
- **Under-reporting upah** — upah yang dilaporkan ke BPJS lebih rendah dari
  upah sebenarnya di slip gaji.

Setiap temuan disertai **rujukan pasal hukum eksplisit** (bukan skor anomali
statistik semata) dan skor keyakinan yang dikalibrasi berbeda untuk UMKM
(mitigasi bias terhadap pelaku usaha kecil dengan dokumen kurang formal).

## Cara menjalankan

Butuh Python 3.9+, tanpa dependency eksternal (hanya pustaka standar).

```bash
git clone https://github.com/<username>/jejak-kepatuhan-prototype.git
cd jejak-kepatuhan-prototype
python3 engine.py              # jalankan deteksi atas 12 kasus simulasi
python3 render_dashboard.py    # render dashboard auditor dari hasil deteksi
open dashboard-live.html       # (atau buka manual di browser)
```

## Struktur

```
.
├── dataset.py              # 12 kasus simulasi (kontrak, slip gaji, data BPJS)
├── engine.py                # ekstraksi + validasi terhadap dasar hukum
├── render_dashboard.py      # merender dashboard HTML dari hasil engine
├── results.json              # output engine (dibuat ulang tiap dijalankan)
├── dashboard-live.html      # dashboard auditor (dibuat ulang tiap dijalankan)
└── README.md                 # dokumentasi teknis lebih lengkap
```

## Dasar hukum yang diimplementasikan

| Aturan | Pasal | Diterapkan untuk |
|---|---|---|
| UU No. 6/2023 (Cipta Kerja) | Pasal 59 ayat (3) | PKWT tanpa syarat sah → demi hukum jadi PKWTT |
| PP No. 35/2021 | Pasal 8 | PKWT melebihi 5 tahun → demi hukum jadi PKWTT |
| UU No. 24/2011 (BPJS) | Pasal 15 ayat (1) | Kewajiban melaporkan data & upah yang benar |

## Status proyek

🟡 **Prototype** — logika deteksi berjalan penuh di atas data simulasi
terkontrol. Ekstraksi dokumen saat ini memakai pencocokan pola (regex)
sebagai pengganti sementara pemanggilan model bahasa (Claude), yang menjadi
rencana peningkatan utama pada tahap pengembangan berikutnya untuk menangani
dokumen dunia nyata yang jauh lebih beragam formatnya (scan, foto, tulisan
tangan).

## Lisensi & penggunaan

Kode ini dibuat untuk keperluan kompetisi Healthkathon 2026. Silakan pelajari
dan gunakan sebagai referensi dengan atribusi.

---
Dibuat oleh Johannes HP Sipahutar, S.H., CLA — dengan bantuan Claude (Anthropic)
untuk implementasi teknis.
