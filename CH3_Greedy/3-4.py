# 1로 만들기
# -1 연산 빼고 선택할 연산이 한가지 뿐이므로 간단하게 그리디 적용 가능
# 만약 연산 선택지가 여러개라면 무조건 dp 적용해서 1부터 한단계씩 올라가야함
n, k = map(int, input().split());

cnt = 0;
while 1:
    if(n == 1):
        break;
    if n % k == 0:
        n = n // k;
        cnt += 1;
    else:
        n = n - 1;
        cnt += 1;

print(cnt);
