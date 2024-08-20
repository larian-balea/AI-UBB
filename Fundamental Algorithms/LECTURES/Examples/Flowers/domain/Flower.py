'''

@author: cami
'''
class Flower:
    '''
    a flower is a structure of two elements: name (a string) and price (an integer)
    
    '''
    def __init__(self, n = "", p = 0):
        '''
            creates a new instance of Flower
            
        '''
        self.name = n
        if (p < 0):
            raise ValueError("the price must be positive...")
        self.price = p
        
    def getName(self):
        '''
            getter method
            return the name of a flower
        '''
        return self.name
    
    def getPrice(self):
        '''
            getter method
            return the price of a flower
        '''
        return self.price  
    
    def setName(self, n):
        '''
            setter method
            set the name of a flower
        '''
        self.name = n
        
    def setPrice(self, p):
        '''
            setter method
            set the price of a flower
        '''
        if (p < 0):
            raise ValueError("the price must be positive...")
        self.price = p
        
    def __str__(self):
        '''
            provides a string representation of a flower
            return a string
        '''
        return self.name+ "-" + str(self.price)
       
    def __eq__(self, other):
        '''
            compares 2 flowers: self and other
            return True, if self == other
                   False, otherwise
        '''
        if ((self.name == other.name) and (self.price == other.price)):
            return True
        else:
            return False
    
def test_create():
    f1 = Flower("tulip", 10)
    assert f1.getName() == "tulip" and f1.getPrice() == 10
    f2 = Flower()
    assert f2.getName() == "" and f2.getPrice() == 0
    f3 = Flower("daisy")
    assert f3.getName() == "daisy" and f3.getPrice() == 0
    f3.setName("rose")
    assert f3.getName() == "rose"
    f3.setPrice(7)
    assert f3.getPrice() == 7
    
    try:
        f4 = Flower("rose", -2)
        assert False
    except:
        assert True
         
    
    
def test_str():
    f1 = Flower("tulip", 10)
    assert f1.__str__() == "tulip-10"
    f2 = Flower()
    assert f2.__str__() == "-0"
    f3 = Flower("rose")
    assert f3.__str__() == "rose-0"
    
def test_eq():
    f1 = Flower("tulip", 10)
    f2 = Flower("tulip", 10)
    assert f1 == f2
    f3 = Flower("daisy", 5)
    assert f1 !=  f3
    
    
test_create()
test_str()
test_eq()
    