nilai=100
hadir=True
#kode yang bernilai True akan dijalankan
if nilai==100:
 #nested if
 if hadir==True:
  ipk=4.00
elif nilai>=80 and nilai<99:
  if hadir==True:
   ipk=3.90
else:
 ipk=3.80
print(ipk)