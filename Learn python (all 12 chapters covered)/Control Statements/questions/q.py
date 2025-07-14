"""
1-10
even numbers
2,4,6,8,10

1,3,5,7,9

%2 == 0

2 % 2 = 0
2 % 3 = 1
2 % 4 = 2

i = 1
i = 2
i = 3...
i = 10 
"""
for i in range(1,11):
    if i % 2 == 0:
        print("even", i)
    else:
        print("odd", i)