**DOKUMEN 1: README_JO.md (Catatan Internal & Catatan Pribadi)**

```markdown
# 📓 CATATAN PRIBADI & JURNAL PROYEK — JEJAK KEPATUHAN
**Inisiasi Proyek:** 7 Oktober 2026  
**Pengembang Utama:** Johannes HP Sipahutar, S.H., CLA  
**Kategori:** Healthkathon BPJS Kesehatan 2026 — *Non-Programmer (Employer Risk Efficiency)*

---

## 📜 Rekam Jejak Perkembangan (Chronological Milestone Log)

### 🔴 Fase 1: Konseptualisasi & Fondasi Hukum (7 Oktober 2026)
* **Inisiasi Ide:** Perancangan konsep awal "JEJAK Kepatuhan" sebagai instrumen audit otomatis untuk memetakan dua modus utama pelanggaran pemberi kerja: *under-reporting upah* dan *misklasifikasi status hubungan kerja*.
* **Penyusunan Dasar Hukum:** Mengunci parameter pemeriksaan berbasis aturan perundang-undangan eksplisit:
  * Pasal 15 UU No. 24/2011 (Kewajiban pendaftaran dan pelaporan data upah yang benar).
  * Pasal 59 UU No. 6/2023 jo. PP No. 35/2021 (Ketentuan PKWT/Harian Lepas yang batal demi hukum menjadi PKWTT).

### 🟡 Fase 2: Mesin Deteksi & Dataset Awal (21 Oktober 2026)
* **Pembangunan Python Engine:** Pembuatan skrip `engine.py` dan `logger_jejak.py` untuk pemrosesan teks, komparasi data slip gaji vs data laporan BPJS Kesehatan, serta eksekusi *rule-based matching*.
* **Dataset Simulasi:** Penyusunan 12 hingga 50 data fiktif sampel entitas pemberi kerja lintas sektor (PPU, PBPU, BP, PBI APBN, dan PBI APBD).
* **Rancangan Purwarupa:** Pembuatan antarmuka web awal untuk memvisualisasikan temuan audit kepatuhan.

### 🟢 Fase 3: Integrasi Standalone Client-Side & GitHub Pages (22 Oktober 2026)
* **Client-Side HTML Full Integration:** Memindahkan seluruh mesin pemrosesan dan OCR Tesseract.js agar berjalan 100% *client-side* tanpa server luar di berkas `demo_jejak.html` dan `dashboard-live.html`.
* **Koneksi Dynamic Interoperability:** Mengirimkan hasil *Single Upload / Scan OCR* dari `demo_jejak.html` langsung ke `dashboard-live.html` menggunakan browser `localStorage`, dilengkapi penanda khusus bertuliskan **`[INPUTAN BARU]`**.
* **Eskalasi Finansial & Nilai Bisnis Strategis:** Skalasi nilai selisih upah sampel ke tingkat Miliar Rupiah dan ekstrapolasi proyeksi pemulihan iuran nasional hingga **Rp 1,85 Triliun**.
* **Keamanan Veto Master:** Penerapan skema otorisasi bertingkat (*Auditor* vs *Veto Master*) yang dilindungi enkripsi kriptografi SHA-256 (`d2d5382d34c986025cc325400def54b30257df34fc45e1fcd2731f8fea5eb73d`) serta kunci *anti-brute-force*.
* **Peluncuran GitHub Pages:** Publikasi repositori resmi di `https://github.com/Parulian-290/jejak-kepatuhan-prototype`.

---

## 💻 Panduan Perintah Git Terminal / Command Prompt Lokal

```cmd
:: 1. Masuk ke folder lokal proyek
cd "%USERPROFILE%\Documents\00aHealthkathon 2026\PANDUAN NEXT LEVEL UP\Menggunakan GEMINI sipahutar819gmail"

:: 2. Cek status berkas
git status

:: 3. Tambahkan perubahan & buat komit
git add .
git commit -m "Update integrasi 50 kasus PSTV08, penanda INPUTAN BARU, dan analisis hukum"

:: 4. Kirim ke repositori GitHub Pages
git push origin main

```

---

## 🎯 Rencana Tindak Lanjut (RTL) Pasca-Healthkathon

1. **Auto Notice Teguran:** Penerbitan draft Surat Pemberitahuan Kepatuhan otomatis saat indikasi *under-reporting* > 20%.
2. **Data Matching PBI:** Verifikasi silang NIK pekerja PPU yang masih terdaftar sebagai penerima subsidi PBI APBN/APBD.
3. **Targeted Field Audit:** Penjadwalan pemeriksaan lapangan terfokus pada 20% Badan Usaha berisiko tertinggi.

```

---

**DOKUMEN 2: README.md (Versi Resmi untuk Repositori GitHub)**

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