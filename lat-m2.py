# Mohd.Musyaffa Alief Athallah
# 123140184
# Praktikum PBO RA

class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")

    def bergerak(self):
        print("Kendaraan sedang bergerak.")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        self.info_kendaraan()
        print(f"Merk Mobil: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

    def bunyikan_klakson(self):
        print("Mobil memutar klakson: Beep beep!")

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self._tenaga_kuda = tenaga_kuda  # Private attribute
        self._harga = harga                # Private attribute

    def get_tenaga_kuda(self):
        return self._tenaga_kuda

    def set_tenaga_kuda(self, tenaga_kuda):
        self._tenaga_kuda = tenaga_kuda

    def get_harga(self):
        return self._harga

    def set_harga(self, harga):
        self._harga = harga

    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda: {self._tenaga_kuda} HP")
        print(f"Harga: {self._harga} juta rupiah")

    def mode_balap(self):
        print("Mobil sport masuk ke mode balap!")

kendaraan = Kendaraan("Darat", 120)
kendaraan.info_kendaraan()
kendaraan.bergerak()

print("\n")

mobil = Mobil("Darat", 200, "Toyota", 4)
mobil.info_mobil()
mobil.bunyikan_klakson()

print("\n")

mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 720, 10000)
mobil_sport.info_mobil_sport()
mobil_sport.mode_balap()

print("\n")

print(f"Tenaga Kuda sebelum diubah: {mobil_sport.get_tenaga_kuda()} HP")
mobil_sport.set_tenaga_kuda(750)
print(f"Tenaga Kuda setelah diubah: {mobil_sport.get_tenaga_kuda()} HP")

print(f"Harga sebelum diubah: {mobil_sport.get_harga()} dollar USD")
mobil_sport.set_harga(12000)
print(f"Harga setelah diubah: {mobil_sport.get_harga()} dollar USD")
