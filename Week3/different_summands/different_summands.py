# Uses python3



## ==================================================================================================================== ##



def optimal_summands(n):
    summands = []
    
    l = 1
    
    while (n > 0):
        if (n > 2*l):
            summands.append(l)
            n = n - l
            l += 1
        else:
            summands.append(n)
            n = n - n    

    return summands



## ==================================================================================================================== ##


n = int(input())
summands = optimal_summands(n)
print(len(summands))
print(sum(summands))
