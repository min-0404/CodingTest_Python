# 연결요소의 개수 세기 -> 그래프에서 뭉텅이의 개수 세기 
# 파인드유니온 활용
from collections import Counter
def findParent(parent, n):
    if parent[n] == n:
        return n
    return findParent(parent, parent[n])

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a 

# n = 노드 개수, m = 간선 개수
n, m = map(int, input().split())

# tmp 는 간선 정보 임시 저장
tmp = []
for _ in range(m):
    x, y = map(int, input().split())
    tmp.append((x,y))

# tmp 순회하면서 연결된 정점끼리 union 해줌
parent = [i for i in range(n+1)]
for a, b in tmp:
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)

# 중요! 자꾸 까먹음: 각 노드별 findParent 다시 돌려서 uf 에 저장하는 과정을 꼭 거쳐야함
uf = []
for i in range(1, n+1):
    uf.append(findParent(parent, i))

# Counter 활용 -> result에는 부모 노드 번호 저장됨(즉, 중복된 부모 노드 없앨 수 있음)
uf = Counter(uf)
result = list(uf.values())

# 따라서 result의 원소 개수 = 부모 노드의 개수 = 뭉텅이의 개수
print(len(result))