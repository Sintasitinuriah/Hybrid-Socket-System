# Hybrid-Socket-System
Repository ini dibuat guna memenuhi tugas matakuliah Jaringan Komputer Lanjut

# 🚀 Hybrid Socket Message & File Distribution System

Proyek ini adalah implementasi aplikasi Client-Server berbasis Command Line Interface (CLI) menggunakan bahasa pemrograman Python 3. Sistem ini dirancang untuk mendemonstrasikan dua jenis layanan jaringan yang berjalan berdampingan: **Multi-Threaded TCP Server** untuk transmisi pesan konkuren dan **UDP Heartbeat/Pinger** untuk mengukur kualitas jaringan (RTT & Packet Loss).

---

## ✨ Fitur Utama

- **TCP Server (Multi-Threaded):**
  - Mampu menangani banyak klien (`N` koneksi) secara bersamaan menggunakan modul `threading`.
  - Mengimplementasikan protokol *message boundary* menggunakan delimiter (`\n`) untuk mengatasi masalah *Byte Stream HOL Blocking*.
- **UDP Heartbeat Server:**
  - Melayani *ping* berkala dari klien.
  - Memiliki fitur **simulasi packet loss** (acak) untuk menguji keandalan penanganan klien.
  - Klien UDP dilengkapi batas *timeout* 1 detik untuk menghitung Round Trip Time (RTT).

---

## 🛠️ Prasyarat (Prerequisites)

- **Python 3.x** terinstal pada sistem operasi Anda (Windows, macOS, atau Linux).
- Tidak memerlukan *library* eksternal tambahan (menggunakan modul bawaan Python: `socket`, `threading`, `time`, `random`).

---

## 🚀 Cara Menjalankan Aplikasi

Lakukan pengujian aplikasi pada terminal/Command Prompt Anda. Anda membutuhkan beberapa jendela terminal yang dibuka secara bersamaan.

### 1. Menjalankan Layanan TCP
1. Buka terminal pertama, arahkan ke direktori proyek, dan jalankan server TCP:
   ```bash
   python TCPServer.py
2. Buka terminal kedua, arahkan ke direktori proyek, dan jalankan client TCP:
   ```bash
   python TCPclient.py

### 2. Menjalankan Layanan UDP
1. Buka terminal pertama, arahkan ke direktori proyek, dan jalankan server UDP:
   ```bash
   python UDPServer.py
2. Buka terminal kedua, arahkan ke direktori proyek, dan jalankan client UDP:
   ```bash
   python UDPclient.py

## 📊 Hasil Pengujian Wireshark
Contoh hasil percobaan Wireshark pada project ini. Disertakan gambar pengujian terminal dan hasil Wireshark untuk TCP dan UDP-nya:

Pengujian Terminal
![Terminal TCP & UDP](/Screenshot 2026-09-15 110834.png)
Tangkapan layar terminal saat pengujian TCP Server-Client dan UDP Pinger dengan simulasi packet loss.

Analisis Wireshark: Proses TCP
![Wireshark TCP](/Screenshot 2026-09-15 111905.png)
Proses pengiriman paket dengan flag [PSH, ACK] dari klien dan [ACK] dari server, menandakan transfer data yang andal.

Analisis Wireshark: Proses UDP
![Wireshark UDP](/Screenshot 2026-09-15 112104.png)
Paket data mentah (datagram) di layer bawah (LLC/IP) dengan tujuan dan sumber ke port 12000 secara connectionless.


##👨‍💻 Informasi Pembuat
Nama: Sinta Siti Nuriah

Institusi: Universitas Gadjah Mada

Mata Kuliah: Jaringan Komputer Lanjut (S2 Ilmu Komputer)