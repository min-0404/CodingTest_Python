n, m = map(int, input().split());

graph = [list(map(int, input().split())) for _ in range(n)];


result = []

for i in range(n):
    min_val = min(graph[i]);
    result.append(min_val);

result.sort();
print(result[-1]);
