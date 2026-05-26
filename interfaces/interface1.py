# interfaces/interfaces.py
# Dibuat oleh: Keisha

from abc import ABC, abstractmethod

# ============================================
# INTERFACE - BISA TERBANG
# ============================================
# Interface ini digunakan sebagai "kontrak" untuk
# hewan-hewan yang memiliki kemampuan terbang.
# Contoh: Burung, Kelelawar
# Hewan yang tidak bisa terbang (Singa, Ikan)
# TIDAK boleh mengimplementasikan interface ini.

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass


# ============================================
# INTERFACE - BISA BERENANG
# ============================================
# Interface ini digunakan sebagai "kontrak" untuk
# hewan-hewan yang memiliki kemampuan berenang.
# Contoh: Ikan, Pinguin
# Hewan yang tidak bisa berenang (Singa, Burung)
# TIDAK boleh mengimplementasikan interface ini.

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass
