# SRP
# Analisis oleh: 
# Nama : KEN GAYUH NUSA ISLAMI
# NIM  : K3525031


# Analisis kesalahan:
# 1.  class hewan memiliki 3 tanggungjawab tetapi tetap dijadikan 1, dan ada yang dipaksakan yaitu method terbang
#     method terbang disini dipaksakan yang padahal tidak semua hewan bisa terbang.
# 2.  class kandang, disini kelas kandang memiliki 2 tanggungjawab tetapi tetap dijadikan 1, 2 tanggungjawab
#     tersebut adalah menggelola hewan dan membersihkan kandang. Jika seandainya cara membersihkan berubah, 
#     kelas ini harus dimodifikasi, padahal pengelolaan hewan belum tentu berubah.

# Langkah Perbaikan:
# 1.  Memisahkan class Hewan menjadi 3 class yaitu:
#     1. Menyimpan data hewan
#     2. Mengatur perilaku makan
#     3. Mengatur perilaku terbang
# 2.  Memisahkan class Kandang menjadi 2 class yaitu:
#     1. Untuk menggelola hewan
#     2. Untuk membersihkan kandang hewan
# Jadi dengan begitu semua memiliki tugas dan tanggungjawabnya masing-masing, inilah
# sebenarnya konsep dari prinsip Single Responsibility dimana 1 class memiliki tanggungjawabnya sendiri.

# Berikut ini untuk kode program yang sudah memenuhi prinsip Single Responsibility:

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

class Makanan:
    def makan(hewan):
        print(f"{hewan.nama} sedang makan.")

class HewanTerbang:
    def terbang(hewan):
        print(f"{hewan.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

class PembersihanKandang:
    def bersihkan_kandang(kandang):
        print("Kandang dibersihkan.")