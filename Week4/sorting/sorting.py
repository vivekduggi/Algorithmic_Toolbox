# Uses python3
import sys
import random


##====================================================================================##

### 3 way partition, partitions array into subarrays of 
### elements less than the pivot, elements greater than
### the pivot and elements equal to the pivot



def partition3(a, l, r):
    
    
    # Shifting all the elements equal to pivot to the head of
    # list, and counting number of elements equal to pivot
    
    count = 1
    x = a[l]
    index = l+1
    
    for i in range(l+1,r+1):
        if a[i] == x:
            a[i], a[index] = a[index],a[i]
            index += 1
            count += 1
    
    
    
    # If pivot is a unique element
    
    if count == 1:
        x = a[l]
        j = l;
        for i in range(l + 1, r + 1):
            if a[i] <= x:
                j += 1
                a[i], a[j] = a[j], a[i]
        a[l], a[j] = a[j], a[l]
        m,n = j,j
        #print("unique")
        return (m,n)
    
    
    
    # If pivot is not unique element
    
    # Partitoning the list into subarray smaller than pivot
    # and subarray larger than pivot
    
    j = l + count - 1
    
    for i in range(l+count, r+1):
        if a[i] < x:
            j += 1
            a[i],a[j] = a[j],a[i]
    
    
    
    m = j
    n = j - count + 1
  
             
             
    length = j-l+1
    
    
    if (length - count <= count):
        iter = length - count
        for i in range(iter):
            a[l],a[j] = a[j],a[l]
            j -= 1
            l += 1
    else:
        iter = count
        for i in range(count):
            a[l],a[j] = a[j],a[l]
            l += 1
            j -= 1
    
    #print("not unique")
    return(m,n)
    
    

##====================================================================================##

### 2 way partition divides array into subarray of elements
### less than or equal to the pivot or greater than the pivot.

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j



##====================================================================================##


            
            #########################################################
            #####  Randomized quick sort using 3 way partition  #####
            #########################################################



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n = partition3(a, l, r)
    randomized_quick_sort(a, l, n - 1);
    randomized_quick_sort(a, m + 1, r);



##====================================================================================##



if __name__ == '__main__':
    a = list(map(int, input().split(" ")))
    randomized_quick_sort(a, 0, len(a)-1)
    for x in a:
        print(x, end=' ')
        
        

##====================================================================================##
'''
                           ############################
                           #####  Stress Testing  #####
                           ############################
                           
                           
        
while(True):
    
    n = random.randint(100000,102250)
    a = [random.randint(1000000000,1000000010) for _ in range(n)]
    
    
    res1 = sorted(a)
    
    randomized_quick_sort(a,0,len(a)-1)
    
    res2 = a
    
    if (res1 != res2):
        print("Wrong Answer", res1, res2, sep = ' ')
    else:
    
    randomized_quick_sort(a,0,len(a)-1)
    print("OK")
    
'''
