
from collections import deque
def solution(n, wires):

    def BFS(n):
        q = deque()
        q.append(n)
        visited[n] = True

        while q:
            x = q.popleft()
            for i in graph[x]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
                    nonlocal cnt
                    cnt += 1
    
    answer = []
    for wire in wires:
        tmp = wires[:] # 얕은복사
        tmp.remove(wire)

        visited = [False for _ in range(n+1)]
        
        # graph: 인접 리스트로 구현
        graph = [[] for _ in range(n+1)]
        for a, b in tmp:
            graph[a].append(b)
            graph[b].append(a)

        result = []
        for i in range(1, n+1):
            if visited[i] == False:
                visited[i] = True
                cnt = 1
                BFS(i)
                result.append(cnt)
        answer.append(abs(result[0] - result[1]))

    return min(answer) 

    
