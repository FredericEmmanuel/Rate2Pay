database = {
    "andi": "12345",
    "budi": "password"
}

def signup():
    print("\n=== Registrasi Akun Baru ===")
    while True:
        new_username = input("Masukkan username baru: ")
        if new_username in database:
            print("Username sudah digunakan, coba username lain.")
        else:
            break
    
    new_password = input("Masukkan password baru: ")
    database[new_username] = new_password
    print("Akun berhasil dibuat. Silakan login kembali.\n")


def login():
    while True:
        print("\n=== Form Login ===")
        username = input("Username: ")

        if username not in database:
            print("Username tidak ditemukan.")
            pilihan = input("Apakah Anda ingin membuat akun? (y/n): ").lower()

            if pilihan == "y":
                signup()
                continue
            else:
                print("Kembali ke form login.")
                continue
        else:
            while True:
                password = input("Password: ")
                if database[username] == password:
                    print("Login berhasil. Program selesai.")
                    return
                else:
                    print("Password salah, coba ulang.\n")

login()
