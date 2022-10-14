def DFS(x):

    # 종결조건: 따로 없음

    # 수행동작
    for i in graph[x]:
        if visited[i] == False:
            visited[i] = True
            DFS(i)
    

# n = 노드 개수, m = 간선 개수
n, m = map(int, input().split())

# tmp 는 간선 정보 임시 저장
tmp = []
for _ in range(m):
    x, y = map(int, input().split())
    tmp.append((x, y))

# tmp 순회하면서 graph 이차원 배열에 인접리스트 구현
graph = [[] for _ in range(n+1)]
for a, b in tmp:
    graph[a].append(b)
    graph[b].append(a)

# visited 배열 -> 1차원이면 충분
visited = [False for _ in range(n+1)]

cnt = 0 # 뭉텅이 개수
for i in range(1, n+1):
    if visited[i] == False:
        DFS(i)
        cnt += 1

print(cnt)
