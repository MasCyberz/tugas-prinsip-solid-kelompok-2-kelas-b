from abc import ABC, abstractmethod

# ANALISIS KESALAHAN

# 1. SRP (Single Responsibility Principle)
#    Class Kandang memiliki 2 tugas:
#    - Menyimpan hewan
#    - Membersihkan kandang
#
#    Solusi:
#    Pisahkan fitur membersihkan kandang ke class baru bernama PembersihKandang.


# 2. ISP (Interface Segregation Principle)
#    Semua hewan dipaksa memiliki method terbang().
#
#    Padahal:
#    - Burung bisa terbang
#    - Kucing tidak bisa terbang
#
#    Solusi:
#    Buat interface khusus untuk hewan yang memang bisa terbang.


# 3. OCP (Open/Closed Principle)
#    Jika nanti ada hewan berenang, maka class Hewan harus diubah lagi.
#
#    Solusi:
#    Pisahkan perilaku menjadi interface agar mudah dikembangkan tanpa mengubah class lama.


# 4. DIP (Dependency Inversion Principle)
#    KebunBinatang langsung membuat object Kandang.
#
#    self.kandang = Kandang()
#
#    Solusi:
#    Gunakan dependency injection agar lebih fleksibel dan mudah dikembangkan.


# PERBAIKAN KODE SESUAI SOLID

# ABSTRACT CLASS

class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass


# INTERFACE PERILAKU

class BisaTerbang:
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class BisaBerenang:
    def berenang(self):
        print(f"{self.nama} sedang berenang.")

class BisaBerlari:
    def berlari(self):
        print(f"{self.nama} sedang berlari.")


# IMPLEMENTASI HEWAN

class Singa(Hewan, BisaBerlari):
    def makan(self):
        print(f"{self.nama} sedang makan daging.")

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

class Ikan(Hewan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan pelet.")

# KANDANG

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)


# PEMBERSIHAN KANDANG

class PembersihanKandang:
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


# KEBUN BINATANG

class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:

            hewan.makan()

            if isinstance(hewan, BisaTerbang):
                hewan.terbang()

            if isinstance(hewan, BisaBerenang):
                hewan.berenang()

            if isinstance(hewan, BisaBerlari):
                hewan.berlari()


# TEST PROGRAM

if __name__ == "__main__":

    kandang = Kandang()

    kandang.tambah_hewan(Singa("Simba"))
    kandang.tambah_hewan(Burung("Elang"))
    kandang.tambah_hewan(Ikan("Nemo"))

    kebun_binatang = KebunBinatang(kandang)

    kebun_binatang.rawat_semua_hewan()

    print()

    pembersihan = PembersihanKandang()
    pembersihan.bersihkan_kandang()