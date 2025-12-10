import time

def hitung():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

print("Hello world.")

start = time.time()
hasil = hitung()
end = time.time()

print("Hasil:", hasil)
print("Waktu eksekusi:", end - start, "detik")
