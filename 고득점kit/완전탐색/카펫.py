def solution(brown, yellow):
    answer = []
    
    for i in range(1, 5001):
        n = i
        m = (brown - (2 * i)  + 4) / 2
        if  n * m - brown == yellow and n >= m:
            answer. append(n)
            answer. append(m)
            

    return answer