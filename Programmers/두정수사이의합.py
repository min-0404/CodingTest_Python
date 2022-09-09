def solution(a, b):
    
    x = max(a,b)
    y = min(a,b)
    
    sum = 0
    for i in range(y, x+1):
        sum += i
    
    
    return sum