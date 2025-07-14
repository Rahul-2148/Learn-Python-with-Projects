# this is a write mode data

file = open("C:/Users/Rahul Raj Modi/OneDrive/Desktop/Rahul All Coding Works/Learn python with coding with sagar/File Handling/files.txt", "w")
content = input('Enter the data to write: ')
file.write(content)
print('data written & saved successfully')

file.close()