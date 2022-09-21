def solution(phone_number):
    
    x = phone_number[:-4]
    y = phone_number[-4:]
    
    answer = ''
    n = len(x)
    for i in range(n):
        answer += '*'
    answer += y
    return answer