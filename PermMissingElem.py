def solution(A):
    N = len(A)
    max_num = N + 1
    expected_sum = max_num * (max_num + 1) // 2
    actual_sum = sum(A)
    
    return expected_sum - actual_sum


A = [2, 3, 1, 5]
print(solution(A))
