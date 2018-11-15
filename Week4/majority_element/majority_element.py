# Uses python3
import sys
from random import randint
from math import floor


##====================================================================================##



# Naive algorithm for finding majority element
# Time complexity => O(n^2)

def get_majority_element_naive(a):
    
    for i in range(len(a)):
        curr = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == curr:
                count += 1
        
        if count > (len(a)/2):
            return (1)
    return (-1)


##====================================================================================##




        #########################################################################
        ####### Divide and Conquer algorithm for finding majority element #######
        #######                Time complexity => O(n*logn)               #######
        #########################################################################



# Function to find whether list contains majority element or not

def get_majority_element_fast(a, left, right):
     
    if left == right:
        return ([1,a[left]])
    else:
        mid = floor(left + (right-left)/2)
        a_left = a[left:mid+1]
        a_right = a[mid+1:]
        [_,L] = get_majority_element_fast(a_left,0,len(a_left)-1)
        [_,R] = get_majority_element_fast(a_right,0,len(a_right)-1)
        
        
        if (a.count(L) > len(a)/2):
            return ([1,L])
        elif (a.count(R) > len(a)/2):
            return ([1,R])
        else:
            return ([-1,-1])
            



##====================================================================================##























##====================================================================================##




'''

if __name__ == '__main__':
    n, *a = list(map(int, input().split(" ")))
    if get_majority_element_naive(a) != -1:
        
        print(1)
    else:
        print(0)
        
'''

##====================================================================================##


                     ####################################
                     #########  Stress Testing  #########
                     ####################################
                     
                     
                     
                     
while(True):
    n = randint(99999,100000)
    a = [randint(8000000000,9000000000) for i in range(n)]
    
    
    
    if get_majority_element_fast(a,0,len(a)-1)[0] != -1:
        res1 = 1
    else:
        res1 = 0
        
        
    print(res1)
     
    break   
    '''
    
    if get_majority_element_naive(a) != -1:
        res2 = 1
    else:
        res2 = 0
        
        
    
    if (res1 != res2):
        print("Wrong Answer", res1,res2,sep = '\t')
        break
    else:
        print("OK")
        
    '''
