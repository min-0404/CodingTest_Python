# 마인크래프트: n * m의 맵이 0층부터 ~ 256층이 되었을때 필요한 시간을 싹 다 구해서 최소값 구하기 -> 전형적인 완전탐색
# 다만 인벤토리안의 블록개수까지 고려해주어야 조건 구현이 조금 까다로울뿐 쉬운 문제임

# n = 가로, m = 세로, b = 인벤토리에 이미 가지고 있는 블록 개수
n, m, b = map(int, input().split())

# 맵 정보 입력받기
graph = []
for _ in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)
 

# 완전탐색
answer = []
for target in range(257): # 0층 ~ 256층이 되었을때의 상황을 완전탐색
    
    big = 0 # 파낸 블록의 개수(즉, 인벤토리에 저장해놓을 블록개수) 
    small = 0 # 매꿀 블록의 개수
    
    # target층 구현을 위해 graph 탐색
    for i in range(n):
        for j in range(m):
            
            if graph[i][j] >= target: # 해당 층이 target 보다 크면 -> "땅 파내야함"
                big += graph[i][j] - target # big에 파낸 블록개수 추가
            
            else: # 해당 층이 target보다 작으면 -> "땅 매꿔야함"
                small += target - graph[i][j] # small에 매꿔야할 블록개수 추가

    # target층 구현이 가능한지 확인        
    if big + b >= small: # 인벤토리 블록개수로 땅 모두 매꾸기 가능한지 확인
        answer.append((small + big * 2, target)) # 땅 매꾸기 = 1초 걸림, 땅 파고 인벤토리 넣기 = 2초 걸림

# 결과처리
answer.sort(key = lambda x : x[0])
print(answer[0][0], answer[0][1])

