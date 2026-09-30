while True:
    try:
        n = int(input("Masukkan maksimal kursi bus: "))
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()

sisa = n
total = 0

while sisa > 0:
    print("Sisa kursi: sisa")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        print()
        continue

    if umur < 0:
        print("Umur tidak valid!")
        print()
        continue

    if umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")
    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: (Rp 50.000)")
    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: (Rp 100.000)")

    total += harga
    sisa -= 1
    print()

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total)