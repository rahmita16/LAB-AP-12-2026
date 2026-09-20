jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ")

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

layanan = 15000 if express == "ya" else 0
tarif = tarif + layanan

print("Total tarif pengiriman: Rp" , tarif)