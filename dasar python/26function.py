# Belajar Module

def say_hello(nama):
    return f"Hello {nama}"

def total(*list_angka):
    hasil = 0
    for data in list_angka:
        hasil = hasil + data
    return hasil

total()

def cetak(param):
    print(param)
    return

cetak("Dicoding Indonesia")

def penjumlahan(a, b):
    a+b

hasil = penjumlahan(10, 10)
print(hasil)