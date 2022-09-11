# Belajar Argument List

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10, 10, 10, 10, 10, 10)

def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i':7, 'j':8})