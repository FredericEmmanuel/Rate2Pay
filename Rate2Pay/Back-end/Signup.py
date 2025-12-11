users = {}
business_data = {}

def signup():
    print("=== FORM REGISTRASI ===")

    while True:
        username = input("Masukkan username: ").strip()
        if username in users:
            print("Username sudah digunakan, silakan pilih yang lain")
        else:
            break

    while True:
        password = input("Masukkan password: ")
        conf = input("Konfirmasi password: ")
        if password != conf:
            print("Password salah, coba lagi")
        else:
            break

    nama_usaha = input("Masukkan nama usaha: ")
    jenis_usaha = input("Masukkan jenis usaha: ")

    while True:
        toko = input("Apakah memiliki toko fisik? (y/n): ").lower()
        if toko not in ["y", "n"]:
            print("Input tidak valid")
        else:
            break

    if toko == "y":
        biaya_sewa = float(input("Masukkan biaya sewa: "))
        biaya_listrik = float(input("Masukkan biaya listrik: "))
        total_pengeluaran = biaya_sewa + biaya_listrik
    else:
        min_pengeluaran = float(input("Masukkan rata-rata pengeluaran minimum: "))
        max_pengeluaran = float(input("Masukkan rata-rata pengeluaran maksimum: "))
        total_pengeluaran = (min_pengeluaran + max_pengeluaran) / 2

    target_laba = float(input("Masukkan target laba bersih: "))

    estimasi_pendapatan = total_pengeluaran + target_laba
    estimasi_laba_bersih = estimasi_pendapatan - total_pengeluaran

    users[username] = password
    business_data[username] = {
        "Nama usaha": nama_usaha,
        "Jenis usaha": jenis_usaha,
        "Toko fisik": toko == "y",
        "Total pengeluaran": total_pengeluaran,
        "Target laba": target_laba,
        "Estimasi pendapatan": estimasi_pendapatan,
        "Estimasi laba bersih": estimasi_laba_bersih
    }

    print("Registrasi berhasil! Silakan login untuk melanjutkan")

def login():
    print("=== FORM LOGIN ===")

    while True:
        username = input("Username: ")

        if username not in users:
            print("Username tidak ditemukan")
            pilihan = input("Apakah Anda ingin membuat akun? (y/n): ").lower()
            if pilihan == "y":
                signup()
            else:
                print("Kembali ke menu login")
            continue

        while True:
            password = input("Password: ")
            if users[username] == password:
                print("Login berhasil")
                return username
            else:
                print("Password salah, coba ulang")

def main():
    print("=== SISTEM LOGIN & REGISTRASI USAHA ===")
    
    while True:
        print("1. Signup")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            signup()
        elif pilihan == "2":
            user = login()
            print(f"Selamat datang, {user}.")
            print("Data usaha Anda:")
            for k, v in business_data[user].items():
                print(f"- {k}: {v}")
        elif pilihan == "3":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid")

main()
