# Liskov Substitution Principle (LSP)
# Analisis oleh: Keisha

"""
=============================================
ANALISIS LISKOV SUBSTITUTION PRINCIPLE (LSP)
=============================================

Definisi LSP:
Subclass harus bisa menggantikan parent class-nya
tanpa menyebabkan error atau mengubah perilaku program.

---------------------------------------------
PELANGGARAN LSP PADA KODE AWAL:
---------------------------------------------

1. Class Singa mewarisi method terbang() dan berenang()
   dari class Hewan, tetapi kedua method tersebut
   melempar Exception karena Singa tidak bisa melakukan
   hal tersebut. Ini melanggar LSP karena mengganti
   objek Hewan dengan Singa bisa menyebabkan program crash.

2. Class Burung mewarisi method berenang() dari class Hewan,
   tetapi melempar Exception. Burung tidak bisa berenang,
   sehingga method ini tidak valid untuk subclass ini.

3. Class Ikan mewarisi method terbang() dan berlari()
   dari class Hewan, tetapi keduanya melempar Exception.
   Ikan tidak bisa terbang maupun berlari.

---------------------------------------------
SOLUSI PERBAIKAN:
---------------------------------------------

Pisahkan kemampuan hewan ke dalam class-class terpisah
(BisaTerbang, BisaBerenang, BisaBerlari), lalu setiap
subclass hanya mewarisi kemampuan yang sesuai.
Dengan begitu, tidak ada method yang di-override
dengan Exception, dan LSP terpenuhi.
"""

# ======= KODE SEBELUM PERBAIKAN (Melanggar LSP) =======

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

    def berenang(self):
        print(f"{self.nama} sedang berenang.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")


class Singa(Hewan):
    def terbang(self):
        raise Exception("Singa tidak bisa terbang!")  # Melanggar LSP

    def berenang(self):
        raise Exception("Singa tidak bisa berenang!")  # Melanggar LSP


class Ikan(Hewan):
    def terbang(self):
        raise Exception("Ikan tidak bisa terbang!")  # Melanggar LSP

    def berlari(self):
        raise Exception("Ikan tidak bisa berlari!")  # Melanggar LSP


# ======= KODE SESUDAH PERBAIKAN (Memenuhi LSP) =======

class HewanV2:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan.")


class BisaTerbang:
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class BisaBerenang:
    def berenang(self):
        print(f"{self.nama} sedang berenang.")


class BisaBerlari:
    def berlari(self):
        print(f"{self.nama} sedang berlari.")


class SingaV2(HewanV2, BisaBerlari):
    pass


class BurungV2(HewanV2, BisaTerbang):
    pass


class IkanV2(HewanV2, BisaBerenang):
    pass


# ======= TEST =======
print("=== Setelah Perbaikan ===")
singa = SingaV2("Simba")
singa.makan()
singa.berlari()

burung = BurungV2("Tweety")
burung.terbang()

ikan = IkanV2("Nemo")
ikan.berenang()