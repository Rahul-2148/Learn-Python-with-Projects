
age = int(input("Enter your age: "))

if age >= 18 and age < 101: # True
    print("You are eligible to vote")
elif age >= 101:
    print("Greater than 101")
elif age <= 0: # False
    print("You are not eligible to vote")
else :
    print("Error Occured")