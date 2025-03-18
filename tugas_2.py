import random
# membantu menentukan genotipe orang tua (kalo heterozigot)
# membantu menentukan genotipe anak

class Father: # konstruktor kelas father
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother: # konstruktor kelas mother
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child: # konstruktor kelas mother
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        # ambil alel dari ayah dan ibu
        father_alel = self.get_allele(self.father.blood_type)
        mother_alel = self.get_allele(self.mother.blood_type)

        # pilih alel secara acak dari ayah dan ibu
        child_alel = random.choice(father_alel) + random.choice(mother_alel)

        # cek golongan darah anak berdasarkan alel
        return self.get_blood_type(child_alel)

    def get_allele(self, blood_type):
        # Mengembalikan alel berdasarkan golongan darah
        if blood_type == 'A':
            return ['A', 'A', 'O']  # AA atau AO
        elif blood_type == 'B':
            return ['B', 'B', 'O']  # BB atau BO
        elif blood_type == 'AB':
            return ['A', 'B']  # AB
        elif blood_type == 'O':
            return ['O', 'O']  # OO
        else:
            raise ValueError("Golongan darah tidak valid")

    def get_blood_type(self, alleles):
        # cek golongan darah berdasarkan kombinasi alel
        if 'A' in alleles and 'B' in alleles:
            return 'AB'
        elif 'A' in alleles:
            return 'A'
        elif 'B' in alleles:
            return 'B'
        else:
            return 'O'

def main():
    print("Program Simulasi Pewarisan Golongan Darah")
    
    father_blood_type = input("Masukkan golongan darah ayah (A, B, AB, O): ")
    father = Father(father_blood_type)

    mother_blood_type = input("Masukkan golongan darah ibu (A, B, AB, O): ")
    mother = Mother(mother_blood_type)

    child = Child(father, mother)
    print(f"Golongan darah anak: {child.blood_type}")

if __name__ == "__main__":
    main()
