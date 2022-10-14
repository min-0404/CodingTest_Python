# 단지 번호 붙이기 : 단순한 DFS 또는 BFS문제, 덩어리 개수와, 그 덩어리 이루는 개수 둘다 알아내야함
from sys import stdin
def DFS(x, y):

    global cnt

    # 종결조건: 따로 없음

    # 수행동작
    visited[x][y] = True 
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n: 
            if map[nx][ny] == 1:
                if visited[nx][ny] == False:
                    DFS(nx, ny)
    
    
n = int(input())
map = [[0] * n for _ in range(n)]
for i in range(n):
    line = stdin.readline().strip()
    for j, b in enumerate(line):
        map[i][j] = int(b)

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


answer = []
result = 0 # 총 단지의 개수
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            if visited[i][j] == False:
                cnt = 0 # 단지별 아파트 개수
                DFS(i, j)
                result += 1 # DFS 끝날때마다 하나씩 증가 
                answer.append(cnt)
print(result)

answer.sort()
for i in answer:
    print(i)