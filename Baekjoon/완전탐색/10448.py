# 유레카 이론: 단순한 반복문 사용한 완저탐색

# 일단 주어진 공식에 따라 triangleNum 배열에 Tn 계산해놓기
triangleNum = []
for i in range(1, 45):
    triangleNum.append(i * (i + 1) // 2)

# Tn에서 3개를 골라 더한 값이 인덱스인 곳을 1로 바꿔놓음 = 완탐 끝
eureka = [0 for _ in range(1001)]
for i in triangleNum:
    for j in triangleNum:
        for k in triangleNum:
            if i + j + k <= 1000:
                eureka[i + j + k] = 1

# 정답 출력
n = int(input())
for _ in range(n):
    x = int(input())
    if eureka[x] == 1:
        print(1)
    else:
        print(0)

        
    
