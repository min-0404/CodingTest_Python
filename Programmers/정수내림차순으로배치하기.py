def solution(n):
    
    n = str(n)
    lst = list(n)
    lst = list(map(int, lst))
    lst.sort(reverse = True)
    answer = ''
    for i in lst:
        answer += str(i)

    return int(answer)