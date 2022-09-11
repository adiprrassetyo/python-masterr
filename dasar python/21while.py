#Perulangan Bertingkat
for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()

count = 0
while (count < 7):
    print(f'Hitungannya adalah: {count}')
    count = count + 1

# Seperti pada bahasa lainnya, eksekusi statement while mungkin bersifat infinit / infinite loop saat sebuah kondisi tidak pernah bernilai False. Contohnya sebagai berikut:
var = 1
while var == 1:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))


while True:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))