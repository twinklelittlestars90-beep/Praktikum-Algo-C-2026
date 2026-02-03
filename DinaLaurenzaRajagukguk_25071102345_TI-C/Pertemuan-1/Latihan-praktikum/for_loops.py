#for loop digunakan untuk mengulang elemen dalam suatu urutan (sequence) seperti list, tuple, string, atau range().
#for variabel in iterable:
# kode yang diulang

#For dengan range()
for i in range(5):
    print(i)

#For pada List
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

#For pada String
for huruf in "Python":
    print(huruf)

#For dengan break dan continue
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

#For dengan else
for i in range(3):
    print(i)
else:
    print("Loop selesai")


