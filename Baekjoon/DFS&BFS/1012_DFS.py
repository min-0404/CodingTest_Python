# 유기농 배추: 덩어리 개수 세는 문제 -> DFS 활용
import sys
sys.setrecursionlimit(1000000) # 탐색 깊이 설정 안해주면 런타임 에러 발생
def DFS(x, y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < m and 0 <= ny < n: # 조건 1
            if graph[nx][ny] == 1: # 조건 2
                if visited[nx][ny] == False: # 조건 3
                    visited[nx][ny] = True
                    DFS(nx, ny)
                    
t = int(input())
for _ in range(t):

    # m = 가로, n = 세로, k = 배추의 개수 (헷갈리게 하려고 n과 m을 바꿈)
    m, n, k = map(int, input().split()) 
    
    # 사전준비
    graph = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # 배추있는 위치를 1로 바꾸기
    for _ in range(k):
        x, y = map(int, input().split());
        graph[x][y] = 1 

    # DFS 실행    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == False:
                if graph[i][j] == 1:
                    visited[i][j] = True
                    DFS(i, j)
                    cnt+=1 # DFS 끝날때마다 1씩 증가
    
    print(cnt)
    

