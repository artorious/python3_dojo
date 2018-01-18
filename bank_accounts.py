#!/usr/bin/env python3
""" Bank Account Objects - A program that manages accounts for a bank. 
TODO:
Use a BankAccount class to implement a simple database of customer bank 
accounts.
Define a class of bank account objects
Each account object would have;
    • account number instance variable (integer) - a unique identifier,
    • name instance variable (string) - account’s owner,
    • balance instance variable - current balance 
        (integer number of cents - use integers to avoid 
        floating-point imprecision)

Store the accounts in a list and move the contents of the list to a file for persistent storage.

NOTE:
Real bank accounts must store a large amount of information: 
the account owner’s name, address, social security number, account number, etc. 
"""
class BankAccount(object):
    """ Models a bank account """

    def __init__(self, acc_number, acc_name, acc_balance):
        """(BankAccount, int, str, int) -> BankAccount

        Initialize the instance variables of a bank account object.
        Disallows a negative initial balance.
        """ 
        pass
    
    def id(self):
        """ (BankAccount) -> int
        
        Returns the account number of this bank account object.
        """
        return 
    
    def deposit(self, amount):
        """ (BankAccount, int) -> BankAccount
        
        Add funds to the account.
        There is no limit to the size of the deposit.
        """
        pass

    def withdraw(self, amount):
        """ (BankAccount, int) -> BankAccount, bool
        
        Remove funds to the account, if possible.
        Only completes the withdrawal successfully if there are enough funds
        in the account to fulfill the withdrawal.
        Return True if successful, False otherwise
        """
        return 

    def __str__(self):
        """ (BankAccount) -> str

        Returns the string representation for this object
        """
        return

# ----------------------------------------------------------------------------
# Global Functions that use BankAccount objects

def open_database(file_name, the_database):
    """ (file, list) -> list

    Read account information from a given file and store it in the given list
    """ 
    pass

def print_database(the_database):
    """ (list) -> stdout

    Display the contents of the database
    """
    pass

def get_account(the_database, account_number):
    """ (list, int) -> BankAccount
    
    Retrieve an account object with a given account number.
    """
    pass

def main():
    """ Simple bank account 'database' """

    database = []

    try:
        pass

    except Exception as eerr:
        print('Error in account database : {0}'.format(eerr))
        raise

if __name__ == '__main__':
    main()