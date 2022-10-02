def solution(numbers, target):
    
    def DFS(idx, sum):
        
        # 종결 조건
        if idx == len(numbers):
            
            # 종결 조건 사이에 sum == target인지 확인
            if sum == target:
                nonlocal answer # solution() 내부 중첩함수라 global 대신 nonlocal 사용
                answer += 1
            
            return
        
        # 수행 동작
        DFS(idx + 1, sum + numbers[idx])
        DFS(idx + 1, sum - numbers[idx])
    
    
    answer = 0
    DFS(0, 0) # idx, sum
    return answer