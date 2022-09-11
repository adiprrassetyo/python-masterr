# Operator Perbandingan
# 
# > lebih dari
# < kurang dari
# >= lebih dari sama dengan
# <= kurang dari sama dengan
# == sama dengan
# != tidak sama dengan
# 

print(1 <= 1)
print(10 == 10)
print(10 != 9)

print("eko" == "eko")
print("eko" != "eko")

from operator import *
hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(hijau, kuning): {}'.format(func.__name__, func(hijau, kuning)))