# 치킨 배달
# 집 위치와 치킨집 위치를 저장해놓고, 남겨놓을 m개의 치킨집을 combiantions으로 뽑아놓음
# 각 경우의 치킨 거리 계산해보고, 치킨 거리 최소 나올때의 경우 반환

from itertools import combinations
n, m = map(int, input().split())

map = list(list(map(int, input().split())) for _ in range(n))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            house.append((i,j))
        elif map[i][j] == 2:
            chicken.append((i,j))

comb = list(combinations(chicken, m))

result = 9999
for c in comb:
    tmp = 0
    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        tmp += chi_len
    result = min(result, tmp)

print(result)     

        


            


            