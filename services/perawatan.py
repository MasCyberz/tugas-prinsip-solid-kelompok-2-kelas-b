class Perawatan:
    def rawat(self, hewan):
        print(f"\nSedang merawat {hewan.nama}...")
        
        if hasattr(hewan, "terbang"):
            hewan.terbang()

        if hasattr(hewan, "berenang"):
            hewan.berenang()

        if hasattr(hewan, "berlari"):
            hewan.berlari()

        print(f"{hewan.nama} selesai dirawat.")