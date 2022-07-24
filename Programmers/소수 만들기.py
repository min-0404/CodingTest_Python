# itertools의 순열(permutations)과 조합(combinations)의 이해 필수
from itertools import combinations
# 에라토스테네스의 체 이용 
def sosu(n):
    lst = [True for _ in range(n + 1)]
    lst[0] = False
    lst[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if lst[i]:
            for j in range(i + i, n + 1, i):
                lst[j] = False
    return lst

def solution(nums):
    # permutations 가 아닌 combinations 사용 이유: 중복 제외하기 위해
    comb = list(combinations(nums, 3)) # 세개의 숫자로 더할 수 있는 조합 배열 
    lst = sosu(3000) # 3000까지의 소수 배열
    
    cnt = 0
    for i in comb:
        if lst[sum(i)]:
            cnt += 1
    return cnt