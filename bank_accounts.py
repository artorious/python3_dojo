#!/usr/bin/env python3
""" Bank Account Objects - A program that manages accounts for a bank. 

BankAccount class implements a simple database of customer bank accounts.
Each account object;
    • account number instance variable (integer) - a unique identifier,
    • name instance variable (string) - account’s owner,
    • balance instance variable - current balance 
        (integer number of cents - use integers to avoid 
        floating-point imprecision)

Store the accounts in a list and move the contents of the list to a file for 
persistent storage.
"""
class BankAccount(object):
    """ Models a bank account """

    def __init__(self, acc_number, acc_name, acc_balance):
        """(BankAccount, int, str, int) -> BankAccount

        Initialize the instance variables of a bank account object.
        Disallows a negative initial balance.
        """ 
        if acc_balance < 0:
            raise ValueError('Negative initial balance not Allowed')
        
        self.__account_number = acc_number  # A/C no.
        self.__name = acc_name              # Customer name
        self.__balance = acc_balance        # Funds available in the account
    
    def id(self):
        """ (BankAccount) -> int
        
        Returns the account number of this bank account object.
        """
        return self.__account_number
    
    def deposit(self, amount):
        """ (BankAccount, int) -> BankAccount
        
        Add funds to the account.
        There is no limit to the size of the deposit.
        """
        self.__balance += amount

    def withdraw(self, amount):
        """ (BankAccount, int) -> BankAccount, bool
        
        Remove funds to the account, if possible.
        Only completes the withdrawal successfully if there are enough funds
        in the account to fulfill the withdrawal.
        Return True if successful, False otherwise
        """
        result = False  # Unsuccessful by default
        if self.__balance - amount >= 0:
            self.__balance -= amount
            result = True   # Successs
        return result

    def __str__(self):
        """ (BankAccount) -> str

        Returns the string representation for this object
        """
        return '[{:>5} {:<10} {:>7}]'.format(
                self.__account_number, self.__name, self.__balance)

# ----------------------------------------------------------------------------
# Global Functions that use BankAccount objects

def open_database(file_name, the_database):
    """ (file, list) -> list

    Read account information from a given file and store it in the given list
    """ 
    with open(file_name, 'r') as lines:   # Open file to read
        for line in lines:
            line.strip()
            number, name, balance = line.split(',')
            the_database.append(BankAccount(int(number), name, int(balance)))
            
def print_database(the_database):
    """ (list) -> stdout

    Display the contents of the database
    """
    for account_data in the_database:
        print(account_data) # Calls the __str__ method of account_data
        
def get_account(the_database, account_number):
    """ (list, int) -> int
    
    Retrieve an account object with a given account number.
    """
    for account_data in the_database:
        if account_data.id() == account_number:
            return  account_data

def main():
    """ Simple bank account 'database' """

    database = []

    try:
        # Open the database of accounts
        open_database('text/account_data.txt', database)
        print_database(database)
        print('-' * 60)
        customer = get_account(database, 129)
        
        if customer:
            print('Account 129 before deposit of $100: ', end='')
            print(customer)

            customer.deposit(100)
            print('Account 129 after deposit of $100: ', end='')
            print(customer)
            
            print('-' * 60)

            print('Account 129 before withdraw of $500: ', end='')
            print(customer)

            customer.withdraw(500)
            print('Account 129 after withdraw of $500: ', end='')
            print(customer)
            
            print('-' * 60)

            print('Account 129 before withdraw of $80000: ', end='')
            print(customer)

            customer.withdraw(80000)
            print('Account 129 after withdraw of $80000: ', end='')
            print(customer)

    except Exception as eerr:
        print('Error in account database : {0}'.format(eerr))
        raise

if __name__ == '__main__':
    main()