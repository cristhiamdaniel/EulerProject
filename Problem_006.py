'''
Sum square difference

function to Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, n+1):
        sum_of_squares += i*i
        square_of_sum += i
    square_of_sum *= square_of_sum
    return square_of_sum - sum_of_squares

def main():
    print(sum_square_difference(100))

if __name__ == '__main__':
    main()