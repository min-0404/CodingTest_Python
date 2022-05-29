import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split());

dx = [-1, 1, 0, 0];
dy = [0, 0, -1, 1];

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True;
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                dfs(nx, ny)
                
cnt = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0 and visited[x][y] == False:
            dfs(x, y)
            cnt += 1
print(cnt)
