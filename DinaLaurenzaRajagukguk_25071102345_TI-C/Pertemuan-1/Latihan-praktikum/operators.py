#Operator, simbol yang digunakan untuk melakukan operasi pada variabel dan nilai.
#Contoh: +, -, *, ==, and, dll.

#arithmetic operators
a = 10
b = 3
print(a + b)   # tambah
print(a - b)   # kurang
print(a * b)   # kali
print(a / b)   # bagi
print(a % b)   # sisa bagi
print(a ** b)  # pangkat
print(a // b)  # bagi bulat

#assignment operators (penugasan)
x = 5
x += 3
print(x)
x *= 2
print(x)
# "="	x = 5	x = 5	               
# "+="	x += 3	x = x + 3	
# "-="	x -= 3	x = x - 3	
# "*="	x *= 3	x = x * 3	
# "/="	x /= 3	x = x / 3	
# "%="	x %= 3	x = x % 3	
# "//="	x //= 3	x = x // 3	
# "**="	x **= 3	x = x ** 3	
# "&="	x &= 3	x = x & 3	
# "|="	x |= 3	x = x | 3	
# "^="	x ^= 3	x = x ^ 3	
# ">>="	x >>= 3	x = x >> 3	
# "<<="	x <<= 3	x = x << 3	
# ":="	print(x := 3)	x = 3 print(x)

#Comparison Operators (Perbandingan)
x = 10
y = 5
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical Operators (Logika)
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Identity Operators, Digunakan untuk mengecek apakah dua variabel objek yang sama.
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)      # True
print(x is z)      # False
print(x is not z)  # True

#Membership Operators, Mengecek apakah nilai ada di dalam data.
buah = ["apel", "jeruk", "mangga"]
print("apel" in buah)
print("pisang" not in buah)

#Bitwise Operators, operator yang bekerja langsung pada representasi biner (bit 0 dan 1) dari bilangan bulat.
a = 5   # 0101
b = 3   # 0011
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)



