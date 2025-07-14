try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f'result: {result}')
    
except ZeroDivisionError:
    print("You cannot divide with 0")
    
except ValueError:
    print("You cannot divide with string")