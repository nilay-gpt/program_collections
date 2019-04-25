"""
Given N buckets, each containing A[i] items. Given K tours within which all of the items are needed to be delivered. It is allowed to take items from only one bucket in 1 tour. The task is to tell the minimum number of items needed to be delivered per tour so that all of the items can be delivered within K tours.
Conditions : K >= N 
Examples:

Input : 
N = 5
A[] = { 1, 3, 5, 7, 9 }
K = 10
Output : 3
By delivering 3 items at a time, 
Number of tours required for bucket 1 = 1
Number of tours required for bucket 2 = 1
Number of tours required for bucket 3 = 2
Number of tours required for bucket 4 = 3
Number of tours required for bucket 5 = 3
Total number of tours = 10
"""

def getMin(N, A, k): 
  
    # Iterating through each possible  
    # value of minimum Items

    for i in range(1, max(A)+1): 
        tours = 0
        for j in range(0, len(A)): 
            if(A[j]% i == 0):# Perfectly Divisible 
                tours += A[j]/i 
  
            else: 
                # Not Perfectly Divisible means required 
                # tours are Floor Division + 1 
                tours += A[j]//i + 1 
  
        if(tours <= k): 
            # Return First Feasible Value found, 
            # since it is also the minimum 
            return i  
    return "Not Possible"
  

if __name__ == "__main__":
    # Driver Code 
    N = 5
    A = [1, 3, 5, 7, 9] 
    k = 10
    print getMin(N, A, k)
