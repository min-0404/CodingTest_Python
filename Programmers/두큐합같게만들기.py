from collections import deque # 귀찮지만 효율성을 위해 써야했음
def solution(queue1, queue2):
    
    # 일단 덱으로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # while 안에서 매번 sum 연산 돌리면 비효율적 -> 귀찮지만 미리 계산해둠
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # cnt가 limit에 도달했을때까지 존나 바꿔댓는데 합이 안같아지면 while문 종결해버림 -> -1 반환
    cnt = 0
    limit = len(q1) * 4
    
    
    while sum1 != sum2:
        
        if sum1 > sum2:
            x = q1.popleft() 
            q2.append(x)
            sum1 -= x
            sum2 += x
            cnt+=1
            
        elif sum1 <= sum2:
            x = q2.popleft() 
            q1.append(x)
            sum2 -= x
            sum1 += x
            cnt += 1
        
        # 종결조건: 두 큐의 합이 같아질 수 없을때 
        if cnt == limit:
            return -1
            
    return cnt