# Uses python3


##-------------------------------------------------------------------##


                 ########################################
                 ########   Placing parantheses  ########
                 ###### Time Complexity => O(n^3) #######
                 ########################################


## Input -> String S, of length 2n+1 for some n, with symbols s(0),
##          s(1),s(2),.....,s(2n). Symbol at even position of S is a
##          digit, symbol at odd position is one of three operations
##          {+,-,*}.
## Output -> Maximum possible value of arithmetic expression.


## Function used ==>> 
## 
## 1. evalt() - It performs the given operation on an expression.
## 
## 2. MinAndMax() - It calculates the maximum and minimum value for
##                  a sub-expression.
##
## 3. get_maximum_value() - It calculates the maximum possible value
##                          for an expression by reordering, 
##                          parantheses.  

## Steps involved ==>>
## 
## Step 1 -> Initialise two square matrices of length n, "m" and "M".
## Step 2 -> Fill diagnol elements of both the matrices with the their
##           respective digit in the "digits" array. 
## Step 3 -> Define a function MinAndMax() which evaluates the minimum
##           and maximum value of a an expression based on minimum and
##           maximum values of its subexpressions, by placing the
##           parantheses in different order. The fucntion returns, 
##           minimum and maximum value for a subexpression.
## Step 4 -> Define a function get_maximum_value() which chooses,
##           the subexpressions from the given input, in order of
##           increasing size, and passes it to the MinAndMax().
## Step 5 -> The minimum and maximum value returned by the MinAndMax(),
##           is used to fill the "m" and "M" matrices.
## Step 6 -> Elements below the diagnols in both the matrices is are 0,
##           the last element in topmost row of both the matrices m and M
##           contain minimum and maximum value for the subexpression,
##           respectively.




## Function to perform given operation on an expression                
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False






## Function to calculate minimum and maximum value for an expression.
## The function returns a list whose first value is the minimum value,
## and the second value is a maximum value.
def MinAndMax(i,j,digits,operators,M,m):

    minVal = float("Inf")
    maxVal = -float("Inf")

    #Loop to calculate the minimum and maximum value for
    #a given subexpression
    for k in range(i,j):
        a = evalt(M[i][k],M[k+1][j],operators[k])
        b = evalt(M[i][k],m[k+1][j],operators[k])
        c = evalt(m[i][k],M[k+1][j],operators[k])
        d = evalt(m[i][k],m[k+1][j],operators[k])


        minVal = min(minVal,a,b,c,d)
        maxVal = max(maxVal,a,b,c,d)


    return ([minVal,maxVal])






## Function to get maximum value using dynamic programming.
def get_maximum_value(digits, operators):

    n = len(digits)

    #Initialising min and max matrices
    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]

    #Filling diagnol elements with corresponding elements in
    #"digits" list.
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]



    #Loop to calculate the maximum value of an expression
    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            m[i][j],M[i][j] = MinAndMax(i,j,digits,operators,M,m)

    '''
    for rows in m:
        print(*rows,end=' ')
        print('\n')
    for rows in M:
        print(*rows,end=' ')
        print('\n')
    '''

    return (M[0][n-1])
    




##-------------------------------------------------------------------##





if __name__ == "__main__":
    expression = list(input())
    digits = [int(x) for x in expression[0:len(expression)+1:2]]
    operators = expression[1:len(expression)+1:2]
    print(get_maximum_value(digits,operators))




##-------------------------------------------------------------------##