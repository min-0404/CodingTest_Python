def solution(n, arr1, arr2):
    
    arr =  [[0] * n for _ in range(n)] #반환할 지도
    
    for i in range(n):
        
        # 10진수를 2진수로 변환(문자열 반환됨)
        x = bin(arr1[i])
        y = bin(arr2[i])
        
        # 앞의 "0b" 삭제
        x = x[2:]
        y = y[2:]
            
        # n자리수가 되도록 앞을 0으로 채워줌    
        while len(x) < n:
            x = "0" + x 
        while len(y) < n : 
            y = "0" + y
            
        # 문자열을 리스트로 변환
        x = list(x)
        y = list(y)
        
        # 문자를 정수로 변환
        x = list(map(int,x))
        y = list(map(int, y))
        
        # 지도 생성
        for j in range(n):
            arr[i][j] = x[j] + y[j]
            
    # 원소들을 문자열로 변경
    result1 = []
    for i in arr:
        i = list(map(str, i))
        result1.append(i)
        
    # 문자열 리스트를 하나의 문자열로 합침
    result2 =[]    
    for i in result1:
        i = "".join(i)
        result2.append(i)
        
    # 0 -> " ", 1 과 2 -> "#"로 변경    
    result3 = []
    for i in result2:
        i = i.replace("2", "#")
        i = i.replace("1", "#")
        i = i.replace("0", " ")
        result3.append(i)
  
    return result3