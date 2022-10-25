#모든 순열

# 풀이1. 단순한 DFS 백트래킹
def DFS():

    # 종결조건
    if len(result) == n:
        print(*result)
        return

    # 수행동작
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            DFS()
            result.pop()

n = int(input())
result = []
DFS()

# 풀이2. permutations 사용
from itertools import permutations

n = int(input())
lst = [i for i in range(1, n+1)]

perm = list(permutations(lst, n))

for p in perm:
    print(*p)


