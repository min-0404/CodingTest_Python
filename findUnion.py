def getParent(parent, x):
    if parent[x] == x:
        return x;
    return getParent(parent, parent[x]);

def unionParent(parent, x, y):
    x = getParent(parent, x);
    y = getParent(parent, y);
    if x < y:
        parent[y] = x;
    else:
        parent[x] = y;

v, e = map(int, input().split());
parent = [0] * (v + 1);

for i in range(1, v + 1):
    parent[i] = i;
for i in range(e):
    a, b = map(int, input().split());
    unionParent(parent, a, b);
print("각 원소가 속한 집합:", end="");
for i in range(1, v + 1):
    print(getParent(parent, i), end =" ");

print()

print("부모 테이블:", end = " ")
for i in range(1, v + 1):
    print(parent[i], end = " ");
    print();



        
    

    