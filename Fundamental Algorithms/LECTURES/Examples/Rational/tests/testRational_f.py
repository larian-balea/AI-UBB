'''

@author: cami
'''
from domain.Rational_f import Rational
         
def test_create():
    r1 = Rational(2,3)  
    assert r1.getNumerator() == 2 and r1.getDenominator() == 3
       
    r2 = Rational(5,4)  
    assert r2.getNumerator() == 5 and r2.getDenominator() == 4
    
    r3 = Rational(25, 15)  
    assert r3.getNumerator() == 5 and r3.getDenominator() == 3
    
    r4 = Rational(3)
    try:
        r4 = Rational(2, 0)
        assert False
    except ValueError as er:
        print("something goes wrong...", er)
        assert True
        
    try:
        r5 = Rational(2, -3)
        assert False
    except ValueError as er:
        print("something goes wrong...", er)
        assert True
        
    try:
        r6 = Rational(-2, 3)
        assert False
    except ValueError as er:
        print("something goes wrong...", er)
        assert True
        
    try:
        r7 = Rational(-2, -3)
        assert False
    except ValueError as er:
        print("something goes wrong...", er)
        assert True
        
    
    
    

def test_add():
    r1 = Rational(2,3)  
    r2 = Rational(5,4)  
    r3 = r1.add(r2)
    assert r3.getNumerator() == 23 and r3.getDenominator() == 12

    
def test_str():
    r1 = Rational(2,3)
    assert r1.__str__() == "2/3"

    
def test_eq():
    r1 = Rational(2,3)
    r2 = Rational(2,3)
    assert r1 == r2
    assert r1.__eq__(r2) == True
    
    r3 = Rational(5,3)
    assert r1 != r3
    assert r1.__eq__(r3) == False

test_create()
test_add()
test_str()
test_eq()

print("all tests are ok...")
