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
        self.numerator = num // d
        self.denominator = denom // d
        
    def getNumerator(self):
        '''
            getter method
            return the numerator of the rational number
        '''
        return self.numerator
    
    def getDenominator(self):
        '''
            getter method
            return the denominator of the rational number
        '''
        return self.denominator
    
    def add(self, other):
        '''
            add two rational numbers (self + other)
            return a new rational number self = self + other
        '''
        a = self.numerator * other.denominator + self.denominator * other.numerator
        b = self.denominator * other.denominator
        d = gcd(a, b)
        self.numerator = a // d
        self.denominator = b // d
        return self
    
    def __str__(self):
        
        '''
            provides a string representation of a rational number
            return a string
        '''
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __eq__(self, other):
        '''
            compares 2 rational numbers: self and other
            return True, if self == other
                   False, otherwise
        '''
        if ((self.numerator == other.numerator) and (self.denominator == other.denominator)):
            return True
        else:
            return False
            
   