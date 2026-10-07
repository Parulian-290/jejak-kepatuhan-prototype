# -*- coding: utf-8 -*-
"""
dataset.py — Set Data Simulasi JEJAK Kepatuhan

Berisi 12 "kasus" pemberi kerja simulasi. Setiap kasus punya TIGA dokumen
mentah dalam bentuk teks tidak terstruktur — persis seperti yang akan
diunggah pengguna nyata (bukan data siap-pakai/terstruktur):

  1. kontrak_kerja_text  -> teks perjanjian kerja
  2. slip_gaji_text      -> teks slip gaji bulan berjalan
  3. data_bpjs_text      -> teks ringkasan data yang tercatat di sistem BPJS

Dataset ini SENGAJA berisi campuran: kasus pelanggaran jelas, kasus
borderline/UMKM (dokumen informal), dan kasus bersih (tidak melanggar) —
supaya mesin deteksi diuji pada situasi realistis, bukan hanya kasus mudah.

SELURUH nama perusahaan, nama pekerja, dan angka adalah FIKTIF/SIMULASI
untuk keperluan purwarupa Healthkathon 2026. Tidak ada data peserta JKN
sungguhan yang digunakan.
"""

CASES = [
    {
        "id": "C-001",
        "perusahaan": "PT Cahaya Nusantara Logistik",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
Antara PT Cahaya Nusantara Logistik ("Pihak Pertama") dan Ahmad Fauzi ("Pihak Kedua").
Pihak Kedua bekerja pada Pihak Pertama sejak tanggal 12 Maret 2019 dengan jabatan
Staff Operasional Gudang. Perjanjian kerja ini berlaku tanpa batas waktu tertentu
sampai dengan berakhirnya hubungan kerja sesuai ketentuan yang berlaku.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Cahaya Nusantara Logistik - Periode Januari 2026
Nama: Ahmad Fauzi | Jabatan: Staff Operasional Gudang
Gaji Pokok: Rp 6.200.000
Tunjangan Transport: Rp 500.000
Tunjangan Makan: Rp 300.000
TOTAL DITERIMA: Rp 7.000.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Ahmad Fauzi
Pemberi Kerja: PT Cahaya Nusantara Logistik
Status Kerja Dilaporkan: Tenaga Lepas / Harian Lepas
Upah Dilaporkan: Rp 4.200.000
Tanggal Terdaftar: 02 Januari 2024
""",
    },
    {
        "id": "C-002",
        "perusahaan": "CV Mitra Sejahtera Konstruksi",
        "skala_usaha": "UMKM",
        "kontrak_kerja_text": """
SURAT PERJANJIAN KERJA WAKTU TERTENTU
CV Mitra Sejahtera Konstruksi dengan Budi Santoso, untuk pekerjaan proyek
pembangunan gudang. Masa kerja: 1 Februari 2025 s.d. 31 Januari 2026 (1 tahun).
""",
        "slip_gaji_text": """
Slip Upah Mingguan - CV Mitra Sejahtera Konstruksi
Nama: Budi Santoso
Upah per bulan (dihitung dari upah harian x 22 hari kerja): Rp 6.500.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Budi Santoso
Pemberi Kerja: CV Mitra Sejahtera Konstruksi
Status Kerja Dilaporkan: PKWT
Upah Dilaporkan: Rp 4.200.000
Tanggal Terdaftar: 05 Februari 2025
""",
    },
    {
        "id": "C-003",
        "perusahaan": "PT Graha Abadi Sentosa",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
PT Graha Abadi Sentosa dan Siti Rahayu, jabatan Admin Keuangan, bekerja sejak
3 Juni 2021, perjanjian kerja tetap tanpa batas waktu.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Graha Abadi Sentosa - Periode Januari 2026
Nama: Siti Rahayu | Jabatan: Admin Keuangan
Gaji Pokok: Rp 5.400.000
Tunjangan Jabatan: Rp 400.000
TOTAL DITERIMA: Rp 5.800.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Siti Rahayu
Pemberi Kerja: PT Graha Abadi Sentosa
Status Kerja Dilaporkan: PKWTT
Upah Dilaporkan: Rp 4.900.000
Tanggal Terdaftar: 10 Juni 2021
""",
    },
    {
        "id": "C-004",
        "perusahaan": "PT Boga Rasa Nusantara",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
PT Boga Rasa Nusantara dan Dewi Kartika, jabatan Supervisor Produksi, bekerja
sejak 15 Agustus 2020, perjanjian tanpa batas waktu tertentu.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Boga Rasa Nusantara - Periode Januari 2026
Nama: Dewi Kartika | Jabatan: Supervisor Produksi
Gaji Pokok: Rp 6.800.000
Tunjangan: Rp 700.000
TOTAL DITERIMA: Rp 7.500.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Dewi Kartika
Pemberi Kerja: PT Boga Rasa Nusantara
Status Kerja Dilaporkan: Tenaga Lepas / Harian Lepas
Upah Dilaporkan: Rp 5.900.000
Tanggal Terdaftar: 03 Januari 2024
""",
    },
    {
        "id": "C-005",
        "perusahaan": "UD Sumber Makmur",
        "skala_usaha": "UMKM",
        "kontrak_kerja_text": """
Surat Kerja - UD Sumber Makmur dan Joko Prasetyo, sebagai pramuniaga toko,
mulai bekerja 1 Maret 2024. (Dokumen ditulis tangan, tidak menyebutkan
jenis perjanjian secara eksplisit.)
""",
        "slip_gaji_text": """
Catatan gaji - UD Sumber Makmur
Joko: 4.000.000 / bulan
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Joko Prasetyo
Pemberi Kerja: UD Sumber Makmur
Status Kerja Dilaporkan: PKWT
Upah Dilaporkan: Rp 3.850.000
Tanggal Terdaftar: 04 Maret 2024
""",
    },
    {
        "id": "C-006",
        "perusahaan": "PT Teknindo Prakarsa",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TERTENTU
PT Teknindo Prakarsa dan Rudi Hartono, untuk proyek instalasi sistem IT klien,
masa kerja 1 Januari 2024 s.d. 31 Desember 2026 (3 tahun).
""",
        "slip_gaji_text": """
SLIP GAJI - PT Teknindo Prakarsa - Periode Januari 2026
Nama: Rudi Hartono | Jabatan: Teknisi IT
Gaji Pokok: Rp 5.500.000
TOTAL DITERIMA: Rp 5.500.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Rudi Hartono
Pemberi Kerja: PT Teknindo Prakarsa
Status Kerja Dilaporkan: PKWT
Upah Dilaporkan: Rp 5.500.000
Tanggal Terdaftar: 05 Januari 2024
""",
    },
    {
        "id": "C-007",
        "perusahaan": "PT Sinar Abadi Tekstil",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
PT Sinar Abadi Tekstil dan Yuni Astuti, jabatan Operator Jahit, bekerja sejak
20 April 2022, perjanjian tanpa batas waktu.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Sinar Abadi Tekstil - Periode Januari 2026
Nama: Yuni Astuti | Jabatan: Operator Jahit
Gaji Pokok: Rp 4.600.000
Tunjangan: Rp 200.000
TOTAL DITERIMA: Rp 4.800.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Yuni Astuti
Pemberi Kerja: PT Sinar Abadi Tekstil
Status Kerja Dilaporkan: PKWTT
Upah Dilaporkan: Rp 4.750.000
Tanggal Terdaftar: 25 April 2022
""",
    },
    {
        "id": "C-008",
        "perusahaan": "CV Berkah Jaya Konstruksi",
        "skala_usaha": "UMKM",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TERTENTU
CV Berkah Jaya Konstruksi dan Hendra Wijaya, untuk proyek konstruksi
berkelanjutan. Masa kerja: 1 Januari 2020 s.d. 31 Desember 2026 (7 tahun,
diperpanjang berkala tiap tahun tanpa jeda).
""",
        "slip_gaji_text": """
Slip Upah - CV Berkah Jaya Konstruksi
Nama: Hendra Wijaya
Upah per bulan: Rp 4.900.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Hendra Wijaya
Pemberi Kerja: CV Berkah Jaya Konstruksi
Status Kerja Dilaporkan: PKWT
Upah Dilaporkan: Rp 4.850.000
Tanggal Terdaftar: 03 Januari 2020
""",
    },
    {
        "id": "C-009",
        "perusahaan": "PT Kencana Wira Logistics",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
PT Kencana Wira Logistics dan Bambang Setiawan, jabatan Supir Armada,
bekerja sejak 8 Mei 2023, perjanjian tanpa batas waktu.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Kencana Wira Logistics - Periode Januari 2026
Nama: Bambang Setiawan | Jabatan: Supir Armada
Gaji Pokok: Rp 5.200.000
Tunjangan: Rp 300.000
TOTAL DITERIMA: Rp 5.500.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Bambang Setiawan
Pemberi Kerja: PT Kencana Wira Logistics
Status Kerja Dilaporkan: PKWTT
Upah Dilaporkan: Rp 5.150.000
Tanggal Terdaftar: 12 Mei 2023
""",
    },
    {
        "id": "C-010",
        "perusahaan": "PT Mekar Jaya Abadi",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
PT Mekar Jaya Abadi dan Indra Gunawan, jabatan Staff Gudang, bekerja sejak
1 Februari 2023, perjanjian tanpa batas waktu.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Mekar Jaya Abadi - Periode Januari 2026
Nama: Indra Gunawan | Jabatan: Staff Gudang
Gaji Pokok: Rp 4.700.000
TOTAL DITERIMA: Rp 4.700.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Indra Gunawan
Pemberi Kerja: PT Mekar Jaya Abadi
Status Kerja Dilaporkan: PKWTT
Upah Dilaporkan: Rp 4.700.000
Tanggal Terdaftar: 06 Februari 2023
""",
    },
    {
        "id": "C-011",
        "perusahaan": "Toko Jaya Elektronik",
        "skala_usaha": "UMKM",
        "kontrak_kerja_text": """
Surat pernyataan kerja - Toko Jaya Elektronik dan Agus Salim, sebagai
pramuniaga, mulai bekerja 15 Januari 2025.
""",
        "slip_gaji_text": """
Catatan gaji bulanan - Toko Jaya Elektronik
Agus: 3.200.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Agus Salim
Pemberi Kerja: Toko Jaya Elektronik
Status Kerja Dilaporkan: PKWT
Upah Dilaporkan: Rp 3.100.000
Tanggal Terdaftar: 18 Januari 2025
""",
    },
    {
        "id": "C-012",
        "perusahaan": "PT Andalan Prima Farma",
        "skala_usaha": "Korporasi",
        "kontrak_kerja_text": """
PERJANJIAN KERJA WAKTU TIDAK TERTENTU
PT Andalan Prima Farma dan Maya Puspita, jabatan Apoteker Pendamping,
bekerja sejak 10 September 2018, perjanjian tanpa batas waktu.
""",
        "slip_gaji_text": """
SLIP GAJI - PT Andalan Prima Farma - Periode Januari 2026
Nama: Maya Puspita | Jabatan: Apoteker Pendamping
Gaji Pokok: Rp 8.200.000
Tunjangan Profesi: Rp 800.000
TOTAL DITERIMA: Rp 9.000.000
""",
        "data_bpjs_text": """
DATA KEPESERTAAN TERDAFTAR - Sistem BPJS Kesehatan
Nama Pekerja: Maya Puspita
Pemberi Kerja: PT Andalan Prima Farma
Status Kerja Dilaporkan: Tenaga Lepas / Harian Lepas
Upah Dilaporkan: Rp 5.400.000
Tanggal Terdaftar: 02 Januari 2025
""",
    },
]
