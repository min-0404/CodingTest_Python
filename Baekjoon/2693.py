# N번째 큰 수

n = int(input())

for i in range(n):
    lst = list(map(int, input().split()))
    lst.sort(reverse = True)
    print(lst[2])
    

