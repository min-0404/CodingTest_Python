def solution(s):
    n = len(s)
    if n % 2 == 1:
        return s[n//2]
    else:
        x = n // 2
        return s[x-1:x+1]

