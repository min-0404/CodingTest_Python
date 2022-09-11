def solution(s):
    
    x = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    if x == 0 and y == 0:
        return True
    if x == y:
        return True
    else:
        return False