X = 10
Y = 300
D = 30


def solution(X, Y, D):
    jumps = 0
    position = X
    while position<Y:
        position+=D
        jumps+=1
    return jumps

print(solution(X, Y, D))
