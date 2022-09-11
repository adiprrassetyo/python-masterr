# Belajar Continue

for i in range(1, 100):
    if i % 2 == 1:
        continue
    print(i)

#Pernyataan continue akan membuat iterasi saat ini berhenti, kemudian melanjutkan ke iterasi berikutnya, mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok perulangan.

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print(f'Huruf saat ini: {huruf}')
    
#cetak bintang yang sama dengan contoh 2 pada pembahasan fungsi break, dengan 1 loop dan 1 if (tanpa else):

jumlahbaris = 10
baris = 0
bintang = 0
while baris < jumlahbaris:
    if (bintang) >= (baris+1):
        print()
        baris = baris+1
        bintang=0
        continue      ##saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*",end="")
    bintang= bintang+1