'''
Katellyn Hyker
Chapter 6 Project 5
Sort the list in ascending order if empty or last item is less than or equal too the one before
isSorted expects a list and returns True if sorted and False if not

'''
import random

LIST_LENGTH = 5

def main():
    sortList = []
    while len(sortList) <= LIST_LENGTH:
            n = random.randint(1, 20)
            sortList.append(n)
    print(sortList)
    print(isSorted(sortList))


def isSorted(sortList):
    for i in range(1, len(sortList)):
         if sortList[i-1] > sortList[i]:
              return False
    return True
    

main()