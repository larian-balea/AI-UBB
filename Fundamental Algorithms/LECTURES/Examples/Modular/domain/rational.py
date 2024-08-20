'''
Created on 15 Sep 2017

@author: cami
'''
import utils.numericlibrary

def test_sum():
    assert sum([2, 3], [4, 5]) == [22, 15]
    assert sum([1, 4], [1, 4]) == [1, 2]
    assert sum([1, 2], [1, 2]) == [1, 1]
    
    '''
    Descr: computes the sum of two rational numbers    
    Data: r1, r2
    Precondition: r1, r2 - rational numbers 
    Results: rs
    Postcondition:rs - rational number, rs = r1 + r2  
    '''
def sum(r1, r2):
    numerator = r1[0] * r2[1] + r1[1] * r2[0]
    denominator = r1[1] * r2[1]
    divisor = utils.numericlibrary.gcd(numerator, denominator)
    rs = [numerator / divisor, denominator / divisor]
    return rs 
   
test_sum()