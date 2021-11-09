class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads
    def attact(self):
        print('I am attacking....')

class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrr\n')

class Mournsnake(Monster):
    def make_sound(self):
        print('Hiisssshhhh\n')

fogthing = Fogthing("Fogthing", "Yello")
fogthing.attact()
fogthing.make_sound()

mournsnake = Mournsnake("Mournsnake","Red")
mournsnake.attact()
mournsnake.make_sound()


fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)

print('I have '+ str(fogthing.heads) +" "+ 'Heads and i\'m'+" "+ fogthing.color)
print('I also have '+ str(mournsnake.heads)+" "+ 'heads and i\'m'+" "+ mournsnake.color)
print('I got '+str(tangleface.heads)+" "+'heads and I\'m'+" "+ tangleface.color)

