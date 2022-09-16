def solution(n):
    
    # 아리스토체 알고리즘 활용
    lst = [True for _ in range(n+1)]
    lst[0] = False
    lst[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if lst[i]: 
            for j in range(i+i, n + 1, i): # 배수들을 모두 False로 만들어버림
                lst[j] = False
    
    # 소수 개수 세기
    cnt = 0
    for i in lst:
        if i == True:
            cnt += 1

    return cnt