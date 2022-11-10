# Memuat built-in libraries yang akan digunakan
from os import getpid
from time import time, sleep
from multiprocessing import Pool, Process

# Input bilangan dan inisialisasi function
a = int(input("Input Bilangan: "))

def cetak(x):
    bil = x % 2
    if bil == 0:
       print(x, "Genap - ID proses", getpid())
    else:
       print(x, "Ganjil - ID proses", getpid())
    sleep(1)

# Sekuensial
print("\nSekuensial")
sekuensial_awal = time()

for x in range(1, a + 1):
    cetak(x)

sekuensial_akhir = time()

# Multiprocessing Process
print("\nMultiprocessing.Process")
kumpulan_process = []
process_awal = time()

for x in range(1, a + 1):
    p = Process(target=cetak, args=(x,))
    kumpulan_process.append(p)
    p.start()

for x in kumpulan_process:
    p.join()

process_akhir = time()

# Multiprocessing Pool
print("\nMultiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(1, a + 1))
pool.close()

pool_akhir = time()

# Waktu Eksekusi
print("Waktu eksekusi sekuensial 		: ", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.process 	: ", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.pool	: ", pool_akhir - pool_awal, "detik")
