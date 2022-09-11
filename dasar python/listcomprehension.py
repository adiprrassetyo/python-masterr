#Cara 1
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

#Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

#Contoh3 menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
  for b in list2:
    if a == b:
      duplikat.append(a)

print(duplikat)  # Output ['d','i']


#Contoh4 Implementasi dengan list comprehension
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat) # Output: ['d','i']

# Contoh 5 kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)

list_a = range(1,10,2)
x = [ [a**2, a**3] for a in list_a]
print(x)