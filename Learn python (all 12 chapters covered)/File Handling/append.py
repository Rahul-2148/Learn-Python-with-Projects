with open('C:/Users/Rahul Raj Modi/OneDrive/Desktop/Rahul All Coding Works/Learn python with coding with sagar/File Handling/data.txt', 'a') as file:
    content = input('Enter the data to write: ')
    file.write(content)
    print('content appended successfully')