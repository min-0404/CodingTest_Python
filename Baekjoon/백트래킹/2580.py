# 미친 로봇

dx = [-1, 1, 0, 0]
dy = [0, 0 ,1 , -1]

def DFS(x, y, visited, total):
    
    global answer 
    if len(visited) == N + 1:
        answer += total
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            DFS(nx, ny, visited, total * probability[i])
            visited.pop()


N, ep, wp, sp, np = map(int, input().split())

probability = [ep, wp, sp, np]

answer = 0 
