n = int(input());

plans = input().split();

move = ["L", "R", "U", "D"];
dx = [0, 0, -1, 1];
dy = [-1, 1, 0, 0];

# 시작점 설정
x = 1;
y = 1;

for plan in plans:
    for i in range(4):
        if plan == move[i]:
            nx = x + dx[i];
            ny = y + dy[i];
            if 1<= nx <= n and 1 <= ny <= n:
                x = nx;
                y = ny;

print(x,y);

        


