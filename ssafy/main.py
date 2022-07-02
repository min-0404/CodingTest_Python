final = []
T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    lst=list(map(int, input().split()))
    result=[]
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue
            result.append((lst[i], lst[j]))
    sum = 0
    for i in result:
        sum += i[0] % i[1]
    final.append(sum)
for test_case in range(T):
    print(f"#{test_case+1}"+" ", final[test_case]);
