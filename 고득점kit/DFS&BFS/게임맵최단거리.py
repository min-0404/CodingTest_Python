from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(maps) # 가로
    m = len(maps[0]) # 세로

    graph = [[-1] * m for _ in range(n)] # 일단 다 -1 로 채우기

    queue = deque()
    queue.append((0, 0))

    graph[0][0] = 1

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if graph[nx][ny] == -1: # 아직 방문안했다면
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    answer = graph[-1][-1]
    return answer