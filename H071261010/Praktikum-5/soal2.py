ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    hasil = []
    if kata == "":
        return hasil
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    while True:
        idx = teks_kecil.find(kata_kecil, start)
        if idx == -1:
            break
        hasil.append(idx)
        start = idx + 1
    return hasil


def cek_batas_kata(teks, i, panjang):
    # Karakter sebelum kata
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    # Karakter sesudah kata
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    indeks_valid = []
    hasil = ""
    pos = 0
    pengganti = simbol[0] * len(kata) if simbol else "#" * len(kata)

    for idx in semua_indeks:
        if idx < pos:
            continue
        if cek_batas_kata(teks, idx, len(kata)):
            hasil = hasil + teks[pos:idx] + pengganti
            pos = idx + len(kata)
            indeks_valid.append(idx)

    hasil = hasil + teks[pos:]
    return (hasil, len(indeks_valid), indeks_valid)


if __name__ == "__main__":
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")
    hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
    print("Hasil Teks:", hasil)
    print("Jumlah:", jumlah, "| Indeks:", indeks)