import csv

USER_FILE = "Rate2Pay/Data/user.csv"

def delete_account(current_user):
    users = []
    user_found = False
    stored_password = None

    # ===============================
    # BACA DATA USER
    # ===============================
    with open(USER_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == current_user:
                user_found = True
                stored_password = row["password"]
            else:
                users.append(row)

    if not user_found:
        print("User tidak ditemukan.")
        return False

    print("\n=== HAPUS AKUN ===")

    # ===============================
    # KONFIRMASI AWAL
    # ===============================
    konfirmasi = input("Yakin ingin menghapus akun? (y/n): ").lower()
    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return False

    # ===============================
    # KONFIRMASI PASSWORD
    # ===============================
    pwd = input("Masukkan password akun: ")
    if pwd != stored_password:
        print("Password salah, penghapusan dibatalkan.")
        return False

    # ===============================
    # PERINGATAN AKHIR
    # ===============================
    print(
        "\n PERINGATAN \n"
        "Segala kehilangan data usaha dan data pribadi\n"
        "bukan menjadi tanggung jawab kami setelah Anda\n"
        "melanjutkan proses ini."
    )

    lanjut = input("Apakah Anda BENAR-BENAR yakin? (y/n): ").lower()
    if lanjut != "y":
        print("Penghapusan dibatalkan.")
        return False

    # ===============================
    # TULIS ULANG CSV TANPA USER
    # ===============================
    with open(USER_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = users[0].keys() if users else ["username", "password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

    print("Akun berhasil dihapus.")
    return True
