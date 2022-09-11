class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def f(self):
        return 'hello world'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

Kalkulator.tambah_angka(100, 2)
print (Kalkulator.tambah_angka(100, 2))

k = Kalkulator()
print(k.tambah_angka(100, 2))