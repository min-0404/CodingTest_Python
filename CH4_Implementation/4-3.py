dx = [1,2,3,4,5,6,7,8];
dy = ["a","b","c","d","e","f","g","h"];
moves = [(-1, 2), (1,2), (2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)];

n = input();
x = int(n[1]);
y = int(dy.index(n[0])) + 1; # 정수형으로 바꿔주는 것이 핵심


cnt = 0;

for move in moves:
    nx = x + move[0];
    ny = y + move[1];
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1;

print(cnt);


