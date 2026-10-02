def rekap_nilai(*args):
    if len(args) == 0:
        return None
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah


nilai_list = []

while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    nilai = float(masukan)
    # Tampilkan sebagai int jika bilangan bulat (agar sesuai contoh: 90, bukan 90.0)
    if nilai == int(nilai):
        nilai = int(nilai)
    nilai_list.append(nilai)

hasil = rekap_nilai(*nilai_list)

if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {float(rata_rata)}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")