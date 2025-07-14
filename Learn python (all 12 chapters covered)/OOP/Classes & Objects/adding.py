class Car:
    def set_details(self, brand, color): 
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f'This car is a {self.color} {self.brand}')


car1 = Car()
car1.set_details('Tesla', 'Red')

car2 = Car()
car2.set_details('BMW', 'Blue')

car1.show_details()
car2.show_details()

# Output:
# This car is a Red Tesla
# This car is a Black BMW