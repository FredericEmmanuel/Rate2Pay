import csv

def data_acc(current_user):
    with open("Rate2Pay/Data/user.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if current_user == row["username"]:
                break
        
    print("\n=== DATA USAHA ANDA ===")
    print("Nama Usaha              :", row["nama_usaha"])
    print("Jenis Usaha             :", row["jenis_usaha"])
    print("Biaya Operasional       :", row["biaya_operasional"])
    print("Pengeluaran (min–max)   :", row["pengeluaran_min"], "-", row["pengeluaran_max"])
    print("Target Laba Bersih      :", row["target_laba"])
    print("Estimasi Pengeluaran    :", row["estimasi_pengeluaran"])
    print("Estimasi Pendapatan     :", row["estimasi_pendapatan"])
    print("Estimasi Laba Bersih    :", row["estimasi_laba"])

def data_change(current_user):
    with open("Rate2Pay/Data/user.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = reader.fieldnames

    for row in rows:
        if row["username"] == current_user:
            while True:
                pass_conf = input("Silahkan input password untuk menggganti data: ")
                if pass_conf == row["password"]:
                    break
                else:
                    print("Password salah, coba ulang")
            row["nama_usaha"] = input("Nama Usaha              :" )
            row["jenis_usaha"] = input("Jenis Usaha             :" )
            row["biaya_operasional"] = int(input("Biaya Operasional       :"))
            row["pengeluaran_min"] = int(input("Pengeluaran (min)       :" ))
            row["pengeluaran_max"] = int(input("pengeluaran (max)       :" ))
            row["target_laba"] = int(input("Target Laba Bersih      :"))
            row["estimasi_pengeluaran"] = int(input("Estimasi Pengeluaran    :" ))
            row["estimasi_pendapatan"] = int(input("Estimasi Pendapatan     :" ))
            row["estimasi_laba"] = int(input("Estimasi Laba Bersih    :" ))
            break

    with open("Rate2Pay/Data/user.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Data usaha berhasil diubah.")
    data_acc(current_user)
