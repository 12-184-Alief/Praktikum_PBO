class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        if other == 0:
            return "Tidak terdefinisi"
        return self.value / other

    def __pow__(self, exponent):
        return self.value ** exponent

    def log(self, base):
        if self.value <= 0 or base <= 0:
            return "Logaritma tidak terdifinisi"
        import math
        return math.log(self.value, base)

def main():
    print("Kalkulator Sederhana")
    nilai_awal = float(input("Masukkan angka awal: "))
    calculator = Calculator(nilai_awal)

    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Eksponen (^)")
        print("6. Logaritma (log)")
        print("7. Keluar")

        pil = input("Masukkan pilihan (1-7): ")

        if pil == '7':
            print("Terima kasih.")
            break

        if pil in ['1', '2', '3', '4', '5']:
            number = float(input("Masukkan Angka: "))
            if pil == '1':
                result = calculator + number
            elif pil == '2':
                result = calculator - number
            elif pil == '3':
                result = calculator * number
            elif pil == '4':
                result = calculator / number
            elif pil == '5':
                result = calculator ** number
            print(f"Hasil: {result}")

        elif pil == '6':
            print("Masukkan basis logaritma:")
            base = float(input())
            result = calculator.log(base)
            print(f"Hasil: {result}")

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
