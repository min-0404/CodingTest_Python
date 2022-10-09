# 연산자 끼워넣기: DFS, permutations 이용하는 방법 있음

import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus != 0:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus != 0:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply != 0:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide != 0:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)