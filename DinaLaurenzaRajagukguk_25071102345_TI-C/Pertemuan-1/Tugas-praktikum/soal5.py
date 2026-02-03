#fungsi
#membuat fungsi dengan parameter
def hitung(a,b):
    penjumlahan = a+b
    pengurangan = a-b
    return penjumlahan, pengurangan  
 #mengembalikan hasil penjumlahan dan pengurangan
hasil_tambah, hasil_kurang = hitung(5,3) 
print("pengurangan =", hasil_kurang)