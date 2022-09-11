print('Dicoding'.center(20, '-'))

while True:
    print('Masukkan nama Anda:')
    name = input()
    if name.isalnum():
        print("Halo", name)
        break
    print('Masukkan nama Anda dengan benar')

for huruf in 'Dicoding':  # Contoh pertama
    print(f'Huruf: {huruf}')

flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:  # Contoh kedua
    print(f'Flower: {flower}')
#fungsi len()
for index in range(len(flowers)):
    print('Flowers: {}'.format(flowers[index]))

