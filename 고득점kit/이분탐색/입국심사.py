def solution(n, times):
    
    # left, right 설정
    left = 1
    right = max(times) * n # 최악의 경우
    answer = 0
     
    while True:
        people = 0 # 해당 시간에서 심사가능한 사람 수
        
        # 종결 조건
        if left > right:
            break
                
        # mid 설정
        mid = (left + right) // 2
        
        for time in times:
            people += (mid // time)
        
        if people >= n: # 해당 시간 안에 충분히 n명 심사가능
            answer = mid # 일단 이게 최소의 경우일 수 있으니 answer에 저장해놓고
            right = mid - 1 # mid 의 왼쪽 탐색
            
        elif people < n: # 해당 시간 안에 n명 심사 불가
            left = mid + 1 # mid의 오른쪽 탐색
   
    return answer