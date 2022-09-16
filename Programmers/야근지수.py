# 해당 방법은 답은 맞지만 효율성 에러남
# def solution(n, works):
#     answer = 0
    
#     if n > sum(works):
#         return 0 
    
#     while n != 0:
#         x = max(works)
#         works[works.index(x)] -= 1
#         n -= 1
    
#     for i in works:
#         answer += i ** 2
#     return answer

import heapq
def solution(n, works):
    
    answer = 0 
    
    if n > sum(works):
        return 0
    
    # 최대힙으로 만들기 위한 사전 작업
    for i in range(len(works)):
        works[i] *= -1
    
    # 힙 생성
    heapq.heapify(works)
    
    while n != 0:
        x = heapq.heappop(works)
        x += 1
        n -= 1
        heapq.heappush(works,x)
    
    for i in works:
        answer += i ** 2
    return answer