"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def main():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            if n > max and is_palindrome(n):
                max = n
    print(f"{i}*{j} = {max}")

if __name__ == '__main__':
    main()
