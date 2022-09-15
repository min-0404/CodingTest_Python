from collections import deque
def solution(begin, target, words):
    
    # target이 없을 경우 바로 words 반환해버림
    if target not in words:
        return 0
    
    n = len(words)
    m = len(begin) # 글자 길이
    
    visited = [False for _ in range(n)]
    q = deque()
    
    # BFS의 특징을 잘 살려야함 -> 몇번째로 큐에 추가된 노드인지 알기 위한 형태
    q.append((begin, 0))
    
    while q:
        word, cnt = q.popleft()
        # 종결 조건
        if word == target:
            return cnt
        for i in range(n): # words 배열을 순환하면서
            temp_cnt = 0
            for j in range(m): # 한 개의 word를 순환하면서
                if word[j] != words[i][j]:
                    temp_cnt += 1
            if temp_cnt == 1 and visited[i] == False:
                q.append((words[i], cnt+1))
                visited[i] = True