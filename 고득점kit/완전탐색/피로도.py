# permutations 유형이라고 할 수 있음 -> 던전 방문 순서에 따라 더 좋은 방문 경로를 찾을 수 있기 때문(사실상 완전탐색)\

# 풀이 1. itertools permutations 사용
from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    
    for perm in permutations(dungeons, n):
        health = k
        cnt = 0
        for i in perm:
            if health >= i[0]:
                health -= i[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    
    return answer


#풀이 2. DFS 사용 -> 평소 하던대로 result 배열에 경로를 저장하는 것보단 visited 만 활용하는 것이 효율적
def solution(k, dungeons):
    
    
    def DFS(health):
        
        nonlocal answer
        
        # 종결조건: 딱히 없음, 그냥 조건 만족못하면 저절로 끝나는 형태 -> 종결조건이 따로 없으므로 백트래킹이 아니라 완전탐색이다.
        
        # 사실상 완전탐색이므로 DFS돌릴때마다 현재 방문한 던전 수를 answer와 비교해보면서 최댓값 탐색
        x = visited.count(True) # visited 에서 True 를 count 하는 것은 자주 활용될 수 있는 스킬
        if x > answer:
            answer = x
                    
        # 수행동작
        for i in range(n):
            if visited[i] == False: # 조건1: 아직 방문안한 던전 일때
                if health >= dungeons[i][0]: # 조건2: 피로도가 최소필요피로도보다 높은 입장가능상태일 때
                    visited[i] = True
                    DFS(health - dungeons[i][1])
                    visited[i] = False
                    

    n = len(dungeons)
    visited = [False for _ in range(n)]    
    answer = 0    
    DFS(k)
    return answer