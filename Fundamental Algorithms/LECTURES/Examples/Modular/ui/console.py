'''
Created on 15 Sep 2017

@author: cami
'''

import utils.numericlibrary
import domain.rational

def readRational():
    num = int(input("numerator = "))
    denom = int(input("denominator = "))
    while (denom == 0):
        print("denominator must be different to 0...give a new value")
        denom = int(input("denominator = "))
    num = num / utils.numericlibrary.gcd(denom, num)
    denom = denom / utils.numericlibrary.gcd(denom, num)    
    return [num, denom]

def run():
    finish = False
    r_sum = [0, 1]
    while (not finish):
        r = readRational()
        if (r[0] == 0):
            finish = True
        else:
            r_sum = domain.rational.sum(r_sum, r)
    print(r_sum)
    

