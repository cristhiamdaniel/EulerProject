'''
A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is
101101 = 143 * 707

Find the largest palindrome made from the product of two 3-digit numbers which is less than N

Input format
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
1 <= T <= 1000
101101 < N < 1000000

Output format
Print the value corresponding to each test case.

Sample Input 0
2
101110
800000

Sample Output 0

101101
793397


'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

'''
def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        max = 0
        for i in range(100, 1000):
            for j in range(100, 1000):
                p = i * j
                if p < n and p > max and is_palindrome(p):
                    max = p
        print(max)
'''

'''
def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        max_palindrome = 0

        # Check all 6-digit palindrome numbers
        for i in range(100000, n):
            if is_palindrome(i):
                # Check if it's the product of two 3-digit numbers
                for j in range(100, 1000):
                    if i % j == 0 and i // j < 1000:
                        max_palindrome = max(max_palindrome, i)
                        break

        print(max_palindrome)
'''

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        max_palindrome = 0
        for i in range(n - 1, 101000, -1):
            if is_palindrome(i):
                for j in range(999, 99, -1):
                    if i % j == 0 and i // j >= 100 and i // j < 1000:
                        max_palindrome = i
                        break
                if max_palindrome:
                    break
        print(max_palindrome)

if __name__ == '__main__':
    main()

'''
La complejidad temporal del primer main() es O(T * 10^3 * 10^3), ya que hay dos bucles anidados que recorren todos los números de 3 dígitos, y para cada par de números se verifica si su producto es un palíndromo y si es menor que el límite especificado en cada caso de prueba.

La complejidad temporal del segundo main() es O(T * 10^6 + T * 10^3 * 10^3), ya que hay un bucle que recorre todos los números de 6 dígitos, y para cada uno se verifica si es un palíndromo y luego se buscan sus posibles factores de 3 dígitos.

La complejidad temporal del tercer main() es O(T * (n-101000) + T * 10^3 ), Ya que se recorre solo los palindromos entre n y 101000, y además se recorre solo un subconjunto de posibles factores de 3 dígitos.

Ten en cuenta que estas complejidades son aproximadas y pueden variar dependiendo de las implementaciones específicas del algoritmo y de los inputs proporcionados.
'''