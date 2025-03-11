# Mohd.Musyaffa Alief Athallah
# 123140184
# Praktikum PBO RA

# Definisikan kelas Robot yang akan menjadi kelas induk untuk semua jenis robot
class Robot:
    # Inisialisasi atribut-atribut robot seperti nama, serangan, dan HP
    def __init__(self, name, attack, hp):
        self.__name = name  # Nama robot
        self.__attack = attack  # Nilai serangan robot
        self.__hp = hp  # HP (Health Points) robot
        self.__max_hp = hp  # Nilai maksimum HP robot

    # Metode untuk robot menyerang musuh
    def serang_musuh(self, enemy):
        enemy.terima_damage(self.__attack)  # Musuh menerima damage sebesar serangan robot
        print(f"{self.__name} menyerang {enemy.get_name()} dan mengurangi HP sebanyak {self.__attack}!")  # Cetak pesan serangan

    # Metode untuk robot menerima damage
    def terima_damage(self, damage):
        self.__hp -= damage  # Kurangi HP robot sebesar damage yang diterima
        if self.__hp < 0:  # Jika HP robot kurang dari 0
            self.__hp = 0  # Set HP robot menjadi 0
        print(f"{self.__name} terkena serangan dan HP sekarang {self.__hp}.")  # Cetak pesan damage

    # Metode untuk robot memulihkan HP
    def pulih_darah(self):
        regen_HP = int(self.__max_hp * 0.1)  # Hitung jumlah HP yang akan dipulihkan (10% dari HP maksimum)
        self.__hp += regen_HP  # Tambahkan HP robot dengan jumlah yang dipulihkan
        if self.__hp > self.__max_hp:  # Jika HP robot melebihi HP maksimum
            self.__hp = self.__max_hp  # Set HP robot menjadi HP maksimum
        print(f"{self.__name} memulihkan HP sebanyak {regen_HP} dan HP sekarang {self.__hp}.")  # Cetak pesan pemulihan HP

    # Metode untuk memeriksa apakah robot masih hidup
    def is_alive(self):
        return self.__hp > 0  # Kembalikan True jika HP robot lebih dari 0, False jika tidak

    # Metode untuk mendapatkan nama robot
    def get_name(self):
        return self.__name  # Kembalikan nama robot

# Definisikan kelas MeleeRobot yang mewarisi dari kelas Robot
class MeleeRobot(Robot):
    # Inisialisasi atribut-atribut MeleeRobot
    def __init__(self, name, attack, hp):
        super().__init__(name, attack, hp)  # Panggil konstruktor kelas induk (Robot)

# Definisikan kelas RangedRobot yang mewarisi dari kelas Robot
class RangedRobot(Robot):
    # Inisialisasi atribut-atribut RangedRobot
    def __init__(self, name, attack, hp):
        super().__init__(name, attack, hp)  # Panggil konstruktor kelas induk (Robot)

# Definisikan kelas Game yang mengatur mekanisme permainan
class Game:
    # Inisialisasi atribut-atribut game seperti robot yang bermain dan nomor ronde
    def __init__(self, robot1, robot2):
        self.robot1 = robot1  # Robot pertama
        self.robot2 = robot2  # Robot kedua
        self.round = 1  # Nomor ronde awal

    # Metode untuk memainkan satu ronde permainan
    def play_round(self):
        print(f"\nRound {self.round}:")  # Cetak nomor ronde

        # Minta input aksi dari robot pertama
        aksi = input(f"{self.robot1.get_name()}, pilih aksi (1: Serang, 2: Pulihkan, 3: Menyerah): ")

        # Periksa aksi yang dipilih dan lakukan aksi tersebut
        if aksi == '1':
            self.robot1.serang_musuh(self.robot2)  # Robot pertama menyerang robot kedua
        elif aksi == '2':
            self.robot1.pulihkan_darah()  # Robot pertama memulihkan HP
        elif aksi == '3':
            print(f"{self.robot1.get_name()} menyerah!")  # Robot pertama menyerah
            return False  # Kembalikan False untuk mengakhiri permainan
        else:
            print("Aksi tidak valid!")  # Jika aksi tidak valid, cetak pesan kesalahan
            return True  # Kembalikan True untuk melanjutkan permainan

        # Periksa apakah robot kedua masih hidup
        if not self.robot2.is_alive():
            print(f"{self.robot1.get_name()} menang!")  # Jika tidak, robot pertama menang
            return False  # Kembalikan False untuk mengakhiri permainan

        # Robot kedua menyerang robot pertama
        self.robot2.serang_musuh(self.robot1)

        # Periksa apakah robot pertama masih hidup
        if not self.robot1.is_alive():
            print(f"{self.robot2.get_name()} menang!")  # Jika tidak, robot kedua menang
            return False  # Kembalikan False untuk mengakhiri permainan

        # Kedua robot memulihkan HP
        self.robot1.pulih_darah()
        self.robot2.pulih_darah()

        self.round += 1  # Tambahkan nomor ronde
        return True  # Kembalikan True untuk melanjutkan permainan

    # Metode untuk memulai permainan
    def start(self):
        print("Pertarungan dimulai!")  # Cetak pesan mulai permainan
        while True:  # Ulangi selama permainan belum selesai
            if not self.play_round():  # Jika play_round mengembalikan False
                break  # Hentikan permainan

# Jika file ini dijalankan sebagai program utama
if __name__ == "__main__":
    Atreus = MeleeRobot("Atreus", 20, 100)  # Buat robot melee dengan nama Atreus, serangan 20, dan HP 100
    Daedalus = RangedRobot("Daedalus", 25, 90)  # Buat robot ranged dengan nama Daedalus, serangan 25, dan HP 90

    game = Game(Atreus, Daedalus)  # Buat objek game dengan Atreus dan Daedalus sebagai lawan
    game.start()  # Mulai permainan
