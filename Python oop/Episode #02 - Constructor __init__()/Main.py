#class Kalkulator:
    #""" contoh kelas kalkulator sederhana"""

    #def __init__(self):
        #self.i = 12345

    #def f(self):
        #return 'hello world'

class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = i  # i adalah variabel pada constructor, self.i adalah variabel dari class

    def f(self):
        return 'hello world'

k = Kalkulator(i=1024)
print(k.i)


class Hero: # template

    def __init__(self, inputName, inputHealth,inputPower, inputArmor):
    	self.name = inputName
    	self.health = inputHealth
    	self.power = inputPower
    	self.armor = inputArmor


hero1 = Hero("sniper",100, 10, 4)
hero2 = Hero("mirana",100, 15, 1)
hero3 = Hero("ucup",1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)