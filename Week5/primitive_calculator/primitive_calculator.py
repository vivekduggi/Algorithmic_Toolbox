# Uses python3
import random


##============================================================##

                #######################################
                ########   Greedy Solution    #########
                ######  Time Complexity => O(n)  ######
                #######################################



## This is a greedy solution to the primitive algorithm
## problem. It is incorrect


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


##============================================================##


          ################################################
          ########  Dynamic Programming Solution  ########
          ##########  Time Complexity => O(n)  ###########
          ################################################


## Step 1 -> Take an array "steps" of length n+1 and initialise
##           the first two elements with zeros, and all the other
##           elements with float("Inf").

## Step 2 -> Take another array "sequence" and initialise, it 
##           will be used to store the sequence in which operation
##           proceed.

## Step 3 -> Fill the array "steps" with the minimum number of
##           operations to be performed to reach ith number

## Step 4 -> Backtrack the sequence of intermediate numbers and
##           fill array "sequence" with it.



def optimal_sequenceDP(n):
	steps = [0]*2
	steps.extend([float("Inf")] * (n-1))

	sequence = []


	# Filling the steps array

	for i in range(2,n+1):
		if (i % 6 == 0):
			steps[i] = min(steps[i // 3], steps[i // 2],
				           steps[i - 1]) + 1
		elif (i % 3 == 0):
			steps[i] = min(steps[i // 3], steps[i - 1]) + 1
		elif (i % 2 == 0):
			steps[i] = min(steps[i // 2], steps[i - 1]) + 1
		else:
			steps[i] = steps[i-1] + 1

	#return(steps[n])


	# Backtracking the sequence of intermediate numbers

	while (n >= 1):
		sequence.append(n)

		if (n % 6 == 0):
			[_,n] = min([steps[n//3],n//3], [steps[n//2],n//2],
				        [steps[n-1],n-1], key = lambda x: x[0])
		elif (n % 3 == 0):
			[_,n] = min([steps[n//3],n//3], [steps[n-1],n-1],
				        key = lambda x:x[0])
		elif (n % 2 == 0):
			[_,n] = min([steps[n//2],n//2], [steps[n-1],n-1])
		else:
			[_,n] = [steps[n-1],n-1]

	return(sequence[::-1]) 


##============================================================##


n = int(input())
print(*optimal_sequenceDP(n), end = " ")

##============================================================##