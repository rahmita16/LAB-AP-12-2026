print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
    except ValueError:
        print("Input baris harus berupa angka!")
        print()
        continue

    if baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        print()
        continue

    break

kursi_per_baris = int(input("Masukkan jumlah kursi per baris: "))

print()
print("--- Daftar Kursi Tersedia ---")

for b in range(1, baris + 1):
    for k in range(1, kursi_per_baris + 1):
        # Aturan Mitos: kursi nomor 13 tidak pernah dijual
        if k == 13:
            continue
        # Aturan Baris VVIP: baris 1 hanya kursi ganjil
        if b == 1 and k % 2 == 0:
            continue
        print("Baris", b, "- Kursi", k)