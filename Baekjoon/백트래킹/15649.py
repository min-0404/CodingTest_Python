# n과 m (1) -> permutations 문제
n, m = map(int, input().split())

def DFS():
    # 종결조건
    if len(answer) == m: # len(answer) 말고 DFS함수의 매개변수로 idx사용해도 괜찮음
        print(" ".join(map(str, answer)))
        return
    # 실행동작
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            DFS()
            answer.pop()
            
answer = []
DFS()


