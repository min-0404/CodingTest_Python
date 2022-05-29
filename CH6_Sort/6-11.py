n = int(input());

lst = []
for i in range(n):
    data = input().split(); 
    lst.append((data[0], int(data[1]))); # 튜플 형태로 리스트에 넣기 (사실 리스트 형태로 넣어도 됨)

lst.sort(key=lambda x : x[1]); # 형식 암기할 것

for i in range(n):
    print(lst[i][0]);