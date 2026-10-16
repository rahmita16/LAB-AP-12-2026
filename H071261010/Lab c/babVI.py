# buah = ["Apel", "Jeruk", "Mangga"]

# print(buah[0])

# buah.append("Pisang")
# print(buah)

# angka = [30, 10, 20]

# angka.append(40)
# angka.insert(1, 15)
# angka.remove(30)
# angka.pop(0)
# angka.sort()

# print(angka)

# angka = [10, 20, 30, 40, 50, 60]

# print(angka[1:4]) 
# print(angka[::2])
# print(angka[::-1])

#study case 1
# data_nilai = [70, 80, 90, 75, 85]
# data_nilai.append(95)
# data_nilai.insert(2, 88)
# data_nilai.pop(0)

# print(f"Data nilai: {data_nilai}")
# print(f"Hasil slicing: {data_nilai[1:5:2]}")

# nilai = [[80, 90], [75,85]]

# print(nilai[0][1])

# angka = [1, 2, 3, 4, 5, 6]

# hasil = [x**2 for x in angka if x % 2 == 0]
# print(hasil)

#study case 2
# data_nilai = [60, 75, 90, 55, 85, 40]
# jumlah_nilai = [x for x in data_nilai if x >= 75]
# print(f"Jumlah nilai >= 75: {len(jumlah_nilai)}")
# print(f"Nilai >= 75: {jumlah_nilai}")

# bahasa = ["Python", "Java", "C++"]

# print(bahasa[0])
# print(bahasa[-1])

# data = ("python", True, 1)

# ubah = list(data)
# ubah[1] = False
# data = tuple(ubah)

# print(data)

#study case 3
# jadwal = ("Lab dasar", "Lab Jaringan", "Lab Pemrograman")
# ubah = list(jadwal)
# ruang_terakhir = ubah [-1]
# ubah[1] = "Lab Multimedia"
# hasil = tuple(ubah)
# print(f"Ruang terakhir: {ruang_terakhir}")
# print(f"Jadwal baru: {hasil}")

# angka = {1, 2, 2, 3, 3}
# print(angka)

# angka.add(4)
# angka.add(1)
# print(angka)

# a = {1,2,3,4}
# b = {3,4,5}

# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)

#study case 4
# a = {101, 102, 103, 104}
# b = {103, 104, 105, 106}
# print(f"semua peserta: {a | b}")
# print(f"peserta kedua: {a & b}")
# print(f"Khusus kelas A: {a - b}")

# mahasiswa = {
#     "nama": "nurul",
#     "nilai": 90
# }

# print(mahasiswa["nama"])
# print(mahasiswa["nilai"])

# mahasiswa = {
#     "nama": "nurul",
#     "nilai": {"matemtika": 80, "bahasa iggris": 90}
# }
# mahasiswa["nilai"]["matemtika"] = 90
# mahasiswa["nilai"]["fisika"] = 75
# mahasiswa.pop("nama")

# print(mahasiswa)

# mahasiswa = {
#     "nama": "Sari",
#     "nilai": {"matematika": 80, "bahasa inggris": 90}
# }
# mahasiswa["nilai"]["matematika"] += 10
# mahasiswa["nilai"]["fisika"] = 75
# mahasiswa.pop("nama")
# print(mahasiswa)
