# Uses python3
import sys
from random import randint, sample
from math import floor


##  =============================================================================================================================  ##



def binary_search(a,left,right,x):
    
    mid = floor(left + (right - left) / 2)
    
    if left > right:
        return -1
    
    if (x == a[mid]):
        return mid
    elif (x > a[mid]):
        return binary_search(a,mid+1,right,x)
    elif (x < a[mid]):
        return binary_search(a,left,mid-1,x)
    
   
    
    



##  =============================================================================================================================  ##






def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1




##  =============================================================================================================================  ##



if __name__ == '__main__':
    '''
    data = list(map(int, input().split(" ")))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,0,len(a)-1,x), end = ' ')
        
    '''
    
    
    n = randint(10000000,20000000)
    m = randint(3000, 4000)
    
    a = sample(range(1000,2000000000), k = n)
    arr = sorted(a)
    sArr = sample(range(100,20000000), k = m)
    
    for x in sArr:
        print(binary_search(arr,0,len(arr)-1,x))
        
        
##  =============================================================================================================================  ##





                              #################################################################
                              ########################  Stress Testing  #######################
                              #################################################################
                              
'''                              
                              
while(True):

    n = randint(10000,10010)
    arr = [randint(10000, 150000) for x in range(n)]
    
    arr = sorted(list(set(arr)))
    x = randint(0,12)
    
    result1 = linear_search(arr,x)
    result2 = binary_search(arr,0,len(arr)-1,x)
    
    
    if (result1 == result2):
        print("OK")
    elif (result1 != result2):
        print("array =>", arr)
        print("key =>", x)
        print("WRONG ANSWER", result1, result2, sep = '\t')
        break 
    
'''    
