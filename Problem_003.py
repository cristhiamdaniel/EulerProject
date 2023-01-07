"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def factor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n

def main():
    n = 600851475143
    while True:
        f = factor(n)
        if f == n:
            print(n)
            break
        n //= f

if __name__ == '__main__':
    main()