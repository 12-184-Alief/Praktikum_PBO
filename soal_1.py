import math

print("Program Menghitung Akar Kuadrat")

inputan_user = input("Masukkan angka: ")

try:
   
    angka = float(inputan_user)

    if angka < 0:
        print("Input tidak valid. Harap masukkan angka positif.")
    
    elif angka == 0:
        print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
    
    else:
       
        hasil_akar = math.sqrt(angka)
    
        if angka.is_integer():
             print(f"Akar kuadrat dari {int(angka)} adalah {hasil_akar}")
        else:
             print(f"Akar kuadrat dari {angka} adalah {hasil_akar}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka yang valid.")