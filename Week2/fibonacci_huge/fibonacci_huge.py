# Uses python3
import sys

from random import randint




def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# function to calculate nth fibonacci number
def calc_fib_fast(n):
    if (n == 0 or n == 1):
        return(n)
    elif (n > 1):
        fibonacci = [0] * (n+1)
        fibonacci[0] = 0
        fibonacci[1] = 1

        for i in range(2,n+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

        return (fibonacci[n])




# function to calculate pisano period
def get_pisano_period(m):
    pisano_array = []
    pisano_array.append(0)
    pisano_array.append(1)
     
    i = 0

    while(True):
        current = pisano_array[-1] + pisano_array[-2]        
 
        if (current >= m):
            current = current % m          
        
        pisano_array.append(current)

        if (pisano_array[-2] == 0 and pisano_array[-1] == 1):
            break 
        i += 1
    
    return (len(pisano_array)-2)




# function to calculate remainder
# of nth Fibonacci when divided by m
# functions used ==> get_pisano_period() and calc_fib_fast()

def get_fibonacci_huge_fast(n,m):
    
    pisano = get_pisano_period(m)

    if (pisano < n):
        i = n % pisano
        Fibonacci = calc_fib_fast(i)
        mod = Fibonacci % m
       
        return (mod)

    Fibonacci = calc_fib_fast(n)
    mod = Fibonacci % m
   
    return (mod) 
          
    

n,m = map(int,input().split(" "))

print(get_fibonacci_huge_fast(n,m))
