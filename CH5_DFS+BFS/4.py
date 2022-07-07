from collections import deque

n, m = map(int, input().split());
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0 ]
dy = [0, 0 , 1, -1]

def BFS(x,y):
    x,y = q