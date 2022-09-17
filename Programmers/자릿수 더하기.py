def solution(n):
    answer = 0
    
    n = str(n)
    
    lst = list(n)
    lst = list(map(int, lst))
    
    for i in lst:
        answer += i


    return answer