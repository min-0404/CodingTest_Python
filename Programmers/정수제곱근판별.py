def solution(n):
    
    x = n ** 0.5
    
    if x % 1 == 0: # 만약 제곱근이 정수라면
        return (x+1) ** 2
    return -1
        
