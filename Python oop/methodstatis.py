class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def f(self):
        return 'hello world'

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

a = Kalkulator.kali_angka(2, 3)
print(a)



k = Kalkulator()
a = k.kali_angka(2, 3)
print(a)