from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(maps) # 가로
    m = len(maps[0]) # 세로

    graph = [[-1] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0))

    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < m and 0 <= nx < n and maps[nx][ny] == 1:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    answer = graph[-1][-1]
    return answer