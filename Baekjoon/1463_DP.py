# 1로 만들기
# 연산 선택지가 -1 말고 한개밖에 없다면 그리디 적용해도 되지만,
# 연산 선택지가 여러개라면 다이나믹 적용해야 풀림
n = int(input());
dp = []
for i in range(n + 1):
    dp.append(i);

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1; # 일단 -1 한걸로 가정
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1);

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1);

print(dp[n]-1);

