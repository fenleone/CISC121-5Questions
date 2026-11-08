def solution(A):
    total_sum = sum(A)
    
    left_sum = 0
    min_diff = None 
    #Loop through each possible split point P (from index 1 up to len(A) - 1)
    for p in range(1, len(A)):
        left_sum += A[p - 1]
        
        right_sum = total_sum - left_sum
        
        diff = abs(left_sum - right_sum)
        
        if min_diff is None or diff < min_diff:
            min_diff = diff
            
    return min_diff

A = [3, 1, 2, 4, 3]
print(solution(A))  #output 1
