# Dependency Inversion Principle (DIP)
# Analisis oleh: Amelia (K3525049)

# =============================================
# ANALISIS DEPENDENCY INVERSION PRINCIPLE (DIP)
# =============================================

# Definisi DIP:
# Kelas tingkat tinggi tidak boleh bergantung pada Kelas tingkat rendah. 
# Keduanya harus bergantung pada abstraksi.

# ---------------------------------------------
# PELANGGARAN DIP PADA KODE :
# ---------------------------------------------

# Pada kode Program sebelumnya belum sesuai dengan DIP karena kodenya yang masih 
# membuat kelas utama yang yaitu KebunBinatang memiliki ketergantungan pada 
# kelas pendukung yaitu Kandang. Letak kesalahanya seperti : 

# 1. Di dalam class KebunBinatang, terdapat pembuatan objek secara langsung 
#   melalui baris self.kandang = Kandang(). Hal ini bisa membuat kedua class 
#   tersebut menjadi sangat terikat dan sulit dipisahkan.

# 2. Prinsip DIP mengharuskan class yang lebih besar tidak boleh bergantung 
#   pada class yang lebih kecil, melainkan harus melalui sebuah perantara 
#   atau abstraksi. 

# 3. Jika suatu saat akan ada perubahan pada cara penyimpanan hewan atau 
#   jenis kandang, maka harus mengubah isi class KebunBinatang secara manual. 
#   Hal ini tidak efisien dan bisa menimbulkan error jika program berkembang 
#   menjadi lebih besar.

# SOLUSI PERBAIKAN:
# 1. Membuat agar kelas utama tidak bergantung pada kelas pendukung dengan cara
#    memasukkan objek Kandang dari luar , sehingga kelas utama tidak lagi memproses
#    pembuatan objek pendukung di dalam kodenya sendiri.
# 2. Mengubah constructor __init__ pada class KebunBinatang agar menerima parameter kandang.
#    Jadi, class ini sekarang menerima objek dari luar, bukan membuatnya sendiri.
# 3. Membuat objek my_kandang terlebih dahulu, lalu memasukkannya ke dalam KebunBinatang(my_kandang).
#    Hal ini dilakukan agar sesuai dengan DIP dimana kelas utama harus menerima ketergantugan dari luar.

# ======= KODE SEBELUM PERBAIKAN (Yang melanggar DIP) =======

class Kandang:
    def __init__(self):
        self.hewan_list = []

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang() 

# ======= KODE SESUDAH PERBAIKAN (Yang memenuhi DIP) =======

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

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan biji.")
    
    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Singa(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan daging.")

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

# ======= TEST =======
if __name__ == "__main__":
    print("=== Menjalankan Solusi DIP (Amelia) ===")
    my_kandang = Kandang()
    my_kandang.tambah_hewan(Singa("Simba"))
    my_kandang.tambah_hewan(Burung("Mprit"))

    kebun_binatang = KebunBinatang(my_kandang)
    kebun_binatang.rawat_semua_hewan()
