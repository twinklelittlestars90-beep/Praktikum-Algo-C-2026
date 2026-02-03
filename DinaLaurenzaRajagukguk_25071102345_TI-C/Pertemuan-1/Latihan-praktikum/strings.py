#string, tipe data untuk menyimpan teks atau kumpulan karakter.
#Ditulis dengan tanda petik satu ' ' atau dua " ".
teks = "Halo semuanya, have a good day"
print(teks)
print(type(teks))

#slicing, digunakan untuk mengambil sebagian isi string.
teks = "PythonProgramming"
print(teks[0:6])     # Python
print(teks[6:])      # Programming
print(teks[-11:-1])  # Programmin
#modify string (mengubah string), Karena string immutable, kita tidak mengubah langsung, tapi membuat string baru.
kalimat = "belajar python"
print(kalimat.upper())       # BELAJAR PYTHON (huruf besar)
print(kalimat.lower())       # belajar python (huruf kecil)
print(kalimat.replace("python", "coding"))
#concatenate, menggabungkan string
a = "Halo"
b = "Dina"
gabung = a + " " + b
print(gabung)
#format
nama = "Dina"
umur = 20
print("Nama saya {}, umur saya {}".format(nama, umur))
#escape characters, Digunakan untuk menulis karakter khusus dalam string.
print("Dia berkata: \"Python itu keren!\"")
print("Baris pertama\nBaris kedua")
print("Tab\tspasi")
print("Backslash: \\")
#string methods, method bawaan
teks = " Belajar Python Itu Seru "
print(teks.strip())        # hapus spasi depan & belakang
print(teks.split())        # pecah jadi list
print(teks.find("Python")) # cari posisi
print(teks.count("u"))     # hitung huruf
print(teks.startswith(" "))
print(teks.endswith(" "))






