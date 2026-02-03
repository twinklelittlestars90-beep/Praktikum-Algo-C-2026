# Membuat fungsi hitung
def hitung(a, b):
    # Menghitung penjumlahan
    jumlah = a + b
    
    # Menghitung pengurangan
    kurang = a - b
    
    # Mengembalikan dua hasil sekaligus
    return jumlah, kurang

# Memanggil fungsi
hasil_penjumlahan, hasil_pengurangan = hitung(5, 3)

# Menampilkan hasil
print("Penjumlahan =", hasil_penjumlahan)
print("Pengurangan =", hasil_pengurangan)
