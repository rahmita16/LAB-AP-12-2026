tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

if tujuan == "Pantai" and waktu == "Pagi":
    print("Paket Rekomendasi: Paket A")

elif tujuan == "Pegunungan" and waktu == "Pagi" and tipe == "Dewasa":
    print("Paket Rekomendasi: Paket B")

elif tujuan == "Kota" and waktu == "Malam" or waktu == "Malam" and tipe == "Dewasa":
    print("Paket Rekomendasi: Paket C")

else:
    print("Tidak ada paket yang cocok")