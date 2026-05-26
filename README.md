# Latihan Analisis Prinsip SOLID

Repository ini berisi tugas analisis penerapan prinsip **SOLID** pada program Python sederhana tentang sistem kebun binatang.
Tugas dilakukan secara berkelompok dengan pembagian analisis setiap prinsip SOLID dan sinkronisasi menggunakan GitHub.

---

## Deskripsi Tugas

Pada tugas ini, kami diminta untuk:

1. Menganalisis apakah kode program sudah memenuhi prinsip SOLID.
2. Menentukan prinsip SOLID yang sudah terpenuhi maupun yang masih dilanggar.
3. Memberikan solusi dan perbaikan kode agar sesuai dengan semua prinsip SOLID.
4. Melakukan pengerjaan secara berkelompok dan sinkronisasi project menggunakan GitHub.

---

# Pembagian Tugas Kelompok

| Nama Anggota | Tugas |
|---|---|
| Gayuh | Mengerjakan bagian hewan |
| Rindy | Mengerjakan bagian zoo |
| Keisha | Mengerjakan bagian interface |
| Bintang | Mengerjakan bagian services |
| Amelia | Mengerjakan bagian habitat |
| Dimas | Perbaikan kode & Mengatur bagian main |

---

# Tutorial Menggunakan GitHub Desktop

## 01. Download dan Install GitHub Desktop
- Download GitHub Desktop melalui website resmi GitHub.
- Install aplikasi seperti biasa sampai selesai.

Link:
[https://desktop.github.com/](https://desktop.github.com/download/)

---

## 02. Login Akun GitHub
- Buka GitHub Desktop.
- Klik **Sign in to GitHub.com**.
- Login menggunakan akun GitHub masing-masing.

---

## 03. Clone Repository GitHub
- Pilih menu **File → Clone Repository**.
- Pilih repository kelompok yang sudah dibuat.
- Tentukan lokasi penyimpanan project di komputer.
- Klik **Clone**.

---

## 04. Sinkronisasi Perubahan Teman
- Sebelum mulai mengerjakan, klik **Fetch Origin** atau **Pull Origin** (jika ada pembaruan). Biasanya ini dibagian menu atas atau di kanan tengah atas yang berbentuk tombol
- Tujuannya agar file project selalu update dan tidak bentrok dengan perubahan anggota lain.

---

## 05. Membuka Folder Project
- Setelah repository berhasil di-clone, klik **Show in VSCode** (atau Show in Explorer jika ingin membuka foldernya manual).

---

## 06. Membuat Branch Baru (Bukan Branch Utama)
Sebelum mulai coding, pastikan kamu tidak bekerja langsung di branch main.
- Di GitHub Desktop, klik menu Current Branch di bagian atas.
- Klik tombol New Branch.
- Beri nama branch sesuai dengan fitur atau tugas yang sedang kamu kerjakan (contoh: analisis-srp atau perbaikan-bug-srp).
- Klik Create Branch.

---

## 07. Membuat atau Mengedit File
- Sekarang kamu sudah berada di branch barumu. Buka VS Code dan kerjakan bagianmu masing-masing.
- Contoh format file: `srp_analisis_dimas.py`
- Contoh isi `srp_analisis_dimas.py`:

```python id="a4f61z"
# Single Responsibility Principle
# Analisis oleh: Nama Kalian

"""
Class Hewan melanggar SRP karena memiliki
lebih dari satu tanggung jawab:
1. Menyimpan data hewan
2. Mengatur perilaku makan
3. Mengatur perilaku terbang
"""

class Hewan:
    pass
```

---

## 08. Commit Perubahan
- Setelah selesai coding dan menyimpan file:
  - Buka GitHub Desktop
  - Isi kolom **Summary**, bagian kiri bawah
  - Contoh:
    ```bash
    Menambahkan analisis SRP - Ken Gayuh
    ```
- Klik tombol Commit to **[nama-branch-kamu]**.

---

## 09. Push ke GitHub
- Setelah commit berhasil, klik tombol **Publish branch** (atau Push origin), biasanya ini ada di menu atas atau di tampilan utama github desktop
- Tujuannya agar perubahan tersimpan di repository GitHub online.

---

## 10. Membuat Pull Request (PR)
Setelah sukses melakukan push, saatnya menggabungkan code kamu ke branch utama melalui review kelompok.
- Di GitHub Desktop, akan muncul tombol biru bertuliskan Create Pull Request. Klik tombol tersebut.
- Kamu akan otomatis diarahkan ke browser (halaman web GitHub).
- Periksa kembali perubahanmu, isi deskripsi PR jika diperlukan, lalu klik tombol Create pull request di halaman web tersebut.
- Selesai! Anggota kelompok lain atau ketua proyek sekarang bisa memeriksa dan melakukan merge code kamu ke branch **main**.

---

## 11. Sinkronisasi Perubahan Kembali
- Setelah mengerjakan, klik **Fetch Origin** atau **Pull Origin** lagi.
- Tujuannya agar file project selalu update dan tidak bentrok dengan perubahan anggota lain.

---

# Teknologi yang Digunakan

- Python 3
- GitHub Desktop
- Visual Studio Code

---

# Kesimpulan

Dari hasil analisis, kode awal belum memenuhi seluruh prinsip SOLID karena masih terdapat beberapa hal, seperti pemaksaan method `terbang()` kepada semua hewan dan ketergantungan langsung antar class.

Dengan melakukan refactor menggunakan abstract class dan pemisahan interface, kode menjadi:

* lebih fleksibel
* mudah dikembangkan
* lebih terstruktur
* sesuai dengan prinsip SOLID

---

## Author

Kelompok 2 
Mata Kuliah Pemrograman Berorientasi Object  
Universitas Sebelas Maret
