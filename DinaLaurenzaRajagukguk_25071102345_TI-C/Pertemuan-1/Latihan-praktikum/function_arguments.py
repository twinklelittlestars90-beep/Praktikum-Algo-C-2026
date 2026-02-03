#function arguments, Arguments (argumen) adalah nilai yang kita kirim ke dalam fungsi saat fungsi dipanggil.
#Argumen dipakai agar fungsi bisa bekerja dengan data yang berbeda-beda.

#contoh functions
def sapa(nama):
    print("Halo,", nama)

sapa("Dina")

#Positional Arguments, nilai dikirim sesuai urutan parameter.
def tambah(a, b):
    print(a + b)

tambah(3, 5)

#Keyword Arguments, mengirim nilai dengan menyebut nama parameter.
def biodata(nama, umur):
    print(nama, umur)

biodata(umur=20, nama="Dina")

#Default Arguments, Parameter punya nilai default jika tidak diisi.
def sapa(nama="Teman"):
    print("Halo,", nama)

sapa()
sapa("Dina")

#Arbitrary Arguments (*args), Jika jumlah argumen tidak pasti.
def jumlah(*angka):
    total = 0
    for x in angka:
        total += x
    print(total)

jumlah(1, 2, 3, 4)

#Arbitrary Keyword Arguments (**kwargs), Mengirim banyak argumen dalam bentuk key=value.
def data(**info):
    for k, v in info.items():
        print(k, ":", v)

data(nama="Dina", umur=20, kota="Pekanbaru")
