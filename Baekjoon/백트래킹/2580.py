# 미친로봇: permutations 형태의 백트래킹

# 주의) 서, 동, 북, 남 순서 맞춰야함
dx = [-1, 1, 0, 0] 
dy = [0, 0, 1, -1]

def dfs(x, y, visited, total):

    global answer

    # 종결조건
    if len(visited) == N + 1:
        answer += total
        return
    
    # 수행동작
    for i in range(4): # 4방향이므로
        nx = x + dx[i] 
        ny = y + dy[i]

        if (nx, ny) not in visited: # 중복제거
            visited.append((nx, ny)) 
            dfs(nx, ny, visited, total * probability[i])
            visited.pop()

N, ep, wp, sp, np = map(int, input().split())
probability = [ep, wp, sp, np]
answer = 0

dfs(0, 0, [(0, 0)], 1)
print(answer * (0.01 ** N))