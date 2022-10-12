# n과m(4)

n, m = map(int, input().split())
def DFS(start):

    # 종결조건
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    
    # 수행동작
    for i in range(start, n + 1): # 중복 검사 안해도됨, but start는 써야함
        answer.append(i)
        DFS(i)
        answer.pop()

answer = []
DFS(1) 