#while loop digunakan untuk mengulang blok kode selama kondisi bernilai True.Jika kondisi menjadi False, loop berhenti.

#while kondisi:
# kode yang diulang
i = 1

while i <= 5: #kode akan diulang
    print(i)
    i += 1

#while dengan break, Menghentikan loop sebelum kondisi False.
i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

#while dengan continue, Melewati satu iterasi.
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#while dengan else, Blok else dijalankan jika loop selesai tanpa break.
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop selesai")
