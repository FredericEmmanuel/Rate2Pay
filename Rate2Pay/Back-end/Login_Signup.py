import csv

current_user = None
user_input = None
pw_input = None

def login():
    global current_user
    global make_acc
    login_berhasil = False
    while login_berhasil == False:
        make_acc = None
        print("\n=== FORM LOGIN ===")
        with open("Rate2Pay/Data/user.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            user_input = input("Username: ")
            pw_input = input("Password: ")
            for row in reader:
                if user_input == row["username"] and pw_input == row["password"]:
                    current_user = row["username"]
                    login_berhasil = True
                    print(f"Login Berhasil!, Selamat Datang {current_user}")
                    break
            if not login_berhasil:
                while True:
                    make_acc = input("Username atau Password salah, Apakah anda ingin membuat akun baru(Y/N)? ").upper()
                    if make_acc == "Y":
                        signup()
                        break
                    elif make_acc == "N":
                        break


def signup():
    password = True
    conf = False
    print("\n=== FORM REGISTRASI ===")
    while True:
        username = input("Username baru: ")
        with open("Rate2Pay/Data/user.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    print("Username sudah digunakan.")
                    break
            else:
                break
        
    while password != conf:
        password = input("Password: ")
        conf = input("Konfirmasi Password: ")
        if password != conf:
            print("Password Dan Konfirmasi Berbeda, Coba Ulang!")

    while True:
        nama_usaha = input("Nama Usaha              :")
        if nama_usaha.strip() == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        jenis_usaha = input("Jenis Usaha             :")
        if jenis_usaha.strip() == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        biaya_operasional = int(input("Biaya Operasi           :"))
        if biaya_operasional == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:        
        pengeluaran_min = int(input("Pengeluaran (min)       :"))
        if pengeluaran_min == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        pengeluaran_max = int(input("pengeluaran (max)       :"))
        if pengeluaran_max == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        target_laba = int(input("Target Laba Bersih      :"))
        if target_laba == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        estimasi_pengeluaran = int(input("Estimasi Pengeluaran    :"))
        if estimasi_pengeluaran == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        estimasi_pendapatan = int(input("Estimasi Pendapatan     :"))
        if estimasi_pendapatan == "":
            print("Tidak boleh kosong.")
        else:
            break
    while True:
        estimasi_laba = int(input("Estimasi Laba Bersih    :"))
        if estimasi_laba == "":
            print("Tidak boleh kosong.")
        else:
            break   

    with open("Rate2Pay/Data/user.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writerow({
            "username": username,
            "password": password,
            "nama_usaha": nama_usaha,
            "jenis_usaha": jenis_usaha,
            "biaya_operasional": biaya_operasional,
            "pengeluaran_min": pengeluaran_min,
            "pengeluaran_max": pengeluaran_max,
            "target_laba": target_laba,
            "estimasi_pengeluaran": estimasi_pengeluaran,
            "estimasi_pendapatan": estimasi_pendapatan,
            "estimasi_laba": estimasi_laba
        })

    print("Signup berhasil!")
