class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color= color
    def attack(self):
       print('I am attacking')

class Fogthing(Monster):
    def make_sound(self):
        print("grrrrrrrr")

class Mounrsnake(Monster):
    def make_sound(self):
        print('This ...')
fogthing = Fogthing("Fog", "Yell")
fogthing.attack()
fogthing.make_sound()

mournsnake = Mounrsnake("Mournsnake","Red")
mournsnake.attack()
mournsnake.make_sound()
