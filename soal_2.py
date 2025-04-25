def show_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def show_taks(list_taks):
    print("\n--- Daftar Tugas ---")
    if not list_taks:
        print("Tidak ada tugas dalam daftar.")
    else:
        for i, tugas in enumerate(list_taks):
            print(f"{i + 1}. {tugas}")
    print("--------------------")

def add_taks(list_taks):
    new_taks = input("Masukkan tugas yang ingin ditambahkan: ").strip() 
    
    if new_taks:
        list_taks.append(new_taks)
        print("Tugas berhasil ditambahkan!")
    else:
        print("Error: Deskripsi tugas tidak boleh kosong.")

def hapus_tugas(list_taks):
    show_taks(list_taks)
    
    if not list_taks:
        return

    try:
        nomor_tugas = input("Masukkan nomor tugas yang ingin dihapus: ")
        if not nomor_tugas.strip():
             print("Error: Nomor tugas tidak boleh kosong.")
             return

        nomor_hapus = int(nomor_tugas)

        indeks_hapus = nomor_hapus - 1

        if 0 <= indeks_hapus < len(list_taks):
            tugas_yang_dihapus = list_taks.pop(indeks_hapus)
            print(f"Tugas '{tugas_yang_dihapus}' berhasil dihapus.")
        else:
            print(f"Error: Tugas dengan nomor {nomor_hapus} tidak ditemukan.")

    except ValueError:
        print("Error: Input harus berupa nomor.")

list_tugas = []

while True:
    show_menu()
    pilihan_user = input("Masukkan pilihan (1/2/3/4): ")

    try:
        if not pilihan_user.strip():
            print("Error: Pilihan tidak boleh kosong.")
            continue

        pilihan = int(pilihan_user)

        if pilihan == 1:
            add_taks(list_tugas)
        elif pilihan == 2:
            hapus_tugas(list_tugas)
        elif pilihan == 3:
            show_taks(list_tugas)
        elif pilihan == 4:
            print("Keluar dari program.")
            break 
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 4.")

    except ValueError:
        print("Error: Input tidak valid. Harap masukkan angka (1/2/3/4).")