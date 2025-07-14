"""
burger - function
extra cheese - extra feature

main function > function add
without changing the main function code 
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the fuction is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator # @laa kr btana h ki hm decorator use kr rhe h old fn me new chij dal rhe h without change the old function
def say_hello():
    print("Hello")

say_hello()

# eg use in 2-factor authentication after login, puchta h lgana h ya nhi agr ha toh yahi concept use hota h 