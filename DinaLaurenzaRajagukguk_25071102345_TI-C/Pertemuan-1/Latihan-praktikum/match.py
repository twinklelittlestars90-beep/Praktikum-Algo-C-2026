#match, fitur Python (mulai Python 3.10) yang digunakan untuk mencocokkan nilai dengan pola tertentu, mirip switch-case di bahasa lain.
#digunakan saat Banyak pilihan kondisi dan Lebih rapi daripada banyak elif

#default value
hari = 2

match hari:
    case 1:
        print("senin") # kode jika cocok dengan nilai1
    case 2:
        print("selasa") # kode jika cocok dengan nilai2
    case _:
        print("hari tidak valid") # default (jika tidak cocok semua)

#combine value
warna = "merah"

match warna:
    case "merah":
        print("Warna merah dipilih")
    case "biru":
        print("Warna biru dipilih")
    case "hijau":
        print("Warna hijau dipilih")
    case _:
        print("Warna tidak dikenal")


