#if_else, digunakan untuk membuat keputusan dalam program.
#Program akan menjalankan kode tertentu jika kondisi benar (True), dan menjalankan kode lain jika salah (False).

#python if
umur = 20
if umur >= 17:
    print("Boleh membuat KTP") # dijalankan jika kondisi True
else:
    print("Belum boleh membuat KTP") # dijalankan jika kondisi False

#if - elif - else, digunakan jika ada lebih dari dua kondisi.
nilai = 85
if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")

#If dalam Satu Baris (Short Hand), bentuk singkat dari if else yang ditulis dalam satu baris.
#Kode lebih ringkas dan Cocok untuk kondisi sederhana
a = 10
b = 5
print("a lebih besar") if a > b else print("b lebih besar")

#Nested If (If di dalam If), if yang berada di dalam if lain.
#Untuk mengecek kondisi berlapis dan Untuk keputusan yang lebih kompleks
x = 10
if x > 0:
    if x % 2 == 0:
        print("Bilangan positif dan genap")
    else:
        print("Bilangan positif dan ganjil")
else:
    print("Bilangan nol atau negatif")

