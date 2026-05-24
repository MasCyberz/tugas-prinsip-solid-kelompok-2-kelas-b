from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def pelihara(self):
        pass

class Burung(Hewan):
    def pelihara(self):
        print("Burung diberi makan dan dilepas terbang.")

class Kucing(Hewan):
    def pelihara(self):
        print("Kucing diberi makan dan diajak bermain.")

class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.pelihara()