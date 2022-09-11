n = int(input("Masukkan angka ="))
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")


#Pada contoh diatas, loop akan di break saat nilai n == 7, saat keluar dari perulangan, maka python tidak akan memunculkan tulisan Loop selesai, namun jika tidak dilakukan break (perulangan berakhir dengan normal):    
n = 10
while n > 0:
    n = n - 1
    print(n)
else:
    print("Loop selesai")