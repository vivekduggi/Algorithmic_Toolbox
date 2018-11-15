#Uses python3

from itertools import permutations
from random import randint


## ================================================================================================================ ##


## Naive algorithm complexity > O(n!), uses "Python's" string concatenating abilities
## First convert number to string, adds and then converts it back to int.
## Time complexity => O(n*n!)

def largest_number_naive(a):
    
    salary = []
    indices = []
    permute = permutations(list(range(len(a))))
    
    for p in permute:
        indices.append(p)

    for i in indices:
        number = int(''.join(str(a[x]) for x in i))
        salary.append(number)    
   
    

    return(max(salary))
     


## ================================================================================================================ ##


## Given two digits, this function checks, which of them has greater value at the "leftmost place"
## Uses "math" module

def isGreaterOrEqual(x,y):
    
    if (y == -float("Inf")):
        return True
    
    x = str(x)
    y = str(y)
    
    a = x + y
    b = y + x
    
    
    
    if (int(a) >= int(b)):
        return True
    else:
        return False    





## ================================================================================================================ ##


## Greedy algorithm
## Time complexity => O(n^2)

def largest_number_greedy(a):

    answer = []
    
    while (len(a) > 0):
        maxDigit = -float("Inf")
        for i in range(len(a)):
            if (isGreaterOrEqual(a[i], maxDigit)):
                i_max = i
                maxDigit = a[i]
            else:
                continue
  
        answer.append(maxDigit)
        a.pop(i_max)
    
    return(answer)


## ================================================================================================================ ##


n = 1000
a = [randint(990,1000) for i in range(n)]
print(''.join(str(x) for x in largest_number_greedy(a)))

    
## ================================================================================================================ ##


                                      ######################################
                                      ########### Stress Testing ###########
                                      ######################################
                                      
                                      

'''
while(True):

    n = randint(100,200)
    data = [randint(500,590) for i in range(n)]
    
    
    res1 = largest_number_naive(data)
    res2 = int(''.join(str(x) for x in largest_number_greedy(data)))
    
    
    if (res1 == res2):
        print("OK")
    else:
        print("Wrong Answer", res1, res2, sep = '\t')
    
'''
