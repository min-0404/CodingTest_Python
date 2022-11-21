# 너무 어렵다

n, m = map(int, input().split());

graph = [list(map(int, input().split())) for _ in range(n)];
visited = [[False] * m for _ in range(m)];

dx = [-1, 1, 0, 0];
dy = [0, 0 , 1, -1];

def DFS(x,y):
    visited[x][y] = True;
    for i in range(4):
        nx = x + dx[i]; 
        ny = y + dy[i];
        if 0 <= nx < n and 0 <= ny < m: 
            DFS(nx, ny);
            visited[nx][ny] = True;

for i in range(n):
    for j in range(m):
         if graph[i][j] == 1 and visited[i][j] == False:
            DFS(i, j);  
             








