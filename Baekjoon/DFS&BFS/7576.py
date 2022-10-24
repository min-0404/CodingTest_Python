# # 토마토 문제: 최단거리와 유사하기 때문에 BFS 사용
from collections import deque
import sys

# n = 가로, m = 세로
m, n = map(int, input().split())

# 초기 box 형태 저장하기
box = []
for _ in range(n):
    lst = list(map(int, input().split()))
    box.append(lst)

# visited 에 익은 날짜 저장할 것임
visited = [[0] * m for _ in range(n)]


# 먼저 초기 box에 익어있는 토마토를 visited에서 1로 설정하고, 큐에 넣어줌
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            visited[i][j] = 1
            q.append((i, j))


# 네 방향으로 BFS 돌리자
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

# 예외처리 1: 하나의 토마토라도 익지 못하면(= 즉, visited에 0이 존재한다면) -1 반환하고 끝내버리기
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and box[i][j] != -1: # 애초에 토마토가 없어서 visited가 0 인 경우는 제외해줘야함
            print(-1)
            sys.exit()

# 예외처리 2: 첨부터 모든 박스 칸의 토마토가 1이라면, 애초에 큐가 안돌아가서 visited의 모든 원소들이 1일 것이고,
# 이 때 0을 프린트 해줘야하는데, 애초에 m = 1 인 상태에서 1이 뺄셈 되어 저절로 0이 되므로 따로 예외 코드가 필요없음

# 이차원 배열에서 최댓값 구하는 법
m = max(map(max, visited)) - 1 #  초기 토마토 시작이 0일이라서 원래 0으로 시작해야하는데, 구별을 위해 어쩔 수 없이 1로 시작했으므로 1빼줌
print(m)

