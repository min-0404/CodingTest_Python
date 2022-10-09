# nqueen 문제: pypy 로 제출해야 통과함

def nqueen(row):
    global answer
    
    # 종결조건
    if row == n:
        answer += 1
        return
    
    # 실행동작
    for i in range(n):
        queen[row] = i # 일단 둬본다
        if check(row) == True: # 제대로 두었는지 확인 
            nqueen(row+1) # 확인되면 다음꺼 진행

def check(row):

    for i in range(row):
        if queen[row] == queen[i] or abs(queen[row] - queen[i]) == abs(row - i):
            return False
    return True

n = int(input())
queen = [0 for _ in range(n)]
answer = 0
nqueen(0)
print(answer)


    