# generator ki just like vending machine ki wo ek baar me ek hi product deliver krti h aur wahi jo ham select krte h 

# yield keyword
def count_down(num):
    while num > 0:
        yield num #yield values one at a time
        num -= 1
        
#using the generator
for num in count_down(5):
    print(num)
    
    
# decorator ka use kiya jata h to modify and enhance functions without changing the original function, basically then wrap the original function, ye extra functionality de deta h mere original function ke andar

#generator ka use kiya jata h to generate the sequence of values over time, yani ki ek value pr ek baar me aap ek hi value ko operate krte h, sari jo iterator h wo pura memory consume nhi krta h