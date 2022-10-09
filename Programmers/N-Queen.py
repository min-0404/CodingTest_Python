def solution(n):
    
    def nqueen(row):
        
        # 종결조건
        if row == n:
            nonlocal answer
            answer += 1
            return
        # 수행동작
        for i in range(n):
            queen[row] = i
            if check(row) == True:
                nqueen(row+1)
        
    def check(row):
        for i in range(row):
            if queen[i] == queen[row] or abs(queen[row] - queen[i]) == abs(row - i):
                return False
        return True
    
    answer = 0
    queen = [0 for _ in range(n)]
    nqueen(0)
    return answer