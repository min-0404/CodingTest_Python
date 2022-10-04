
def solution(n, costs):

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
    
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    answer = 0

    for a, b, cost in costs:
        if findParent(parent, a) == findParent(parent,b ):
            continue
        else:
            unionParent(parent, a, b)
            answer += cost
    return answer