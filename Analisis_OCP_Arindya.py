# Open/Closed Principle
# Analisis oleh: ARINDYA AULIA WARDAH (K3525050)

# Analisis kesalahan:
# 1. class Hewan memiliki method terbang(), padahal tidak semua hewan bisa terbang.
#    sehingga jika ada hewan baru seperti singa atau ikan,
#    kode lama harus dimodifikasi agar program tetap berjalan benar.
# 2. class KebunBinatang, semua hewan langsung dipanggil method terbang().
#    Jika ditambahkan jenis hewan baru yang tidak bisa terbang, 
#    maka kode lama harus diubah lagi
# 3. Melanggar prinsip Open/Closed Principle karena program tidak tertutup terhadap modifikasi.
#    Setiap ada penambahan fitur atau jenis hewan baru, kode lama harus ikut diubah.

# Langkah Perbaikan:
# 1. Memisahkan kemampuan terbang ke class tersendiri,
#    sehingga hanya hewan tertentu yang memiliki method terbang().
# 2. Membuat class dasar Hewan yang berisi perilaku umum seperti makan.
# 3. Menambahkan hewan baru bisa dilakukan dengan membuat class baru
#    tanpa mengubah kode yang sudah ada.

# kode pembenaran dari prinsip Open/Closed Principle:
from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class Singa(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan daging.")

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Kandang:
    def __init__(self):
        self.hewan_list = []
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()

            if isinstance(hewan, BisaTerbang):
                hewan.terbang()