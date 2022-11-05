import math

def compute_pvalue(tosses):
    n,x = 0,0
    for idx in range(len(tosses)):
        if tosses[idx] == "H":
            x += 1
        n += 1
    
    # implement factorial computation using Memoization (Dynamic programming) and not brute force Recursion
    factorials = [-1]*n
    for idx in range(n):
        if idx == 0:
            factorials[idx] = 1
        else:
            factorials[idx] = factorials[idx - 1]*(idx + 1)
        
    pvalue = (factorials[n - 1]*math.pow(0.5, x)*math.pow(0.5, n - x))/(factorials[x - 1]*factorials[n-x - 1])
    return pvalue
