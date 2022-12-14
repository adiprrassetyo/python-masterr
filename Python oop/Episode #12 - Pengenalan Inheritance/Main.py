class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai

####
class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

###
class KalkulatorKali(Kalkulator):
    """ contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    def bagi_angka(self, angka1, angka2):
        self.nilai =  angka1 / angka2
        return self.nilai

###
class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai


kk = KalkulatorKali()
a = kk.kali_angka(2, 3)  # sesuai dengan definisi class memiliki fitur kali_angka
print(a)

b = kk.bagi_angka(10, 2)  # memiliki fitur tambah_angka karena mewarisi dari Kalkulator
print(b)

class Hero:

	def __init__(self,name,health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero):
	pass

class Hero_strength(Hero):
	pass

lina = Hero('lina',100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(lina.health)
print(techies.name)
print(axe.name)