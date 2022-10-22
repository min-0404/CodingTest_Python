# 숨바꼭질: 최단거리를 탐색하는 유형이므로, DFS 보단 BFS를 사용해야한다.
from collections import deque
n, k = map(int, input().split())
m = 10 ** 5 # 최댓값 설정
lst = [0] * (m+1) # n부터 시작해서 몇번째 스텝의 위치인지 저장하는 리스트


q = deque()
q.append(n)

while q:
    x = q.popleft()
    
    # 종결조건
    if x == k:
        break
            
    # 수행동작
    for i in (x - 1, x + 1, x * 2): # 이렇게 for문을 활용하는 것도 가능하다.
        if 0 <= i <= m: # 조건1. 다음 스텝이 범위 안에 존재할 때
            if lst[i] == 0: # 조건2. 다음 스텝이 아직 방문안한 위치일 때
                lst[i] = lst[x] + 1
                q.append(i)


print(lst[x])