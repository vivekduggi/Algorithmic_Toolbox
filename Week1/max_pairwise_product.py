# Uses Python3


a = list(map(int,input().split(" ")))


def max_pairwise_product(arr):
    max = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(a)):
            product = arr[i] * arr[j]
            if (product >= max):
                max = product
    return max

print(max_pairwise_product(a))

