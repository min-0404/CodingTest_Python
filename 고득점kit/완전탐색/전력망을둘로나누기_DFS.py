def solution(n, wires):

    def DFS(n):
        # 종결조건: 없음

        # 실행동작
        nonlocal cnt
        for i in graph[n]:
            if visited[i] == False:
                visited[i] = True
                cnt += 1
                DFS(i)

    answer = [] # 한개의 wire 삭제한 경우들의 두개의 전력망 차이 저장할 배열
    for wire in wires:
        tmp = wires.copy() # 얕은 복사
        tmp.remove(wire)

        visited = [False for _ in range(n)] # idx = 0 인 애는 걍 버리자
        
        # graph 인접 리스트 구현
        graph = [[] for _ in range(n+1)]
        for a, b in tmp:
            graph[a].append(b)
            graph[b].append(a)

        result = [] # DFS 결과, 두개의 송전탑 결과를 저장할 배열

        # 모든 송전탑을 순차적으로 탐색하면서 DFS 실행
        for i in range(1, n+1):
            if visited[i] == False:
                cnt = 1 # 일단 탐색된 것도 한개로 쳐야함
                visited[i] = True
                DFS(i)
                result.append(cnt)
    
        answer.append(abs(result[0] - result[1])) # result[0] = 첫번째 전력망의 송전탑 개수, result[1] = 두번째 전력망의 송전탑 개수
    
    return min(answer)
                
                
            