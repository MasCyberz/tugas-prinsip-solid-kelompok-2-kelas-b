from abc import ABC, abstractmethod

# ANALISIS KESALAHAN

# 1. SRP (Single Responsibility Principle) ❌
#    Class Kandang memiliki 2 tugas:
#    - Menyimpan hewan
#    - Membersihkan kandang
#
#    Solusi:
#    Pisahkan fitur membersihkan kandang ke class baru bernama PembersihKandang.


# 2. ISP (Interface Segregation Principle) ❌
#    Semua hewan dipaksa memiliki method terbang().
#
#    Padahal:
#    - Burung bisa terbang
#    - Kucing tidak bisa terbang
#
#    Solusi:
#    Buat interface khusus untuk hewan yang memang bisa terbang.


# 3. OCP (Open/Closed Principle) ❌
#    Jika nanti ada hewan berenang, maka class Hewan harus diubah lagi.
#
#    Solusi:
#    Pisahkan perilaku menjadi interface agar mudah dikembangkan tanpa mengubah class lama.


# 4. DIP (Dependency Inversion Principle) ❌
#    KebunBinatang langsung membuat object Kandang.
#
#    self.kandang = Kandang()
#
#    Solusi:
#    Gunakan dependency injection agar lebih fleksibel dan mudah dikembangkan.


# PERBAIKAN KODE SESUAI SOLID


# Interface untuk makan
class BisaMakan(ABC):

    @abstractmethod
    def makan(self):
        pass


# Interface khusus hewan yang bisa terbang
class BisaTerbang(ABC):

    @abstractmethod
    def terbang(self):
        pass


# CLASS DASAR HEWAN

class Hewan(BisaMakan):

    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")


# CLASS BURUNG

# ANALISIS:
# Burung bisa makan dan bisa terbang. Maka class ini menggunakan interface BisaTerbang.

class Burung(Hewan, BisaTerbang):

    def terbang(self):
        print(f"{self.nama} sedang terbang.")


# CLASS KUCING

# ANALISIS:
# Kucing hanya makan dan tidak perlu method terbang(). Ini sudah sesuai prinsip ISP.

class Kucing(Hewan):
    pass


# CLASS KANDANG

# ANALISIS:
# Class ini sekarang hanya bertugas menyimpan data hewan. Ini sudah sesuai SRP.

class Kandang:

    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)


# CLASS PEMBERSIH KANDANG

# ANALISIS:
# Tugas membersihkan kandang dipisah agar tanggung jawab class tidak bercampur.

class PembersihKandang:

    def bersihkan(self):
        print("Kandang dibersihkan.")


# CLASS KEBUN BINATANG

# ANALISIS:
# Class ini menggunakan dependency injection. Jadi tidak membuat object Kandang langsung. Ini sudah sesuai DIP.

class KebunBinatang:

    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):

        for hewan in self.kandang.hewan_list:

            # Semua hewan makan
            hewan.makan()

            # Hanya hewan tertentu yang bisa terbang
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()



# PENGGUNAAN PROGRAM

# Membuat kandang
kandang = Kandang()

# Membuat object hewan
burung = Burung("Elang", "Burung")
kucing = Kucing("Milo", "Kucing")

# Menambahkan hewan ke kandang
kandang.tambah_hewan(burung)
kandang.tambah_hewan(kucing)

# Membuat kebun binatang
kebun_binatang = KebunBinatang(kandang)

# Merawat semua hewan
kebun_binatang.rawat_semua_hewan()

# Membersihkan kandang
pembersih = PembersihKandang()
pembersih.bersihkan()