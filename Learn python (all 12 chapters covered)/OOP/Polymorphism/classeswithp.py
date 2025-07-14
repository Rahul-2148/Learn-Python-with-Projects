#polymorphism with classes method overriding

class Bird():
    def sound(self):
        print('Birds make sounds')
        
class Crow(Bird):
    def sound(self):
        print('Crow says caw caw')
        
class Parrot(Bird):
    def sound(self):
        print('Parrot says squak hello')
        
bird1 = Crow()
bird1.sound()

bird2 = Parrot()
bird2.sound()