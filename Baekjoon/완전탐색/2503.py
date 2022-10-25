# 숫자야구: 완전탐색 = permutations 활용 + 까다로운 조건
from itertools import permutations

# 게임 횟수
N = int(input())

# 3개 숫자로 가능한 모든 조합 제작
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
perm = list(permutations(data, 3))

# 게임 N번
for _ in range(N):
    
    
    n, s, b = map(int, input().split())
    n = list(str(n))
    rmcnt = 0

    for i in range(len(perm)):

        # 1. strike, ball 초기화
        strike = 0
        ball = 0
        i -= rmcnt # num[0] 부터 시작하기 위해: 항상 perm의 첫번째 원소부터 순회 시작하기 위해 필요한 변수
        
        # 2. 하나의 숫자 분석하면서 스트라이크, 볼 개수 세기
        for j in range(3):
            if perm[i][j] == n[j]:
                strike += 1
            elif n[j] in perm[i]:
                ball += 1

        # 3. 스트라이크, 볼 횟수로 가능한 후보인지 판단: 후보가 아니라면 perm에서 삭제해버림
        if (strike != s) or (ball != b):
            perm.remove(perm[i])
            rmcnt += 1

print(len(perm))