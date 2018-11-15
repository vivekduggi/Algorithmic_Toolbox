# Uses python3

a = list(map(int,input().split(" ")))



def max_pairwise_product_fast(arr):


    maxIndex1 = -1
    maxIndex2 = -1

    for i in range(len(arr)):
        if (maxIndex1 == -1 or arr[i] >= arr[maxIndex1]):
            maxIndex1 = i



    for j in range(len(arr)):
        if ((arr[j] != arr[maxIndex1]) and ((maxIndex2 == -1) or (arr[j] >= arr[maxIndex2]))):
            maxIndex2 = j

    return (arr[maxIndex1] * arr[maxIndex2])

print(max_pairwise_product_fast(a))
