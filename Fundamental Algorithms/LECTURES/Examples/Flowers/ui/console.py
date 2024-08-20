'''

@author: cami
'''
from domain.Flower import Flower
flowers = []

def readFlower():
    '''
    reads a flower (name and price)
    
    '''
    flowerName = input("name = ")
    flowerPrice = int(input("price = "))
    f = Flower(flowerName, flowerPrice)
    return f

def readFlowers():
    '''
    reads more flowers
    
    '''
    global flowers
    correct = False
    while (not correct):
        try:
            s = input("no of flowers = ")
            n = int(s)
            if (n >= 0):
                correct = True
            else:
                print("please give a positive integer (the no of flowers)")
        except:
            print("please give an integer (the no of flowers)")
            
    i = 0
    while(i < n):
        try:
            crtFlower = readFlower()
            flowers.append(crtFlower)
            i = i + 1
        except ValueError as ex:
            print("something doesn't work: ", ex)
    
def printFlowers():
    '''
    prints all the flowers
    '''
    global flowers
    for f in flowers:
        print(f)
    
def printMenu():
    '''
    print a menu with options
    '''
    print("Choose an option: ")
    print("1: read flowers")
    print("2: print flowers")
    print("0: exit")
    print("opt = ")
    
def run():
    '''
    implement the user interface
    '''
    cont = True
    while (cont):
        printMenu()
        opt = input("")
        if (opt == "1"):
            readFlowers()
        elif (opt == "2"):
            printFlowers()
        elif (opt == "0"):
            print("bye bye...")
            cont = False
        else:
            print("please give a correct option...")

    