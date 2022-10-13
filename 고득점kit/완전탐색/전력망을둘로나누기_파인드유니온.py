from collections import Counter
def solution(n, wires):
    
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
    
    answer = []
    for wire in wires:
        tmp = wires[:] # 얕은복사
        tmp.remove(wire)

        parent = [i for i in range(n+1)]
        
        for a, b in tmp:
            if findParent(parent, a) == findParent(parent, b):
                continue
            unionParent(parent, a, b)

        uf = []
        for i in range(1, n+1):
            uf.append(findParent(parent, i))

        uf = Counter(uf)
        result = list(uf.values())
        
        answer.append(abs(result[0] - result[1]))

    return min(answer)

