#Data Types, (tipe data) adalah jenis nilai yang disimpan dalam sebuah variabel.
x = 10        # int (angka bulat)
y = 3.14      # float (desimal)
z = "Halo"    # str (teks)

#Numeric Types (Angka)
x = 10
print(x, type(x))     # int (angka bulat)
y = 3.14
print(y, type(y))     # float (desimal)
z = 2 + 3j
print(z, type(z))     #complex (bilangan kompleks)

#Text Type:	str
nama = "Dina"
print(nama, type(nama))

#Sequence Types:list, tuple, range
hewan=["anjing", "kucing", "kambing" ] #list, bisa diubah (mutable)
print (hewan, type(hewan))
x=(1,2,3) #tuple, tidak bisa diubah (immutable)
print (x, type(x))
range(5) #range, deret angka
print (range(5), type (range(5)))

#Mapping Type:	dict
data = {"nama": "Dina", "umur": 20}
print(data, type(data)) #dict, Data pasangan key:value

#Set Types:	set, frozenset
#set, tidak berurutan (unik)
himpunan = {1, 2, 3, 3}
print(himpunan, type(himpunan))
#frozenset, set yang tidak bisa diubah
fs = frozenset([1, 2, 3])
print(fs, type(fs))

#Boolean Type:	bool
a = True
b = False
print(a, type(a))
print(b, type(b))

#Binary Types:	bytes, bytearray, memoryview
#tipe data Python untuk menyimpan data dalam bentuk biner (0 dan 1).
#bytes, Data biner, immutable (tidak bisa diubah)
b = bytes([65, 66, 67])
print(b)
print(type(b))
#bytearray, Data biner, mutable (bisa diubah)
ba = bytearray([65, 66, 67])
ba[0] = 90
print(ba)
print(type(ba))
#memoryview, Akses langsung ke data biner tanpa menyalin
b = bytes([1, 2, 3, 4])
mv = memoryview(b)

print(mv[0])
print(type(mv))

#None Type:	NoneType
x = None
print(x, type(x))

