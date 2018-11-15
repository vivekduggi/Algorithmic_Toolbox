#Uses python3



from random import randint


## ================================================================================================================== ##


# Greedy algorithm. It sorts both the arrays in descending order then takes the product
# of max elements in both the arrays iteratively.

def max_dot_product(a, b):
    

    # Sorting both the arrays in descending order

    a.sort(reverse = True)
    b.sort(reverse = True)
    
    max_product_sum = 0

    
    for i in range(len(a)):
        max_product_sum += a[i] * b[i]
        
            
    return(max_product_sum)

## ================================================================================================================== ##



data = list(map(int, input().split(" ")))
n = data[0]
a = data[1:(n + 1)]
b = data[(n + 1):]
print(max_dot_product(a, b))
    
