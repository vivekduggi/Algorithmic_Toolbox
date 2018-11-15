# Uses python3
import sys
from random import sample, randint

##======================================================================================##


                       ###########################################        
                       #####          Fast algorithm         #####
                       #####  Time complexity => O(nlog(n))  #####
                       ###########################################
                       
                       
                                              
## Step 1:             Time complexity => O(n)
## Create a dictionary in which key = points, value = number of segments with point
## on it, initialise their value with -(total number of segments)

                         
## Step 2:             Time complexity => O(nlogn)                         
## After sorting the list we need to know, whether a point is a start point, end
## point or just a point to be searched on the segment.
## We make a list of tuples where first value of tuple will be the point, and second
## value of will be denote whether the point is starting point, ending point, or
## point to be searched on the line segment => (x,a); x => start,end; a = {'l','p','r'}.
## Sort the list first in increasing order of first value in tuple and then sorting,
## lexicographically the tuple according to its second value. 


## Step 3:             Time complexity => O(n)
## Scan the sorted array of (p+2s) length from left to right and count the number of
## of starting points (x,'l'), on encountering an initial point, store the value of 
## count in a dictionary with key = initial point and value = count


## Step 4:             Time complexity => O(n)
## Again scan the array but from right to left this time, and on encountering a point
## add the count value to the value of key = point.





def fast_count_segments(starts, ends, points):
    cnt = {}
    
    for point in points:
        cnt[point] = -len(starts)
    
    
    # Creating list of tuples out of start, points and ends array
    list_tuples = []
    for i in range(len(starts)):
        list_tuples.append((starts[i],'l'))
        list_tuples.append((ends[i],'r'))
    
    for i in range(len(points)):
        list_tuples.append((points[i],'p'))

        
    # Sorting "list_tuples" in increasing order of points
    list_tuples = sorted(list_tuples, key = lambda x:(x[0],x[1]))
    

    # Counting number of segments which contain the points
    left = 0
    right = 0
    for i in range(len(list_tuples)):
        if (list_tuples[i][1] == 'l'):
            left += 1
        elif (list_tuples[i][1] == 'p'):
            cnt[list_tuples[i][0]] += left
            
    
    for i in range(len(list_tuples)-1,-1,-1):
        if (list_tuples[i][1] == 'r'):
            right += 1
        elif (list_tuples[i][1] == 'p'):
            cnt[list_tuples[i][0]] += right
    
    
    return cnt
    
##======================================================================================##

                        #######################################
                        #####        Naive Algorithm     ######
                        #####  Time complexity => O(s*p)  #####
                        #######################################
                    

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt
    
    
    
##======================================================================================##

'''
if __name__ == '__main__':
    data = list(map(int, input().split(" ")))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for point in points:
        print(cnt[point], end=' ')
        
    

starts = [2, 5, 9, 0, 7]
ends = [12, 16, 15, 15, 10]
points = [10, 6, 8]

print(fast_count_segments(starts,ends,points))
##======================================================================================##
'''
                               ############################
                               #####  Stress Testing  #####
                               ############################
                               
                               
while(True):

    m = randint(50000,55600)
    n = randint(50160,50180)
    
    starts = [randint(-100000000,0) for i in range(m)]
    ends = [randint(0,100000000) for i in range(m)]
    points = sample(range(-100000000,100000000),n)
    
    #res1 = naive_count_segments(starts,ends,points)
    dict = fast_count_segments(starts,ends,points)
    
    res = []
    for point in points:
        res.append(dict[point])
    '''    
    if res1 != res2:
        print("Wrong Answer",res1,res2,starts,ends,points)
        break
    else:
        print("OK")    
    '''
    
    print("OK")


