def solution(x):
    z = str(x)
    sum = 0
    for i in z:
        sum += int(i)
    
    if x % sum == 0:
        return True
    else:
        return False