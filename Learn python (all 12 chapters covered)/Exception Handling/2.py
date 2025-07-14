try:
    file = open("C:/Users/Rahul Raj Modi/OneDrive/Desktop/Rahul All Coding Works/Learn python with coding with sagar/Exception Handling/errors.txt", "r")
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print("File not found")
    
except PermissionError:
    print("You don't have permission to open this file")
    
finally:
    file.close()
    print('file operation completed')