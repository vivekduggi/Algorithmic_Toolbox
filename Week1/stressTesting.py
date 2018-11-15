# Uses python 3

from random import randint


# function to calculate maximum product
# time complexity = O(n)

def max_pairwise_product_fast(arr):


    maxIndex1 = -1
    maxIndex2 = -1

    for i in range(len(arr)):
        if (maxIndex1 == -1 or arr[i] >= arr[maxIndex1]):
            maxIndex1 = i



    for j in range(len(arr)):
        if ((j != maxIndex1) and ((maxIndex2 == -1) or (arr[j] >= arr[maxIndex2]))):
            maxIndex2 = j

    print(maxIndex1, maxIndex1, sep='\t')

    return (arr[maxIndex1] * arr[maxIndex2])


# time complexity = O(n^2)

def max_pairwise_product(arr):
    max = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            product = arr[i] * arr[j]
            if (product >= max):
                max = product
    return max


# loop to carry out stress testing

while(True):
    n = randint(2,1000)
    print(n)

    # list to store input values
    a = []

    for _ in range(n):
        a.append(randint(0,99999))

    print(a)

    result1 = max_pairwise_product(a)
    result2 = max_pairwise_product_fast(a)

    if (result1 != result2):
        print("Wrong Answer", result1, result2, sep = '\t')
        break
    else:
        print("OK")
