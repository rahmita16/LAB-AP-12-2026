def format_set(s):
    
    return "{" + ", ".join(repr(x) for x in sorted(s)) + "}"


def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pemilih in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak ada dalam daftar! Suara tidak dicatat.")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara '{nama_pemilih.capitalize()}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in sorted(kandidat_set)}
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    for kandidat, jumlah in perolehan.items():
        print(f"  {kandidat}: {jumlah} suara")

    total = sum(perolehan.values())
    print()
    print(f"Total suara masuk: {total}")

    suara_tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == suara_tertinggi]

    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    print("=" * 40)


def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print("  SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)
    print()

    # Fase pendaftaran
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)

    print()
    print(f"Kandidat terdaftar: {format_set(kandidat_set)}")
    print()

    # Fase pemungutan suara
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        print()
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {format_set(kandidat_set)}")
        pilihan = input("Pilih kandidat: ").strip()
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    print()
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)


main()