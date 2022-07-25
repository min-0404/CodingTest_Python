from collections import deque

def solution(priorities, location):
    
    answer = 0
    
    q = deque([(v,i) for i,v in enumerate(priorities)])    
    
    while q:
        
        x = q.popleft()
        
        if x[0] < max(q)[0]:
            q.append(x)
        else:
            answer += 1
            if x[1] == location:
                break
                
    return answer
            
    