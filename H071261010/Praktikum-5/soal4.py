def deteksi_anomali_email(email):
    error = []

    # Aturan 1: tepat satu '@'
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        # Aturan 3 tetap dicek
        if " " in email:
            error.append("Tidak boleh mengandung spasi.")
        return error

    local, domain = email.split("@")

    # Aturan 2: local/domain tidak kosong
    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tidak boleh ada spasi
    if " " in email:
        error.append("Tidak boleh mengandung spasi.")

    # Aturan 4: aturan titik pada local
    if local != "" and (local.startswith(".") or local.endswith(".") or ".." in local):
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    # Aturan 5: aturan domain
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: domain resmi
    if not email.lower().endswith((".com", ".id", ".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    border_char = karakter_border[0] if karakter_border else "="
    terpanjang = 0
    for e in daftar_email_valid:
        if len(e) > terpanjang:
            terpanjang = len(e)

    garis = "+" + border_char * (terpanjang + 2) + "+"
    hasil = garis + "\n"
    for e in daftar_email_valid:
        hasil += "| " + e.ljust(terpanjang) + " |\n"
    hasil += garis
    return hasil


if __name__ == "__main__":
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    print()
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    daftar_valid = []

    while True:
        email = input("Masukkan email: ")
        if email == "tutup":
            break

        error = deteksi_anomali_email(email)

        if not error and email in daftar_valid:
            error.append("Email sudah terdaftar (Duplikat).")

        if error:
            print(">> Email DITOLAK karena:")
            for e in error:
                print("   -", e)
        else:
            daftar_valid.append(email)
            print(">> Email VALID!")

    print()
    print("--- HASIL EMAIL VALID ---")
    print(cetak_daftar(daftar_valid, border))