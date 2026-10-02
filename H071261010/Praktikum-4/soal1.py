def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 0.9
    return subtotal


print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ").strip().lower()
adalah_member = (status == "y")

total = 0

while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)
    total += subtotal
    print(f"Subtotal {nama}: Rp{int(subtotal)}")

print(f"Total belanja: Rp{int(total)}")