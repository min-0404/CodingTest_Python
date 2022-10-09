# n 과 m (2) -> combinations 문제
n, m = map(int, input().split())

def DFS(start):

    # 종결조건
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    
    # 수행동작
    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            DFS(i+1)
            answer.pop()

answer = []
DFS(1)