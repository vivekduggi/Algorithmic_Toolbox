import random
import math


##===========================================================================##

                   #########################################
                   #####  Distance bewteen two points  #####
                   #########################################


## This is the function to calculate "euclidean" distance between two points.


def euclideanDistance(a,b):

	squaredDistance = (a[0]-b[0])**2 + (a[1]-b[1])**2
	dist = math.sqrt(squaredDistance)

	return (float(dist))


##===========================================================================##

                    ############################
                    #####  Closest points  #####
                    ############################


## This is function to calculate minimum distance between pair of points
## Time complexity => O(n^2)

def minimum_distance_naive(a):
	min = float("Inf")
	for i in range(len(a)-1):
		for j in range(i+1,len(a)):
			distance = euclideanDistance(a[i],a[j])
			if distance <= min:
				min = distance
				ind = [a[i],a[j]]
				
	return min


##===========================================================================##

                #########################################       
                #####  Closest point fast algorithm #####
                #########################################


## Algorithm uses "Divide and Conquer" approach to find closest point
## Time complexity => O(nlogn)

## Step 1: Sorting the array first by x in increasing order, and them the, sub-
## -array with equal x, by y in increasing order.
## Time complexity => O(nlogn)

## Step 2: Base case, i.e, when there is only one element, return "infinity".

## Step 3: Recursive case, first find the minimum value between the smallest
## distance in left half and right half.

## Step 4: Merge case, There may be elements, p and q such that, p ∈ left half
## and q ∈ right half, and the distance between them may be less than the 
## previously calculated distance. So we select points from left half and append
## them in array "closest_pair1" and from right half and append them in array 
## "closest_pair2". This is found by using technique mentioned in the link
## "https://www.cs.ucsb.edu/~suri/cs235/ClosestPair.pdf".
## Time complexity => O(6*(n/2)) = O(3n)



def minimum_distance_fast(a,left,right):
	if left >= right:
		return(float("Inf"))

	mid = math.floor((left+right)/2)
	d1 = minimum_distance_fast(a,left,mid)
	d2 = minimum_distance_fast(a,mid+1,right)
	
	d_min = min(d1,d2)
	closest_pair1 = []
	closest_pair2 = []
	
	for i in range(left,mid+1):
		if a[mid][0] - a[i][0] <= d_min:
			closest_pair1.append(a[i])
	for j in range(mid+1,right+1):
		if a[j][0] - a[mid][0] <= d_min:
			closest_pair2.append(a[j])
	
	for p1 in closest_pair1:
		for p2 in closest_pair2:
			count = 0
			if (abs(p1[1] - p2[1]) <= d_min):
				distance = euclideanDistance(p1,p2)
				d_min = min(d_min,distance)
			elif count >= 6:
				break
	
	return(d_min)




##===========================================================================##
'''
if __name__ == '__main__':
	n = int(input())
	arr = list(map(int,input().split(" ")))
	x = arr[0:2*n-1:2]
	y = arr[1:2*n:2]
	a = list(zip(x,y))
	a = sorted(a,key = lambda x:(x[0],x[1]))
	print(a)
	print(minimum_distance_fast(a,0,n-1))
'''

##===========================================================================##

                      ############################
                      #####  Stress Testing  #####
                      ############################


while(True):
	n = random.randint(200,300)
	x = [random.randint(-500,-15) for _ in range(n)]
	y = [random.randint(-15,500) for _ in range(n)]
	a = list(zip(x,y))
	a = sorted(a, key = lambda x:(x[0],x[1]))
	
	r1 = minimum_distance_naive(a)
	r2 = minimum_distance_fast(a,0,n-1)

	res1 = round(r1,5)
	res2 = round(r2,5)

	if res1 != res2:
		print("Wrong Answer", a,res1,res2)
		break
	else:
		print("OK")
	
