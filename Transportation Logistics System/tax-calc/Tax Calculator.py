# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 13:24:20 2025

@author: SEA4720
"""



income=int(input('Enter your taxable income:'))

if income<=18200:
    tax=0
    print(f'Tax payable on this income is: {tax}')
    
elif 18201 <= income <= 45000:
    taxable=income-18200
    tax = taxable * 0.19
    print(f'Tax payable on this income is: {tax}')
    
elif 45001 < income < 120000:
    taxable=income-45000
    tax=5092+taxable*0.325
    print(f'Tax payable on this income is: {tax}')
    
elif 12001 < income < 180000:
    taxable=income-120000
    tax=29467+taxable*0.37
    print(f'Tax payable on this income is: {tax}')
    
elif income > 180001:
    taxable=income-180000
    tax=51667+taxable*0.45
    print(f'Tax payable on this income is: {tax}')