# 토마토 문제 -> 최단거리와 유사하기 때문에 BFS 사용
from collections import deque
# n = 가로, m =  세로(헷갈리게 하려고 순서 바꿔놓음)
m, n = map(int, input().split())

box = []
for _ in range(n):
    x = list(map(int, input().split()))
    box.append(x)

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 일단 큐에 토마토 위치 집어넣기
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

# BFS 돌리기
while q:
    
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
        if box[nx][ny] != -1:
        

    


visited = [[False] * m for _ in range(n)]
graph = [[x] * m for _ in range(i)]
if visited[i][j] == True:
    
# 설계과정
