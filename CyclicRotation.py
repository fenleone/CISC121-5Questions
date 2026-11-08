A = [1, 2, 3, 4, 5]
K = 1

def solution(A, K):
    if len(A)==0:
        return A
    N = len(A)
    K = K%N # if k is bigger than length of a

    for e in range(K):
        last_element = A[N-1]

    for i in range(N-1, 0, -1):
        A[i] = A[i-1]

    A[0] = last_element
    
    return A

print(solution(A, K))

    

