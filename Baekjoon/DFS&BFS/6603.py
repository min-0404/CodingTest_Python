# 로또 -> 전형적인 combiantion 유형

def DFS(idx, start):
    
    global answer, k

    # 종결조건
    if idx == 6:
        print(*answer)
        return

    # 수행동작
    for i in range(start, k): # 꼭 start 사용
        if arr[i] not in answer: # 중복제거
            answer.append(arr[i]) 
            DFS(idx + 1, i+1)
            answer.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    del arr[0]
    if k == 0:
        break
    answer = []
    DFS(0,0)
    print()