# 초기 풀이: 비효율적
"""
def solution(s):
    answer = 1

    for i in range(len(s)):
        mid = i
        n =  min(i, len(s) - 1 - i)
        for j in range(1, n +1):
            left = s[mid -j:mid]
            left = left[::-1]
            right = s[mid+1:mid+1+j]
            if left == right:
                answer = max(answer, j *2 + 1)
            
    return answer
"""

# 개선된 풀이
def isPalindrome(x):
    if x == x[::-1]:
        return True
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i + 1,len(s) + 1):
            if isPalindrome(s[i:j]):
                answer = max(answer, len(s[i:j]))

    return answer