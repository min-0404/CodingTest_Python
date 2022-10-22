# 미로탐색: BFS 사용
from collections import deque

# n = 가로, m = 세로
n, m = map(int, input().split())

# 이 문제에선 visited 의 True/False로 방문확인하거나
# map 배열 따로 추가해서 경로 저장할 필요가 없음 -> graph 하나면 충분
graph = []
for _ in range(n):
  graph.append(list(map(int, input()))) # split 사용 안해야함

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

# BFS 돌리면서 graph에 경로순서 저장해나가기
queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m: # 조건1. nx, ny 범위 안벗어나는지 확인
        if graph[nx][ny] == 1: # 조건2. graph[nx][ny] 가 "벽이 아니라는 것" + "아직 방문안했다는 것" 둘 다 확인 가능
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

# [nx, ny] 값 출력
print(graph[-1][-1])
