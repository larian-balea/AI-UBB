'''
Created on 10 Sep 2017

@author: cami
'''



def test_gcd():
    #test function for gcd
    assert gcd(14,21) == 7
    assert gcd(24, 9) == 3
    assert gcd(3, 5) == 1
    assert gcd(0, 3) == 3
    assert gcd(5, 0) == 5

    '''
    Descr: computes the gcd of 2 natural numbers    
    Data: a, b
    Precondition: a, b - natural numbers, b > 0
    Results: res
    Postcondition:res=(a,b)  
    '''
def gcd(a, b):
    if (a == 0):
        if (b == 0):
            return -1   # a == b == 0
        else:
            return b    # a == 0, b != 0
    else:
        if (b == 0):    # a != 0, b == 0
            return a
        else:           # a != 0, b != 0
            while (a != b):
                if (a > b):
                    a = a - b
                else:
                    b = b - a
            return a    # a == b

      
test_gcd()