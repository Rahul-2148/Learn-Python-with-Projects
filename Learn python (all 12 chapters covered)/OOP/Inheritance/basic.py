class Animal: #parent class
    def speak(self):
        print("Animal make sound")
        
class Dog(Animal): #child class 
    def bark(self):
        print("Dog barks")
        
dog = Dog()
dog.speak()
dog.bark()
