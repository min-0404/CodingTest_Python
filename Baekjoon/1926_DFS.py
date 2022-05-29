# 그림문제 : DFS 로 풀기
import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split());
graph = [list(map(int, input().split())) for _ in range(n)];
visited = [[False] * m for _ in range(n)];
dx = [-1, 1, 0, 0];
dy = [0, 0, -1, 1];

def DFS(x,y):
    global cnt;
    visited[x][y] = True;
    cnt += 1;

    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                DFS(nx, ny);


lst = [];
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and visited[x][y] == False:
            cnt = 0;
            DFS(x,y);
            lst.append(cnt);

if len(lst) == 0:
    print(len(lst));
    print(0);
else:
    print(len(lst));
    print(max(lst));