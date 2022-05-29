# DFS
import sys
sys.setrecursionlimit(10000);

def DFS(y, x):
    visited[y][x] = True;
    for i in range(4):
        ny = y + dy[i];
        nx = x + dx[i];
        if (0 <= nx < m) and (0 <= ny < n):
            if visited[ny][nx] == False and graph[ny][nx] == 1:
                DFS(ny, nx);
        
t = int(input());
for _ in range(t):
    m, n, k = map(int, input().split());
    
    graph = [[0] * m for _ in range(n)]; # 일단 0으로 다 채우기
    visited = [[False] * m for _ in range(n)];
    cnt = 0;

    for i in range(k): # 주어진 좌표는 1로 변경
        x, y = map(int, input().split());
        graph[y][x] = 1; # 조건에 따라서 유동적으로 좌표를 조절해줘야함
    
    dx = [0, 0, -1, 1];
    dy = [-1, 1, 0, 0];
    
    for y in range (n):
        for x in range(m):
            if visited[y][x] == False and graph[y][x] == 1:
                DFS(y,x)
                cnt+=1
    print(cnt);
    

