def getIndexOfEquilibrium(arr):
    total_sum = sum(arr) # O(n)
    left_sum = 0 # O(1)
    for pos, val in enumerate(arr): # O(n)
        total_sum -= val            # O(1)
         
        if left_sum == total_sum:   # O(1)
            return pos  
        left_sum += val             # O(1)

    return -1

# O(n)