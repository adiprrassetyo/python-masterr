# Belajar String

nama = "Eko Kurniawan Khannedy"
kota = 'Jakarta'
alamat = 'Jalan Raya Bla Bla Bla'

nama_depan = "Eko"
nama_belakang = "Khannedy"
nama_lengkap = nama_depan + " " + nama_belakang

print(nama_lengkap)

#silicing pada string
s = "Hello World!"
print(s[4]) 		#ambil karakter kelima dari string s
print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
s[5]="d" 		    #ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print (s)

#menambahkan nilai variabel pada string
print('hai {}'.format('bro'))

nama = "Dicoding"
print("Halo, %s!" % nama)

nama = "Dicoding"
umur = 5
print("Umur %s adalah %d tahun." % (nama, umur))

#menambahkan objek selain string
angka = [7, 9, 11, 13]
print("Angka saya: %s" % angka)

#Contoh mencetak representasi Hexa (bilangan basis 16):
a, b = 10, 11
a, b
print('a: %x and b: %X' % (a, b))
