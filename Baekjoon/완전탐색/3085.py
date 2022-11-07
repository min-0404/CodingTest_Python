# 사탕게임: 애니팡이랑 똑같은 게임
# 가로로 또는 세로로 사탕위치 한 번 스왑해보고, 동일한 사탕 연속으로 된 것의 최댓값 구함
# 변경 방식: DFS(swap -> 결과 -> 원위치)
# 연속된 사탕의 최댓값 구하기: 구현력 필요(countCandy 함수) -> 처음엔 DFS로 탐색해보려 했지만 가로 한줄에서 최대, 세로 한 줄에서 최대이므로 따로 구현을 해줘야함

# map을 탐색하며 연속된 사탕 중 가장 긴 것 반환하는 함수
def countCandy():

    # result[0]은 가로 중 최대 연속 값, result[1]은 세로 최대 연속 값
    result = [] 

    
    # 가로 줄 확인 
    cnt = []
    for i in range(n):
        tmp = 1
        for j in range(n-1):
            if map[i][j] == map[i][j+1]:
                tmp += 1
            else:
                cnt.append(tmp)
                tmp = 1
        cnt.append(tmp) # 마지막 칸이 저장안될 경우를 위해서
    result.append(max(cnt))
    
    
    # 세로 줄 확인
    cnt = []
    for i in range(n):
        tmp = 1
        for j in range(n-1):
            if map[j][i] == map[j+1][i]:
                tmp += 1
            else:
                cnt.append(tmp)
                tmp = 1
        cnt.append(tmp) # 마지막 칸이 저장안될 경우를 위해서
    result.append(max(cnt))
    
    return max(result)
            
# n = 가로, 세로 길이
n = int(input())

# map 입력받기
map = []
for _ in range(n):
    x = str(input())
    x = list(x)
    map.append(x)


result = []
for i in range(n):
    
    for j in range(n-1):
        
        # 양옆 스왑: DFS와 유사하게 진행
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j] # 1. 스왑 한번 해보고
        result.append(countCandy()) # 2. 결과 저장하고
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j] # 3. 다시 원위치
        
        # 위아래 스왑
        map[j][i], map[j+1][i] = map[j+1][i], map[j][i] # 1. 스왑 한번 해보고
        result.append(countCandy()) # 2. 결과 저장하고
        map[j][i], map[j+1][i] = map[j+1][i], map[j][i] # 3. 다시 원위치

print(max(result))

        