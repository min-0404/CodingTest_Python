# DFS 와 BFS : 인접리스트로 구현했음
import sys
sys.setrecursionlimit(10000)
from collections import deque

n, m, v = map(int, input().split());
graph = [[] for _ in range(n+1)];
visited = [False for _ in range(n+1)];

for _ in range(m):
    x, y = map(int, input().split());
    graph[x].append(y);
    graph[y].append(x);



def DFS(x):
    visited[x] = True;
    print(x, end=" ");
    for i in graph[x]:
        if visited[i] == False:
            DFS(i);

def BFS(x):
    q = deque();
    q.append(x);
    visited[x] = True;
    while q:
        x = q.popleft();
        print(x, end = " ")
        for i in graph[x]:
            if visited[i] == False:
                q.append(i);
                visited[i] = True;
    

for i in range(1, len(graph)):
    graph[i].sort()
DFS(v);
visited = [False for _ in range(n+1)];
print();
BFS(v);
            

