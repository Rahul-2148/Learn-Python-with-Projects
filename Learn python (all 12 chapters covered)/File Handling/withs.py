with open("C:/Users/Rahul Raj Modi/OneDrive/Desktop/Rahul All Coding Works/Learn python with coding with sagar/File Handling/data.txt", "w") as file:
    
    content = input('Enter the content to write: ')
    file.write(content)
    print('data written & saved successfully')