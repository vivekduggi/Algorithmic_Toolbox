# Uses python3


from random import randint


# Naive solution using recursion
def get_change_naive(m):
    coins = [1,5,10]
    if m == 0:
        return 0
    elif m < 0:
        return (float("Inf"))
    else:
        minsum = 1 + min(get_change_naive(m - c) for c in coins)
         
    return(minsum)
     

# Uses greedy algorithm
def get_change_greedy(m):
    
    # Minimum sum
    minSum = 0

    while(m > 0):

        if (m >= 10):
            m, minSum = [m % 10, minSum + (m // 10)]
        elif (m >= 5 and m < 10):
            m, minSum = [m % 5, minSum  + (m // 5)]
        elif (m < 5):
            m, minSum = [m % 1, minSum + (m // 1) ]
         
    return minSum


m = int(input())
print(get_change_greedy(m))


'''
# Performing stress testing

while(True):
     m = randint(1,20)

     res1 = get_change_naive(m)
     res2 = get_change_greedy(m)

     if (res1 == res2):
         print("OK")
     else:
         print("WRONG ANSWER", res1, res2, sep=' ')
         break

 '''
