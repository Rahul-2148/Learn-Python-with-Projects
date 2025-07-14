"""
it is used to compare the memory location of two variables/objects
is - True
is not - True
"""

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)
print(a is c)
print(a is not c)