from collections import Counter
def solution(topping):
    
    # counter = {1: 4개, 2: 2개, 3: 1개...}
    counter = Counter(topping)
    
    s1 = set()
    s2 = set(topping)
    
    answer = 0
    for i in topping: # topping 순회하면서
        
        counter[i] -= 1
        
        s1.add(i)  # s1에는 추가
        
        if counter[i] == 0: # counter[i] = 0 이란 뜻은 더이상 s2에 이 토핑이 없다는 뜻
            s2.remove(i) # s2에선 빼줌
        
        if len(s1) == len(s2):
            answer += 1
    
    return answer