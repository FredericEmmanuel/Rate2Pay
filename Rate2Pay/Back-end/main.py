import Login_Signup
import data_acc
import del_acc
import RTP
from Login_Signup import current_user

print("\n=== Rate2Pay ===")
while True:
    punya_acc = input("Apakah anda memiliki akun?(Y/N) ").upper()
    if punya_acc == "Y":
        Login_Signup.login()
        break
    elif punya_acc =="N":
        Login_Signup.signup()
        break
    else:
        print("Pilihan Invalid!")
    
while True:
    print("\n=== Rate2Pay ===")
    print("1. RTP")
    print("2. Data Akun")
    print("3. Delete Akun")
    print("4. Keluar")
    pilihan = int(input("\nApa yang ingin anda lakukan?"))
    if pilihan == 1:
        RTP.RTP(current_user)
    if pilihan == 2:
        data_acc.data_acc(current_user)
    if pilihan == 3:
        del_acc.delete_account(current_user)
    if pilihan == 4:
        print("\nTerimaKasih untuk menggunakan Rate2Pay")
        break
