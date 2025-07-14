'''
Encapsulation ka mtlb hota h internal details ko hide krna kisi bhi object ki and direct access krne se rokna , usko directly aap data me modification nhi kr skte kyuki yaha pe internal details ko jo h hide kiya gya h 
dusra aap controlled access de skte ho using methods i.e getters and setters

simple aese samjho ki encapsulation ka mtlb h ki aap sensitive data ko hide krte h aur sirf ek controlled access provide krte h jaise ki ek bank account ka example lete h

 self.__balance = balance #public variable #agar ariable ke name ke pahle __ laga diya toh wo private accessible hoga yaad rahe parameter me nhi lagana h self ke baad hi lagana h
'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance #private variable 

    def deposit(self, amount):
        self.__balance += amount #controlled access
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount): 
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance #controlled access #getters
    
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())

print(account.__balance) #attribute error aayega kyuki private variable h toh direct access nhi kr skte h 