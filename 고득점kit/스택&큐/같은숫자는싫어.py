def solution(arr):
    
    stack = []
    stack.append(arr[0]) # 일단 첫번재 원소 하나 넣고 시작
    
    for i in range(1, len(arr)):
        if arr[i] != stack[-1]: # 스택의 top가 i 비교해서 다를때만 푸쉬
            stack.append(arr[i])
        
    return stack