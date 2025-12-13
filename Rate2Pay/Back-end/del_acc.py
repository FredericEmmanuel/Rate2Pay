import csv

def delete_account(current_user):
    with open("Rate2Pay/Data/user.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if current_user == row["username"]:
                break
    print("\n=== HAPUS AKUN ===")

    konfirmasi = input("Yakin ingin menghapus akun? (y/n): ").lower()
    if konfirmasi != "y":
        print("Dibatalkan.")
        return False

    pwd = input("Masukkan password untuk konfirmasi: ")
    if pwd != db["users"][username]["password"]:
        print("Password salah, batal menghapus.")
        return False

    print("*PERINGATAN* Seluruh data usaha akan dihapus permanen.")
    lanjut = input("Apakah Anda benar-benar yakin? (y/n): ").lower()
    if lanjut != "y":
        print("Penghapusan dibatalkan.")
        return False

    del 
