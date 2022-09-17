def solution(s):
    
    n = len(s)
    
    s = s[2: n-2] #{{, }} 제거
    
    lst = s.split("},{") # 사이의 },{ 제거
    
    lst.sort(key = len) # len 를 기준으로 정렬
    
    # "," 처리
    lst2 = []
    for i in lst:
        i = i.split(",")
        lst2.append(i)
    
    # 정수로 변환
    lst3 = []
    for i in lst2:
        i = list(map(int, i))
        lst3.append(i)

        
    answer = []
    for i in lst3:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer