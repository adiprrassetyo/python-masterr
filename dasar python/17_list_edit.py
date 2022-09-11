# Membuat List
nama = ["eko", "budi", "andi"]

# Menambah Data ke List
nama.append("joko")

# Mengakses List
nama[0]

# Menghapus Data dari List
nama.remove("budi")

# Mengubah Data di List
print(nama)
nama[0] = "kurniawan"
print(nama)

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)