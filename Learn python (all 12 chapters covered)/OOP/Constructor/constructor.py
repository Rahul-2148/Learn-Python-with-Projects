"""
__init__() method is a special method in Python that is called when a new object is created from a class. It is used to initialize the attributes of the object.

aao ek exmple se samajhte h constructor kya hota h:
suppose aapne ek smartphone kharida, jb aap us phone ko chalu kroge pehli baar me toh auomatically jo wo h ek default language pakadta h ek default time pakadta h aur ek default WiFi se jo h connect krne ki koshish krta h agar koi free open pada hua h toh wo usse connect ho jata h, so authomatic jo setup process h yaha pe wo ho chuki h, automatic language, time sb select kr liya baad me ja kr aap modification karte ho ki agar usne japanese select kari h toh aap english me set kr loge, time agar usne dusri country ka select kiya ho toh aap India ka kar loge, apne ghar ka WiFi connect krte ho so initial jo setup tha wo automatically ho gya so similarly jo ye automatic setup process h yahi Constructor hoti h python me as soon as jaise hi object create hota h usko iniialize krne ke liye iska use kiya jata h, so akhir me ham samajhte h ki aakhir me iski jarurat kya h, why we need a constructor bina constructor ke aapko ek method ko manually call krna padega and uski values ko assign krna padega object ko so Constructor jo h aapki is process ko automate krta h, jaise ki ham kya krte h without constructor manually value set krenge, jaise ki ek car krke hamne class banaya ab ham set_details krke ek method create krte h jisme ham self brand aur color ko set krenge
"""

# Note: this is withour constructor jisme hame manually set_details ko call krna pad rha h ab with constructor se kaise hoga automatic ye aap mere with constructor file me dekh lo  

class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
        
# creating objects
car1 = Car()
car1.set_details('Tesla', 'Red')

print(car1.brand, car1.color)