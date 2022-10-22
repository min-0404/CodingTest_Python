# 암호만들기: combinations 유형 -> 문자열은 꼭 오름차순이어야 하기때문에, 오름차순으로 정렬된 배열을 탐색할때,
# 문자 하나 선택되면 그 문자보다 앞에 있는 문자들은 탐색할 필요 없다. 따라서 combinations 유형이다.

def DFS(start):

    global visited, arr

    # 종결조건
    if len(visited) == l:

        # 모음, 자음 조건 맞는지 확인
        vo = 0
        co = 0
        for i in visited:
            if i in ['a', 'e', 'i', 'o', 'u']:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(visited))
        
        return

    # 수행동작
    for i in range(start, c): # combinations 이므로 start 사용하는 것 잊지말자
        if arr[i] not in visited: # 중복 확인
            visited.append(arr[i])
            DFS(i+1)
            visited.pop()



l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
visited = []
DFS(0)