## 🎯 Rencana Tindak Lanjut (RTL) Pasca-Healthkathon

1. **Auto Notice Teguran:** Penerbitan draft Surat Pemberitahuan Kepatuhan otomatis saat indikasi *under-reporting* > 20%.
2. **Data Matching PBI:** Verifikasi silang NIK pekerja PPU yang masih terdaftar sebagai penerima subsidi PBI APBN/APBD.
3. **Targeted Field Audit:** Penjadwalan pemeriksaan lapangan terfokus pada 20% Badan Usaha berisiko tertinggi.

```

---

README.md (Versi Resmi untuk Repositori GitHub)**

```markdown
# 🛡️ JEJAK Kepatuhan — Employer Risk Efficiency Engine

**Purwarupa Mesin Audit Kepatuhan Pemberi Kerja Berbasis AI & Kepatuhan Hukum untuk BPJS Kesehatan**  
*Dikembangkan untuk Healthkathon BPJS Kesehatan 2026 — Kategori Non-Programmer (Employer Risk Efficiency Track).*

> **Sanggahan (Disclaimer):** Seluruh data, nama entitas, dan angka yang tercantum dalam repositori ini merupakan **data simulasi/fiktif terkontrol** untuk keperluan uji coba purwarupa. Tidak ada Data Pribadi (PII) atau data peserta JKN sungguhan yang digunakan.

---

## 🌐 Tautan Web Live & Evaluasi Juri

* **Repositori Kode (GitHub):**  
  [https://github.com/Parulian-290/jejak-kepatuhan-prototype](https://github.com/Parulian-290/jejak-kepatuhan-prototype)
* **Live Dashboard Aggregator (100+ Data & Veto Master):**  
  [https://parulian-290.github.io/jejak-kepatuhan-prototype/dashboard-live.html](https://parulian-290.github.io/jejak-kepatuhan-prototype/dashboard-live.html)
* **Single Upload & OCR Scan Master (50 Preset Kasus PSTV08):**  
  [https://parulian-290.github.io/jejak-kepatuhan-prototype/demo_jejak.html](https://parulian-290.github.io/jejak-kepatuhan-prototype/demo_jejak.html)

---

## 🚀 Gambaran Umum System

**JEJAK Kepatuhan** adalah sistem analisis kepatuhan otomatis yang memindai dokumen ketenagakerjaan (Kontrak Kerja/PKWT/PKWTT, Laporan Payroll, Slip Gaji) melalui OCR client-side, lalu memadankannya dengan data pelaporan iuran BPJS Kesehatan.

Sistem secara presisi mendeteksi dua modus utama kebocoran (*leakage*) iuran:
1. **Under-Reporting Upah Massal:** Pelaporan nilai upah ke BPJS Kesehatan yang lebih rendah dibandingkan riil payroll/slip gaji.
2. **Misklasifikasi Status Hubungan Kerja:** Pengalihan status pekerja tetap (PKWTT) menjadi pekerja harian lepas atau PKWT tanpa syarat sah untuk menghindari kewajiban iuran penuh.

---

## 💰 Nilai Bisnis & Proyeksi Dampak Finansial

| Tingkatan Analisis | Skala Nilai Sampel | Indikator Dampak BPJS Kesehatan |
| :--- | :--- | :--- |
| **Sampel Entitas (UMKM)** | Rp 15 Juta – Rp 85 Juta / bulan | Koreksi selisih iuran Badan Usaha skala sedang/kecil. |
| **Sampel Entitas (Korporasi)** | Rp 250 Juta – Rp 1,8 Miliar / bulan | Penyelamatan *under-reporting* upah massal ratusan pekerja. |
| **Agregat Sampel (100 BU)** | **Rp 32,51 Miliar / bulan** | Akumulasi potensi pemulihan iuran dari sampel terpantau. |
| **Proyeksi Nasional** | **Rp 1,85 Triliun / tahun** | Proyeksi pencegahan kebocoran iuran pada Badan Usaha Wajib. |

---

## ✨ Fitur Utama Purwarupa

* **100% Client-Side Privacy:** Pemrosesan berkas OCR (Tesseract.js) dan analisis data berjalan sepenuhnya di dalam browser pengguna. Zero data leakage ke server luar.
* **Interoperabilitas Real-Time (`localStorage`):** Setiap dokumen baru yang diproses melalui `demo_jejak.html` secara otomatis masuk ke `dashboard-live.html` dan ditandai dengan badge biru **`[INPUTAN BARU]`**.
* **Cakupan Segmentasi PSTV08:** Mendukung pengujian untuk 5 kategori peserta (PPU, PBPU, BP, PBI APBN, dan PBI APBD).
* **Pengamanan Veto Master (Super User):** Proteksi akses koreksi auditor dengan enkripsi hashing **SHA-256** dan sistem penguncian otomatis (*anti-brute-force lockout*) setelah 3 kali salah kata sandi.

---

## ⚖️ Landasan Hukum & Regulasi

| Peraturan Perundang-Undangan | Pasal | Penerapan Sistem Deteksi |
| :--- | :--- | :--- |
| **UU No. 24 Tahun 2011 (BPJS)** | Pasal 15 ayat (1) | Kewajiban Pemberi Kerja mendaftarkan seluruh pekerja dan melaporkan data upah secara benar. |
| **UU No. 6 Tahun 2023 (Cipta Kerja)** | Pasal 59 ayat (3) | PKWT yang tidak memenuhi syarat demi hukum berubah menjadi PKWTT (Pekerja Tetap). |
| **PP No. 35 Tahun 2021** | Pasal 8 & Pasal 15 | Batas waktu PKWT dan kewajiban pembayaran kompensasi/iuran perlindungan sosial. |

---

## 📁 Struktur Repositori

```text
.
├── dashboard-live.html   # Live Dashboard Aggregator (100 Data + Veto Master + Modals)
├── demo_jejak.html       # Single Upload Component & OCR Scan Master (50 Preset Kasus)
├── logger_jejak.py       # Python Backend Script untuk pemrosesan log lokal
├── README.md             # Dokumentasi resmi repositori GitHub
└── README_JO.md          # Catatan internal & linimasa pengembangan proyek

```

---

## 👨‍💻 Pengembang

**Johannes HP Sipahutar, S.H., CLA**

*Advokat, Konsultan Hukum, & Pengembang Purwarupa JEJAK Kepatuhan*

Peserta Healthkathon BPJS Kesehatan 2026 — Kategori Non-Programmer.

```

```
