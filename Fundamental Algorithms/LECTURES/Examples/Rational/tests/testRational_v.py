'''

@author: cami
'''

from domain.Rational_v import Rational

        
            
def test_create():
    r1 = Rational(3, 2)  
    assert r1.getNumerator() == 3 and r1.getDenominator() == 2
       
    r2 = Rational(4, 5)  
    assert r2.getNumerator() == 4 and r2.getDenominator() == 5
    
    r3 = Rational(15, 25)  
    assert r3.getNumerator() == 3 and r3.getDenominator() == 5
    
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
    r3 = Rational(5,3)
    assert r1 != r3
   
test_create() 
test_add()
test_str()
test_eq()
print("all tests are ok...")