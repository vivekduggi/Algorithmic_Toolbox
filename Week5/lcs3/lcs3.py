#Uses python3

import pprint
import random


##-----------------------------------------------------------------##


              #############################################
              #######  Longest Subsequence Problem  #######
              #######       Recursive Solution      #######
              #######   Time Complexity => O(4^n)   #######
              #############################################



## This is a recursive implementation for the "Longest Subsequence
## Problem".
## Time Complexity => O(4^n)


## Step 1 -> Base case: If any of the indices becomes zero, i.e, 
##           length of the substring becomes 0, then return 0.
## Step 2 -> Recursive case: Check for the equality of element at
##           the index i,j, cases are as follows:
##           If equal: add 1 to the return value,
##           and check if it is less than or equal to min(i,j),
##           if TRUE return 1 + ans, else return ans
##           If not equal : return ans.
##           Note that the the maximum possible length of the
##           substring cannot be greater than the length of smaller
##           of two strings being compared



def lcs_recursive(a,b,c,i,j,k):


	# Base case:
	# returns 0 if any of the index becomes 0
	# If length of any of the sub string is less than or
	# equals 0, return 0.
	if (i < 0 or j < 0 or k < 0):
		return 0
	# Recursive case:
	# If none of the substrings are NULL, then add 1 to the
	# returned value of subproblem, and check whether it is
	# equal to or less than the length of smallest substring,
	# if TRUE keep the ans and return it, else, return the 
	# original ans of the subproblem.
	else:
		ans = max(lcs_recursive(a,b,c,i-1,j,k),
			      lcs_recursive(a,b,c,i,j-1,k),
			      lcs_recursive(a,b,c,i,j,k-1),
			      lcs_recursive(a,b,c,i-1,j-1,k-1))

        # Checking whether the length of common subsequence
        # is less than or equal to the length of smallest
        # string.
		if ((1+ans) <= min(i,j,k)+1 and (a[i] == b[j] == c[k])):
			return (1+ans)
		else:
			return (ans)

	

	


##-----------------------------------------------------------------##



               ############################################
               #######  Longest Subsequence Problem  ######
               #######   Time Complexity =>          ######
               ############################################


## This is the algorithm for computing the length of common sub-
## -sequence for three sequences.

## Input ->  Integers n,m,l, and sequences of length n,m,l
##           respectively.
## Output -> Non-negative integer p denoting length of common
##           subsequence.


## Below is the algorithm to compute the length of common
## subsequence for three given sequences, it employs dynamic
## programming.


## Steps:
## Step 1 -> Create a 3-D matrix with length = i, breadth = j,
##           depth = k. 
## Step 2 -> All the elements with 0 index either for length, 
##           breadth or height or all, is filled with 0.
## Step 3 -> Create a loop to fill the 3-D matrix, following 
##           rules are to be followed in order to fill the matrix.
## Step 4 -> To fill element mat[i][j][k], first find the max
##           value among mat[i-1][j][k], mat[i][j-1][k],
##           mat[i][j][k-1], mat[i-1][j-1][k-1].
## Step 5 -> If a[i] = b[j] = c[k], add 1 to the max value
##           obtained above, and check whether the new value
##           is less than or equal to the min(i,j,k).
## Step 6 -> IF TRUE, fill the mat[i][j][k] with the new value
##           else, fill mat[i][j][k] with unchanged max value.

def lcs3(a, b, c, n, m, l):

	# 3-D matrix to store longest subsequence for
	# each combinations of arrays
	mat = [[[0 for x in range(l+1)] for y in range(m+1)] 
	         for z in range(n+1)]

	#pprint.pprint(mat)

	
	# Loop to fill our 3-D matrix
	for i in range(1,n+1):
		for j in range(1,m+1):
			for k in range(1,l+1):
				maxVal = max(mat[i-1][j][k],mat[i][j-1][k],
					         mat[i][j][k-1],mat[i-1][j-1][k-1])
				#print(maxVal,a[i-1],b[j-1],c[k-1],end=' ')
				if (a[i-1] == b[j-1] == c[k-1]):
					#print("Yes")
					if (1+maxVal <= min(i,j,k)):
						mat[i][j][k] = 1+maxVal
						#print("inc",1+maxVal)
					else:
						mat[i][j][k] = maxVal
				else:
					#print("No")
					mat[i][j][k] = maxVal


	#pprint.pprint(mat)



	return mat[n][m][l]



##-----------------------------------------------------------------##

'''

if __name__ == '__main__':
    n,*a = list(map(int, input().split(" ")))
    m,*b = list(map(int, input().split(" ")))
    l,*c = list(map(int, input().split(" ")))
    
    #print(a,b,c,end = '\n')
    print(lcs3(a,b,c,n,m,l))

'''

##-----------------------------------------------------------------##


                 ####################################
                 #########  Stress Testing  #########
                 ####################################


while(True):
	n = random.randint(90,100)
	m = random.randint(90,100)
	l = random.randint(90,100)

	a = [random.randint(-118,-108) for i in range(n)]
	b = [random.randint(-118,-108) for i in range(m)]
	c = [random.randint(-118,-108) for i in range(l)]

	print(lcs3(a,b,c,n,m,l))

	break


	'''

	res1 = lcs_recursive(a,b,c,n-1,m-1,l-1)
	res2 = lcs3(a,b,c,n,m,l)

	if (res1 == res2):
		print("OK")
	else:
		print("Wrong Answer", res1, res2, sep = '\t')
		break

	'''

	


##-----------------------------------------------------------------##