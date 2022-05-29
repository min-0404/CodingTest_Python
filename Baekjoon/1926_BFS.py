# 그림문제 - BFS 로 풀기
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0];
dy = [0, 0, -1, 1];

def BFS(x,y):
    cnt = 1;
    q = deque();
    q.append((x,y));
    visited[x][y] = True;

    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                q.append((nx, ny));
                visited[nx][ny] = True;
                cnt += 1;
    return cnt;

lst = [];            
for x in range(n):
    for y in range(m):
        if visited[x][y] == False and graph[x][y] == 1:
            lst.append(BFS(x,y));

if len(lst) == 0:
    print(len(lst));
    print(0);
else:
    print(len(lst));
    print(max(lst));