#  부분수열의 합: 백트래킹이 아니라 사실상 완전탐색이라고 볼 수 있음
n, s = map(int, input().split())
arr = list(map(int, input().split()))


def DFS(idx, total):
    
    # 종결조건
    if idx >= n:
        return
    
    # total에 idx의 값을 더한 후에 s와 비교과정을 거쳐야함
    # 생각없이 idx의 값 더하지 않고 먼저 s와 비교해버리면 에러남
    total += arr[idx]
    if total == s:
        global answer
        answer += 1 # 여기서 return 해버리면 안됨, 찾았다고 끝이 아니라 부분수열에서 더 확장시킨 수열도 정답일수 있으므로
    
    # 수행동작
    DFS(idx + 1, total)
    DFS(idx + 1, total - arr[idx])


answer = 0
DFS(0, 0)
print(answer)    

        