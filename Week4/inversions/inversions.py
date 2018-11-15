# Uses python3
import sys
import random
from math import floor


##====================================================================================##

                ##################################################
                #####  Number of inversions Naive Algorithm  #####
                #####        Time complexity => O(n^2)       #####
                ##################################################       


def get_number_of_inversions(a):
    
    count = 0
    
    for i in range(len(a)-1):
        for j in range(1,len(a)):
            if (i < j and a[i] > a[j] ):
                count += 1
                
    return count
    

##====================================================================================##

                      ##################################
                      #####  Number of inversions  #####
                      ##################################
                      
                 
                      
## The below function calculates the number of inversions in an array. It uses modified
## merge sort algorithm. Merge procedure return the sorted array and number of pairs
## (l,r) such that l=>L and r=>R, and l > r. MergeSort return sorted array and number 
## of inversions.


                                                    

def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L,R = [],[]
    
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+j+1])

           
           
    i,j = 0,0
    
    #print(L,R)
    
    count = 0
       
    for k in range(p,r+1):
        if i >= n1:
            A[k] = R[j]
            j += 1
        elif j >= n2:
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        elif L[i] > R[j]:
            A[k] = R[j]
            count += len(L) - i
            j += 1
            
            
    return(count)


##====================================================================================##
   
                     #############################################
                     #######       Merge sort algorithm    #######
                     ####### Time complexity => O(nlog(n)) #######
                     #############################################
                     
                     
                     
def MergeSort(A,p,r):
     
    # variable to store count of inversions
    inversions = 0
     
    # base case
    if p >= r:
        return (0)
    
    q = (p+r) // 2
    
    inversions += MergeSort(A,p,q)
    inversions += MergeSort(A,q+1,r)
    inversions += Merge(A,p,q,r)
    
    return(inversions)
    


##====================================================================================##
'''
if __name__ == '__main__':
    a = list(map(int, input().split(" ")))
    #b = n * [0]
    p = 0
    r = len(a)-1
    q = floor((p + r)/2)
    print(MergeSort(a,p,r))
'''

##====================================================================================##

                             ############################
                             #####  Stress Testing  #####
                             ############################
                             
                             
while(True):

    n = random.randint(90000,100000)
    
    a1 = [random.randint(1000000000,2000000000) for i in range(n)]
    
    '''
    a2 = a1[:]
    p,r = 0,len(a1)-1
    
    res1 = MergeSort(a1,p,r)
    res2 = get_number_of_inversions(a2)
    
    
    if (res1 != res2):
        print("Wrong Answer", a,res1,res2,sep = ' ')
        break
    else:
        print("OK")
    '''
    
    res1 = MergeSort(a1,0,len(a1)-1)
    
    print("OK")
    break
