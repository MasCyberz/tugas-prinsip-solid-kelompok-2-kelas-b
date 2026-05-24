# Interface Segregation Principle (ISP)
# Analisis oleh: Bintang

"""
Interface Segregation Principle (ISP) merupakan salah satu prinsip
SOLID yang menyatakan bahwa sebuah class tidak boleh dipaksa
menggunakan method yang sebenarnya tidak dibutuhkan.

Pada kode program awal, class Hewan memiliki method:
1. makan()
2. terbang()

Permasalahan muncul karena tidak semua hewan memiliki kemampuan
untuk terbang. Contohnya ikan, sapi, dan kucing.

tetapi seluruh object dari class Hewan tetap mendapatkan method
terbang(), sehingga program melanggar prinsip ISP.

Akibat pelanggaran ISP:
1. Struktur program kurang fleksibel
2. Sulit dikembangkan
3. Method tidak relevan dimiliki semua object
4. Kode menjadi kurang efisien

Solusi:
Memisahkan perilaku terbang ke dalam class khusus agar hanya
hewan tertentu saja yang memiliki kemampuan tersebut.
"""


# Class dasar hewan
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")


# Class khusus hewan yang bisa terbang
class HewanTerbang(Hewan):
    def terbang(self):
        print(f"{self.nama} sedang terbang.")


# Object hewan biasa
kucing = Hewan("Kitty", "Kucing")

# Object hewan terbang
burung = HewanTerbang("Elang", "Burung")


# Menjalankan program
kucing.makan()

burung.makan()
burung.terbang()