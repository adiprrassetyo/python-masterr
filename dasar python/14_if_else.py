# Belajar If Else

menang = False

if menang:
    print("Selamat!")

else:
    print("Silahkan coba lagi!")
    
    
tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan>=160:
   print ("Silakan, Anda boleh masuk")
else:
   print ("Maaf, Anda belum boleh masuk")
   
   
bilangan = int(input("Masukkan Angka = "))
if bilangan % 2 == 0:
    print(f'Bilangan {bilangan} adalah genap')
else:
    print(f'Bilangan {bilangan} adalah ganjil')