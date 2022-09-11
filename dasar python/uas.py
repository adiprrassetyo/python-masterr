Nilai = [7,2,1,8,5,7,2,1,11,9,6]
print("\n1. Akses List Per index: ")

print (Nilai [8])#Baris 8
print (Nilai [0])#Baris 0
print (Nilai [3])#Baris 3

print("\n2. Mengintegrasikan isi List: ")
for i in Nilai:
    print (i, end ="")

print("\n3. Panjang List: ", len (Nilai))

print("\n4. Banyaknya Angka 0: ", str(Nilai.count (0)))

print("\n5. Menambah Element List Dengan Append: ")
Nilai.append (17)
print (Nilai)

print("\n6. Mencari Posisi suatu Nilai dengan Index: ")
print (Nilai.index (5))
#- angka 6 terletak dibaris 4

print("\n7. Menyisipkan suatu nilai ke posisi tertentu: ")
Nilai.insert (9,21) #- menyisipkan angka 21 di baris ke 9
Nilai.insert (3, 43) #- menyisipkan angka 43 di baris ke 3
Nilai.insert (5, 55) #- menyisipkan angka 55 di baris ke 5
print (Nilai)

print("\n8. Membuang nilai tertentu dengan pop(): ")
Nilai.pop(0)
print (Nilai)

print("\n9. menghapus nilai tertentu dengan remove(): ")
Nilai.remove (11) #- menghapus nilai 11 dari Nilai print (Nilai)

print("\n10. menyambung data list dengan extend(): ")
angkal=[31, 32, 33, 24, 35, 66]
Nilai.extend (angkal)
print (Nilai)

print("\n11. membalik urutan list dengan reserve (): ")
Nilai.reverse()
print (Nilai)

print("\n12. mengurutkan nilai dari yang terkecil hingga ke terbesar menggunakan sort(): ")
Nilai.sort()
print (Nilai)

print("\n13. mencari nilai maximum dengan max(): ")
print (max (Nilai))

print("\n14. memcari nilai minimal dengan min (): ")
print (min (Nilai))

print("\n15. mencari total nilai dengan sum(): ")
print (sum (Nilai))

print("\n16. mencari rata-rata total dari nilai:")
a = sum(Nilai) / len(Nilai)
print(a)