import  cmath
from cmath import sqrt


a = float( input("Masukkan Nilai A : ") )
b = float( input("Masukkan Nilai B : ") )
c = float( input("Masukkan Nilai C : ") )

diskriminasi = float(b * b) - (4 * a * c)

if diskriminasi > 0 :
    x1 = float(-b + cmath.sqrt(diskriminasi)) / (2 * a)
    x2 = float(-b - cmath.sqrt(diskriminasi)) / (2 * a)
    print(f"Akar Real = {x1}, {x2}")
elif diskriminasi == 0.0 :
    x1 = (-b) / (2 * a)
    x2 = x1
    print(f"Akar Kembar = {x1}, {x2}")
else :
    re = float(-b) / (2 * a)
    x2 = cmath.sqrt(diskriminasi) / (2 * a)
    im = cmath.sqrt(abs(diskriminasi)) / (2 * a)
    print(" Akar Komplek")
    print("x1 =", re + im)
    print("x2 =", re - im)