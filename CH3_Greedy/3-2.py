n, m ,k = map(int, input().split());

data = list(map(int, input().split()));

data.sort(reverse=True);

cnt1 = m // (k + 1); # 패턴 연산 횟수
cnt2 = m % (k + 1); # 쩌리짱

pattern_val = (data[0] * k) + data[1];

print((pattern_val * cnt1) + (data[0] * cnt2)) 
