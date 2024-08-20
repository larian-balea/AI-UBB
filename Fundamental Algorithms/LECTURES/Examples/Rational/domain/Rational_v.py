'''

@author: cami
'''
from utils.numericLibrary import gcd

class Rational:
    '''
    A rational number is composed by 2 numbers: numerator and denominator > 0
    denominator <> 0, gcd(numerator, denominator) == 1
    '''
    def __init__(self, num = 0, denom = 1):
        '''
            creates a new instance of Rational
        '''
        if (denom == 0):
            raise ValueError("0 denominator not allowed")
        if (num < 0) or (denom < 0):
            raise ValueError("numerator and denominator must be positive numbers")
        d = gcd(num, denom)
        self.number = [num // d, denom // d]
        
    def getNumerator(self):
        '''
            getter method
            return the numerator of the rational number
        '''
        return self.number[0]
    
    def getDenominator(self):
        '''
            getter method
            return the denominator of the rational number
        '''
        return self.number[1]
    
    def add(self, other):
        '''
            add two rational numbers (self + other)
            return a new rational number self = self + other
        '''
        a = self.number[0] * other.number[1] + self.number[1] * other.number[0]
        b = self.number[1] * other.number[1]
        d = gcd(a, b)
        self.number = [a // d, b // d]
        return self
        
        
    def __str__(self):
        '''
            provides a string representation of a rational number
            return a string
        '''
        return str(self.number[0]) + "/" + str(self.number[1])
       
    def __eq__(self, other):
        '''
            compares 2 rational numbers: self and other
            return True, if self == other
                   False, otherwise
        '''
        if ((self.number[0] == other.number[0]) and (self.number[1] == other.number[1])):
            return True
        else:
            return False
    