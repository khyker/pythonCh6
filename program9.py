'''
Katellyn Hyker
Chapter 6 Project 9
A program that calculates and prints the average of numbers in a text file in a simple design using higher-order functions

'''
from functools import reduce

def main():
    number_file = input("Enter the name of the txt file (ex: name.txt): ")
    with open(number_file, 'r') as file:
        for line in file:
            fields = line.split(' ')
            data = list(map(int, fields))
    print(calcAverage(data))


def calcAverage(nums): 
    numSum = 0
    count = 0
    for i in nums:
        count += 1
        numSum = reduce(lambda x,y : x+y, nums)
    return round(numSum / count, 2)

if __name__ == '__main__':
    main()