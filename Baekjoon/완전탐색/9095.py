# 1, 2, 3 더하기 -> 간단한 product 유형: 중복검사도 필요없고, start도 필요없다. 무지성 탐색 (종결조건 꼭 필요)
n = int(input())

def DFS():
    
    global cnt, x

    # 종결조건
    if sum(result) == x:
        cnt += 1
        return

    # 주의!: 완전 무지성 탐색이므로 배열길이가 x보다 길어졌을때 종결조건을 꼭 넣어줘야함
    if len(result) > x:
        return
    
    # 수행동작
    for i in range(1, 4):
        result.append(i)
        DFS()
        result.pop()


for _ in range(n):
    x = int(input())
    cnt = 0
    result = []    
    DFS()
    print(cnt)
        