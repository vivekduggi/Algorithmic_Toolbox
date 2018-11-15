# Uses python3


from random import randint


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10




# function to calculate nth Fibonacci number

def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return (current)



# pisano period for n = 10 is 60
# sum of first n Fibonacci numbers : F(0)+F(1)+F(2)+.....+F(n) = F(n+2) - F(2)
# sum of Fibonacci numbers from m to n terms : F(m)+F(m+1)+....+F(n) = F(n+2)-F(m+2)+F(m)

def fibonacci_partial_sum_fast(m,n):

    ind1 = (m+2) % 60
    ind2 = (n+2) % 60

    if (m > 60):
        m = m % 60
    
    A = calc_fib(ind2) % 10
    B = calc_fib(ind1) % 10
    C = calc_fib(m) % 10

   
    partial_sum = (A - B + C) % 10
        

    return (partial_sum)



m,n = sorted([randint(10**17,10**18), randint(10**17,10**18)])

print(fibonacci_partial_sum_fast(m,n))


'''
# implementing stress testing

while(True):
 
    m,n = sorted([randint(50000,50010), randint(50000,50010)])

    print(m,n,sep=' ')

    res1 = fibonacci_partial_sum_naive(m,n)
    res2 = fibonacci_partial_sum_fast(m,n)

    if (res1 != res2):
        print("Wrong Answer", res1,res2,sep='\t')
        break
    else:
        print("OK")
'''

