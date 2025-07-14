a = [1,2,3, "python", 'java', True, 1,1,1,2,3]
counter = a.count(1)
print(counter)


counter = sum(1 for i in a if i is 1)
print(counter)  # Output: 4
