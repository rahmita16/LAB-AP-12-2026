ALFABET = "abcdefghijklmnopqrstuvwxyz"


def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        huruf = ch.lower()
        if huruf in ALFABET:
            hasil += huruf
    return hasil


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)


def inti_palinrome(teks):
    terpanjang = ""
    awal = 0
    n = len(teks)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks[i:j]
            if cek_palinrome(sub)[0] and len(sub) > len(terpanjang):
                terpanjang = sub
                awal = i
    return {"teks": terpanjang, "panjang": len(terpanjang), "indeks_awal": awal}


if __name__ == "__main__":
    teks = input("Masukkan teks prasasti: ")
    bersih = bersihkan_teks(teks)
    print()
    print("Teks Bersih:", bersih)
    print("Output Terharap:", inti_palinrome(bersih))
    