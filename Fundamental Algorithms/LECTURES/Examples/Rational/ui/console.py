'''

@author: cami
'''
#from domain.Rational_f import Rational
from domain.Rational_v import Rational

rationalnumbers = []

def readRational():
    '''
        read a rational number
        raise ValueError if the numerator and denominator do not satisfy preconditions
    '''
    num = int(input("numerator = "))
    denom = int(input("denominator = "))
    r = Rational(num, denom)
    return r 
    
def printRational(r):
    print(str(r.getNumerator()) + "/" + str(r.getDenominator()))
    #print(r)
    
    
def run():
    print("give (numerator. denominator) pairs until (0,*)")
    
    finish = False
    r_sum = Rational()
    while (not finish):
        try:
            r = readRational()
            if (r.getNumerator() == 0):
                finish = True
            else:
                r_sum = r_sum.add(r)
        except ValueError as ex:
            print("something doesn't work: " + str(ex))         
    
    print("sum of read rational numbers is : ")
    printRational(r_sum)
    
