class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
        
        print(brand, color)
        
car1 = Car()
car1.set_details('Tesla', 'Red')

# Output:
# Tesla Red

'''
Know these points:
i. Always use self to store a property inside an object.

ii. python automatically object ko pass krta h as a self argument so waha pr aapko method ke definition pe usko define krna hi padega self ko include krna hi padega nhi toh TypeError eeror aa jayega ki TypeError: Car.set_details() takes 2 positional arguments but 3 were given

iii. Bina self ke object me variable store hi nhi hone wala jisse error aane wala h yani ki agar aap self hata doge toh ye jo variable ke andar data h wo store hi nhi ho payega, so this is all about classes and objects.
'''