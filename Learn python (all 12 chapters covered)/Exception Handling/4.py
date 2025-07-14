#check password strength

# import pandas as pd
# pd.set_option('display.max_colwidth', None)

def check_password(password):
    if len(password) < 8:
        raise Exception("Error: Password must be at least 8 characters long.")
    
    if not any(char.isupper() for char in password):
        raise Exception("Error: Password must contain at least one uppercase letter.")
    
    if not any(char.islower() for char in password):
        raise Exception("Error: Password must contain at least one lowercase letter.")
    
    if not any(char.isdigit() for char in password):
        raise Exception("Error: Password must contain at least one digit.")
    
    print('Password is strong')

try: 
    password = input("Enter your password: ")
    check_password(password)

except Exception as e:
    print(e)