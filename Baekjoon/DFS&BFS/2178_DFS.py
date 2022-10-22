# 미로탐색: DFS 사용 -> DFS 사용 불가
# DFS 알고리즘 특성 상, 최단 거리를 찾으려면 완전 탐색을 하고, 그 중에서 최소값을 선택해야 하는데,
# 경로가 아주 많아지면 무조건 시간 초과 발생 -> 하지만 BFS는 최단거리를 보장하기 때문에 최단거리 문제는 무조건 BFS 사용해야함

# n = 가로, m = 세로
n, m = map(int, input().split())

# 이 문제에선 visited 의 True/False로 방문확인하거나
# map 배열 따로 추가해서 경로 저장할 필요가 없음 -> graph 하나면 충분
graph = []
for _ in range(n):
  graph.append(list(map(int, input()))) # split 사용 안해야함

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def DFS(x, y):

    # 종결조건: 따로 없음

    # 수행동작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                DFS(nx, ny)

DFS(0, 0)

print(graph[-1][-1])