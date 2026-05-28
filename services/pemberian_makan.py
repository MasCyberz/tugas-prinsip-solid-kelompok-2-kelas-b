class PemberianMakan:
    def beri_makan(self, hewan):
        print(f"\nMemberi makan {hewan.nama}...")
        hewan.makan()
        print(f"{hewan.nama} sudah selesai makan.")