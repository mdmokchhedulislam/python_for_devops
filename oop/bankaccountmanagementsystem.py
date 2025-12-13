class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.__account_number=account_number
        self.__owner=owner
        self.__balance=balance
    

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def owner(self):
        return self.__owner
    

    @owner.setter
    def owner(self, name):
        if isinstance(name, str) and len(name)>0:
            self.__owner=name
        else:
            print("owner name must be a valid string")

    @property
    def balance(self):
        return self.__balance
    

    def deposit(self, amount):
        if amount > 0:
            self.__balance +=amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
             print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrow ${amount}, new balance: ${self.__balance}")
        else:
            print("insufficient balance or invalid ammount")

    def display_info(self):
        print("-----Account Info-----")
        print(f"Account Number: {self.__account_number}")
        print(f"Owner: {self.__owner}")
        print(f"Balance: ${self.__balance}")
        print("---------------------")

if __name__ == "__main__":

    user1 = BankAccount("AC110", "mokchhedul", 1000)

    user1.display_info()
    user1.deposit(500)
    user1.withdraw(200)
    print(f"Current Balance: ${user1.balance}")

    user1.owner = "Karim"
    print(f"Updated Owner: {user1.owner}")