'''
Smallest multiple

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

import math

def main():
    n = 20
    result = 1
    for i in range(1, n+1):
        result = math.lcm(result, i)
    print(result)

if __name__ == '__main__':
    main()




