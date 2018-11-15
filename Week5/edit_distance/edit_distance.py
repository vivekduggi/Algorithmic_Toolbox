                   

                 ###############################
                 ###  Edit distance problem  ###
                 ###############################


import random


##-------------------------------------------------------------------##


              ######################################
              ## Edit distance recursive solution ##
              ####  Time Complexity => O(3^n)   ####
              ######################################




## This is the recursive solution to edit distance problem.

## Problem Definition =>
## Edit distance between two strings is the minimum number of 
## insertion, deletions and mismatches in the alignment of two
## strings.

def edit_distance_recursive(string1, string2, m, n):

	# If the first string is empty then we'll have to insert
	# all the characters of second string in the first one.
	if (m == 0):
		return n

	# If the second string is empty then we'll have to delete
	# all the characters in the first string.
	elif (n == 0):
		return m

	# If the last characters of the two strings are identical,
	# then we ignore them and compare the remaining substring.
	elif (string1[m-1] == string2[n - 1]):
		return(edit_distance_recursive(string1, string2, m-1, n-1))

	# Else we find out which process among insertion, deletion,
	# or mismatch incurs minimum cost.
	else:
		return(1 + 
			   min(edit_distance_recursive(string1,string2,m,n-1),
			   	   edit_distance_recursive(string1,string2,m-1,n-1),
			   	   edit_distance_recursive(string1,string2,m-1,n)
			   	   )
			   )




##-------------------------------------------------------------------##


                  #######################################
                  ###           Edit Distance         ###
                  ###   Dynamic Programming Solution  ###
                  ###    Time Complexity => O(m*n)    ###
                  #######################################


## Input => Two strings of lower case letters.
## Output => Edit distance between the two strings.

## This is an algorithm for computing edit distance between two
## strings using dynamic programming.

## Time complexity => O(m*n)


## Step 1 -> Initialise a matrix of row m, and column n with 0.

## Step 2 -> Initialise the first row of the matrix with corresponding
##           column number and, first column with the corresponding
##           row number.

## Step 2 -> Compute the cost of performing folllowing 3 operations
##           insertion, deletion, mismatch, if character in both
##           the string match then the cost is 0, else 1.



def edit_distance_DP(string1, string2):

	m = len(string1)
	n = len(string2)

	# Distance matrix with (m+1) rows, and (n+1) columns
	distance = [[0 for x in range(m+1)] for y in range(n+1)]

	for i in range(m+1):
		distance[0][i] = i
	for j in range(n+1):
		distance[j][0] = j

	# Filling the distance matrix
	for i in range(1, n+1):
		for j in range(1,m+1):
			insertion = distance[i][j-1] + 1
			deletion = distance[i-1][j] + 1
			match = distance[i-1][j-1]
			mismatch = distance[i-1][j-1] + 1

			# Checking for match
			if string1[j-1] == string2[i-1]:
				distance[i][j] = min(insertion,deletion,match)
			elif string1[j-1] != string2[i-1]:
				distance[i][j] = min(insertion, deletion,mismatch)
	'''
	for rows in distance:
		print(*rows, end = " ")
		print('\n')
	'''

	return(distance[n][m])



##-------------------------------------------------------------------##


if __name__ == "__main__":
	string1 = list(input())
	string2 = list(input())
	print(string1, string2, end = " ")
	print('\n')
	print(edit_distance_DP(string1, string2))

##-------------------------------------------------------------------##
