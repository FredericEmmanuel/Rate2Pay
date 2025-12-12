database = {
    "andi": "12345",
    "budi": "password"
}

current_user = None

def login(username, password):
    global current_user

if username not in database:
    return False, "Username tidak ditemukan"

if database[username] == password:
    current_user = username
    return True, f"Login berhasil sebagai {username}"
else:
    return False, "Password salah"
