# 좋은 수열: product 형태의 백트래킹 -> 중복제거, start 이런거 다 필요업음

import sys
n = int(input())

def check(idx):
    global answer
    
    for i in range(1, (idx // 2) + 1):
        if answer[-i:] == answer[-2 * i : -i]:
            return False
    return True


def DFS(idx):
    global answer

    # 종결조건
    if idx == n:
        for i in range(n):
            print(answer[i], end = "")
        sys.exit() # 주의!!: 최소 숫자 하나 구하고 끝이므로 발견순간, 아예 모든 재귀 끝내버려야해서 return 이 아닌 exit 사용
        
    
    # 수행동작
    for i in range(1, 4):
        answer.append(i)
        if check(idx + 1) == True:
            DFS(idx + 1)
        answer.pop()
    
answer = []
DFS(0)