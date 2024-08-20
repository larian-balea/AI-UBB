'''

@author: cami
'''
       
def gcd(a, b):
    if ((a < 0) or (b < 0)):
        raise ValueError("a and b must be positive")
    if (a == 0):
        if (b == 0):
            raise ValueError("one number must be != 0")
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
  
  
 
def test_gcd_v2():
    assert gcd(0, 2) == 2
    assert gcd(2, 0) == 2
    assert gcd(3, 2) == 1
    assert gcd(6, 2) == 2
    assert gcd(4, 6) == 2
    assert gcd(24, 9) == 3
    
    try:
        gcd(0, 0)
        assert False
    except ValueError:
        assert True
    
    try:
        gcd(0, -2)
        assert False
    except ValueError:
        assert True
        
    try:
        gcd(-2, 2)
        assert False
    except ValueError:
        assert True
    
test_gcd_v2()
    