# Belajar Membuat Method / Function

nama = []

def print_nama():
    print("=================")
    for data in nama:
        print(data)

nama.append("eko")
print_nama()

nama.append("kurniawan")
print_nama()

nama.append("khannedy")
print_nama()
#dicoding

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print(f'Dicetak dari dalam fungsi :{hasil}')
    return hasil

keluaran = kali(10, 20);
print(f'Dicetak sebagai kembalian: {keluaran}')

def kuadrat(x):
    return x*x
a = 10
k = kuadrat(a)
print(f'nilai kuadrat {a} adalah {k}')

#Pass by reference vs value


def ubah(list_saya):
    "Deklarasi Variabel list_saya berikut hanya di kenali(berlaku) di dalam fungsi ubah"
    list_saya = [1, 2, 3, 4]
    print(f'Nilai di dalam fungsi: {list_saya}')

# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print(f'Nilai di luar fungsi: {list_saya}')

