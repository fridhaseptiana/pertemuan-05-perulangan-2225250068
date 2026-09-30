# 01_tabel_perkalian.py
# Program menampilkan tabel perkalian dari 1 sampai 10

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")