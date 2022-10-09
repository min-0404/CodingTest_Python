# n 과 m (3) -> product 문제
n,m = map(int, input().split())
def DFS():
    
    # 종결조건
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    
    # 수행동작
    for i in range(1, n+1):
        answer.append(i)
        DFS()
        answer.pop()

answer = []
DFS()
    
