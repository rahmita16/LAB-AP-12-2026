print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")
print()

while True:
    masukan = input("Masukkan jumlah item: ")

    try:
        jumlah = int(masukan)
    except ValueError:
        print("Input harus berupa angka!")
        print()
        continue

    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break

    if jumlah < 0:
        print("Jumlah tidak boleh negatif")
        print()
        continue

    if jumlah > 100:
        print("Maksimal 100 item per transaksi!")
        print()
        continue

    print("Transaksi", jumlah, "item berhasil!")
    print()