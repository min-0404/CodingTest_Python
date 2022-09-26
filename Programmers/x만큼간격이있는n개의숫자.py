def solution(x, n):
    
    answer = []
    cnt = 1
    
    while cnt <= n:
        growth = x * cnt
        answer.append(growth)
        cnt +=  1
    
    return answer