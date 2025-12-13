# ================================
#  MODULE: Rate Tarif Price (RTP)
# ================================

def GetExchangeRate(currency):
    kurs = {
        "IDR": 1,
        "CNY": 2300,
        "JPY": 110
    }
    return kurs.get(currency, 1)

def SaveRTPResult(user, data):
   print(f"[DEBUG] Data RTP untuk user {user}")

def GetUsahaData(user):
    #Dummy data.
    #Nanti tolong tambahin di sistemnya, ambil dari database
    return {
        "biaya_operasional": 500000,
        "beban_pajak": 100000,
        "target_laba": 300000
    }

def RTP(current_user):

    print("\n=== menu rate tarif price (rtp) ===")

    jumlah_barang = int(input("Masukkan jumlah barang: "))
    barang_list = []

    for i in range(1, jumlah_barang + 1):
        print(f"\nBarang ke-{i}:")
        nama_barang = input("Nama barang: ")
        harga_beli = float(input("Harga distribusi: "))

        mata_uang = input("Pilih mata uang (IDR/CNY/JPY): ").upper()

        # konversi default RTP
        if mata_uang == "CNY":
            rtp_low, rtp_mid, rtp_high = 2000, 3000, 4000
        elif mata_uang == "JPY":
            rtp_low, rtp_mid, rtp_high = 100, 150, 200
        else:
            rtp_low, rtp_mid, rtp_high = 1, 1, 1

        # konvesi harga beli ke rupiah
        kurs = GetExchangeRate(mata_uang)
        harga_beli_idr = harga_beli * kurs

        barang_list.append({
            "nama": nama_barang,
            "harga_beli": harga_beli,
            "harga_beli_idr": harga_beli_idr,
            "rtp_low": rtp_low,
            "rtp_mid": rtp_mid,
            "rtp_high": rtp_high
        })

    #sertakan pajak?
    include_pajak = input("Sertakan pajak? (Y/N): ").upper()
    pajak = 0.1 if include_pajak == "Y" else 0

    usaha_data = GetUsahaData(current_user)

    print("\n=== HASIL PERHITUNGAN RTP ===")

    for barang in barang_list:
        print(f"\nBarang: {barang['nama']}")

        #perhitungan RTP
        harga_rtp_low = barang["harga beli"] * barang["rtp_low"]
        harga_rtp_mid = barang["harga beli"] * barang["rtp_mid"]
        harga_rtp_high = barang["harga beli"] * barang["rtp_high"]

        #tambah pajak jika ada
        harga_final_low = harga_rtp_low * (1 + pajak)
        harga_final_mid = harga_rtp_mid * (1 + pajak)
        harga_final_high = harga_rtp_high * (1 + pajak)

        # laba bersih
        laba_kotor = harga_final_mid - barang["harga_beli_idr"]
        laba_operasional = laba_kotor - usaha_data["biaya_operasional"]
        laba_bersih = laba_operasional - usaha_data["beban_pajak"]

        print(f"Harga Beli (IDR): {barang['harga_beli_idr']}")
        print(f"RTP Rendah (Final): {harga_final_low}")
        print(f"RTP Rekomendasi (Final): {harga_final_mid}")
        print(f"RTP Tinggi (Final): {harga_final_high}")
        print(f"Laba Bersih Estimasi: {laba_bersih}")

        if laba_bersih >= usaha_data["target_laba"]:
            print("✅ Target laba tercapai.")
        else:
            print("❌ Target laba belum tercapai.")

    print("\nSelesai menghitung RTP.")
    print("1. Kembali ke Menu Utama")
    print("2. Ulangi RTP")

    pilihan = int(input("Pilih: "))

    if pilihan == 2:
        simpan = input("Simpan data sebelumnya? (Y/N): ").upper()
        if simpan == "Y":
            SaveRTPResult(current_user, barang_list)

        return RTP(current_user)  # Rekursi sesuai pseudocode

    else:
        print("Kembali ke Main Menu...")
        return




