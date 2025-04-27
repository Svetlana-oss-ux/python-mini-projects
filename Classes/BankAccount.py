# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 08:54:59 2025

@author: Svetlana Kolos
"""

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
        
        
    def deposit (self,amount):
        if amount  > 0:
            self.balance+=amount
            print(f'The deposit amount is {self.balance}')
            
        else:
            print(f"The deposit amount should be positive")
            
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You withdraw {self.amount}")
        else:
            print("Unsufficient balance")
            
    def display(self,balance):
        print(f"The balance is {self.balance}")
        
amount= float(input("Enter the amount to withdraw"))
balance=float(input("Enter initial balance"))
account = BankAccount("Jordan", balance)
account.withdraw(amount)
account.display_balance()

        
        
    
    
    
    