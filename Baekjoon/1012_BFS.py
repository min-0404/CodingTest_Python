# BFS
from collections import deque

def BFS(y,x):
    q = deque();
    q.append((y,x));
    visited[y][x] = True;
    
    while q:
        y, x = q.popleft();
        for i in range(4):
            ny = y + dy[i];
            nx = x + dx[i];
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False and graph[ny][nx] == 1:
                q.append((ny, nx));
                visited[ny][nx] = True;

t = int(input());
for _ in range(t):
    m, n, k = map(int, input().split());
    
    graph = [[0] * m for _ in range(n)]; # 일단 0으로 다 채우기
    visited = [[False] * m for _ in range(n)];

    for i in range(k): # 주어진 좌표는 1로 변경
        x, y = map(int, input().split());
        graph[y][x] = 1;
    
    dx = [0, 0, -1, 1];
    dy = [-1, 1, 0, 0];

    cnt = 0;    
    for y in range (n):
        for x in range(m):
            if visited[y][x] == False and graph[y][x] == 1:
                BFS(y,x)
                cnt+=1
    print(cnt);
    