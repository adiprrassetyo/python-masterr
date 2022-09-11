# Belajar Elif => else if

menu_pilihan = input("Silahkan pilih menu [1-3] : ")

if menu_pilihan == "1":
    print("Anda memilih menu 1")
elif menu_pilihan == "2":
    print("Anda memilih menu 2")
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
else:
    print("Menu tidak tersedia")

if menu_pilihan == "x":
    print("Program keluar")


#kasus penilaian tugas siswa.

nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai>80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai>70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai>60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")


#kasus pengecekan bilangan positif, negatif, atau nol.
bilangan = int(input("Masukkan Bilangan = "))
if bilangan > 0:
    print(f'Bilangan {bilangan} adalah positif')
elif bilangan < 0:
    print(f'Bilangan {bilangan} adalah negatif')
else:
    print(f'Bilangan {bilangan} adalah nol')