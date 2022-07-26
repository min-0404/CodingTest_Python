def solution(n, computers):
    
    visited = [False for _ in range(n)]
        
    def DFS(x):
        
        visited[x] = True
        
        for i in range(n):
            if computers[x][i] == 1 and visited[i] == False:
                    DFS(i)
    
    cnt = 0
    for i in range(n):
            if visited[i] == False:
                DFS(i)
                cnt += 1 
                
    return cnt