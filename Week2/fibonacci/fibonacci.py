# Uses python3

from random import randint

# calculates nth fibonacci number
# using recursion
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# calculates nth fibonacci number
# using array
def calc_fib_fast(n):
    if (n == 0 or n == 1):
        return(n)
    elif (n > 1):
        fibonacci = [0] * (n+1)
        fibonacci[0] = 0
        fibonacci[1] = 1

        for i in range(2,n+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

        return(fibonacci[n])


n = int(input())
print(calc_fib_fast(n))
