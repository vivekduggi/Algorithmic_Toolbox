# Uses python3




from random import randint




#### =========================================================================================================== ####
#### =========================================================================================================== ####
#### =========================================================================================================== ####



# Naive greedy algorithm, time complexity O(n^2)

def get_optimal_value_naive(capacity, weights, values):
    
    
    value = 0.
    valueVect = []

    for i in range(len(weights)):    
        
        if capacity == 0:
            return value
        
        max = 0
        j_max = -1

        # Select i with w(i) > 0 and max(v(i)/w(i))
        for j in range(len(weights)):
            if (weights[j] > 0 and values[j] > 0):
                unit_val = values[j] / weights[j]
                print(unit_val)
                if (unit_val >= max):
                    max = unit_val
                    j_max = j
                    
                                  
        v = min(weights[j_max], capacity)
        valueVect.append(v)
        value += v * max
        weights[j_max] -= v
        capacity -= v
        
    
    

    
    return(value)




#### ============================================================================================================ ####
#### ============================================================================================================ ####
#### ============================================================================================================ ####




# Greedy algorithm with time complexity O(nlogn)
# Uses a sorting algorithm to sort values of 
# values[i] / weights[i], maximum to minimum

def get_optimal_value_fast(capacity, weights, values):

    value = 0.
    valueVect = [0] * len(weights)
   

 
    # loot_matrix stores a tuple of values[i], weights[i] and 
    # values[i] / weights[i]
   
    loot_matrix = []




    # Loot matrix is a list of  tuples of values, weights and their corresponding
    # values / weights ratio. If weights[i] == 0 or values[i] == 0, then that item
    # is skipped.

    for i in range(len(weights)):
         if (weights[i] > 0 and values[i] > 0) :
             loot_matrix.append([values[i],weights[i],values[i] / weights[i]])
    
    


    if (len(loot_matrix) == 0):
        return value

      
    
    # Sorting loot_matrix based on values[i] / weights[i],
    # from maximum to minimum.

    loot_matrix = sorted(loot_matrix, key = lambda x:x[2], reverse = True)
    
    


        
    for i in range(len(loot_matrix)):

         if capacity == 0:
            return value


         max = 0
         


         # Select i with weights[i] > 0 and max values[i] / weights[i] 
         # here i_max is equal to i.

         if (loot_matrix[i][1] > 0):
             
             max  = loot_matrix[i][2]
             

             # variable "minWeight" holds the weight that can be put into the knapsack if weight of the item 
             # is greater than capacity of the knapsack then then part of loot chosen whose weight is 
             # equal to the capacity of knapsack, i.e, it fills knapsack completely, with some portion of
             # it still remaining, otherwise whole quantity of the item is filled in the knapsack.

             minWeight = min(loot_matrix[i][1], capacity)
             valueVect[i] = minWeight
             value += minWeight * max
             loot_matrix[i][1] -= minWeight
             capacity -= minWeight
             
         elif (loot_matrix[i][1] == 0):
         
             continue;
              
          

         
       
        
    return(value)




#### ============================================================================================================ ####
#### ============================================================================================================ ####
#### ============================================================================================================ ####





data = list(map(int, input().split(" ")))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value_fast(capacity, weights, values)


print("{:.10f}".format(opt_value))




#### ============================================================================================================ ####
#### ============================================================================================================ ####
#### ============================================================================================================ ####



#### -----------------------------------------------  NOTE  ----------------------------------------------------- ####


# Remember that change made is a variable by a function is not reflected back in the original values, but if an 
# array is passed it is passed by reference and thus all the changes made by the function is reflected back in
# the original array, or in case of python a "list". Always remember that, when performing stress testing.





                 ################################################################################
                 ##############################   Stress testing   ##############################
                 ################################################################################



'''
while(True):

    n = randint(1,8)
    capacity = randint(10,30)
    values1 = [randint(0,20) for i in range(n)]
    weights1 = [randint(0,10) for i in range(n)]

    values2 = values1
    weights2 = weights1

    print(n,capacity,values1,weights1,sep=' ')

    
    res1 = "{:.2f}".format(get_optimal_value_naive(capacity, weights1, values1))
    res2 = "{:.2f}".format(get_optimal_value_fast(capacity, weights2, values2))


     

    if res1 == res2:
        print("OK")
    else:
        print("WRONG ANSWER", res1,res2,sep=' ')
        break

'''





