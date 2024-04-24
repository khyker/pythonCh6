'''
Katellyn Hyker
Chapter 6 Project 10
Define and test a function myRange
Behaves like standard range function but returns a list (dont use range function)
Default value of None and if parameters both equal None function called with just stop value
If just third equals None function called with a start value

'''

def myRange(a, b=None, step=None):
    numList = []
    if b is None:
        b = a
        a = 0
        while a < b:
            numList.append(a)
            a += 1
    while step is None and a < b:
        numList.append(a)
        a += 1
    while step is not None and a < b:
        numList.append(a)
        a += step
    return numList

print(myRange(0, 100, 10))