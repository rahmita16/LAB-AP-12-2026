GENRE_VALID = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]


def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}"


def format_genre_set(genre_set, playlist):
    # urutan sesuai kemunculan pertama di playlist
    urut = []
    for lagu in playlist:
        if lagu[2] in genre_set and lagu[2] not in urut:
            urut.append(lagu[2])
    return "{" + ", ".join(repr(g) for g in urut) + "}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
    print("=" * 55)
    print(f" {'No':>2}  {'Judul':<18}  {'Artis':<13}  {'Genre':<8}  Durasi")
    print("=" * 55)
    total = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, 1):
        print(f" {i:>2}  {judul:<18}  {artis:<13}  {genre:<8}  {format_durasi(durasi)}")
        total += durasi
    print("=" * 55)
    print(f" Total durasi playlist: {total // 60} menit {total % 60} detik")


def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
        return True
    print("Nomor lagu tidak valid!")
    return False


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print("  STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    if not playlist:
        print("  Playlist masih kosong.")
        print("=" * 40)
        return

    distribusi = {}
    for lagu in playlist:
        distribusi[lagu[2]] = distribusi.get(lagu[2], 0) + 1

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    print(f"  {'Total lagu':<16}: {len(playlist)}")
    print(f"  {'Jumlah genre':<16}: {len(genre_set)}")
    print(f"  {'Daftar genre':<16}: {format_genre_set(genre_set, playlist)}")
    print()
    print("  Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f"    {genre:<12}: {'#' * jumlah} ({jumlah})")
    print()
    print(f"  {'Lagu terpanjang':<16}: {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f"  {'Lagu terpendek':<16}: {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


def tampilkan_menu():
    print()
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")


def normalisasi_genre(genre):
    for g in GENRE_VALID:
        if g.lower() == genre.lower():
            return g
    return genre.title()


def main():
    playlist = []
    genre_set = set()

    print("=" * 40)
    print("   PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = normalisasi_genre(input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip())
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    raise ValueError
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Durasi harus berupa angka positif!")

        elif pilihan == "2":
            print()
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            if not playlist:
                print("Playlist masih kosong.")
                continue
            print(f"Genre tersedia: {format_genre_set(genre_set, playlist)}")
            target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, target)
            print()
            if hasil:
                print(f"Lagu bergenre '{hasil[0][2]}':")
                for i, (judul, artis, genre, durasi) in enumerate(hasil, 1):
                    print(f"  {i}. {judul} - {artis} ({format_durasi(durasi)})")
            else:
                print(f"Tidak ada lagu bergenre '{target}'.")

        elif pilihan == "4":
            if not playlist:
                print("Playlist masih kosong.")
                continue
            print()
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                if hapus_lagu(playlist, nomor):
                    # perbarui set genre agar sesuai dengan playlist
                    genre_set.clear()
                    genre_set.update(lagu[2] for lagu in playlist)
            except ValueError:
                print("Nomor harus berupa angka!")

        elif pilihan == "5":
            print()
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-6.")


main()