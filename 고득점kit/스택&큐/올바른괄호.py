def solution(s):
    
    stack = []
    
    for i in s:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
                
    if len(stack) >= 1:
        return False
    return True
    