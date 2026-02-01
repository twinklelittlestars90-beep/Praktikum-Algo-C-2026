# LOOP MENAMPILKAN BILANGAN DAN JUMLAHNY SEBANYAK N KALI

n = int(input('Banyak angka: '))

for x in range(1, n+1):
    print(x)

jumlah = 0
for x in range(1, n+1):
    jumlah = jumlah + x
print(f'Jumlah = {jumlah}')
