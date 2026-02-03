#VARIABLES, digunakan untuk menyimpan data atau nilai

#python variables, contohnya
a = 4
b = "dina"
print (a)
print (b)
x = str(3)    # x sama dengan "3" karena string
y = int(3)    # y sama dengan 3 karena integer (bilangan bulat)
z = float(3)  # z sama dengan 3.0 karena float (bilangan desimal atau pecahan)

#variables name
myname = "dina" #nama variabel bisa menggunakan huruf kecil semua
my_name = "dina" #nama variabel bisa menggunakan tanda "_" untuk memisahkan agar mudah dibaca (snake case)
_my_name = "dina" #nama variabel bisa menggunakan tanda diawal nama variabel dan bukan angka atau bilangan
myName = "dina" #nama variabel bisa menggunakan huruf kecil di depan (camel case)
MyName = "dina" #nama variabel bisa menggunakan huruf besar di depan (pascal case)
MYNAME = "dina" #nama variabel bisa menggunakan huruf besar semua
myname2 = "dina"#nama variabel bisa menggunakan angka atau bilangan dengan syarat tidak di awal nama variabel

#assign multiple values, Memberikan beberapa nilai ke beberapa variabel sekaligus dalam satu baris kode.
#Dengan kata lain, kita bisa mengisi banyak variabel dalam satu perintah.
a ,b ,c = "cokelat" ,"soto" ,"ice cream"
print(a)
print(b)
print(c)
a=b=c="makanan favorit"
print(a)
print(b)
print(c)
makanan_favorit=["cokelat", "soto", "ice cream"]
a, b, c =makanan_favorit
print(a)
print(b)
print(c)

#output variables, keluaran atau nilai dari variabel yang kita buat. misalnya contoh berikut akan mengeluarkan nilai 4.
a=4
print(a)

#Global variable, variabel yang dibuat di luar fungsi, sehingga bisa digunakan di seluruh bagian program.
x = 10   # ini global variable

def tampil():
    print(x)

tampil()

