start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

skip = int(input("Enter the number you want to skip: "))

for i in range(start, stop):
    if i == skip:
        continue
    print(i)