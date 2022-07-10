import math
def solution(progresses, speeds):
    
    p = []
    results = []
    answer = []

    for i in progresses:
        p.append(100 - i);
    
    for i in range(len(speeds)):
        results.append((p[i] // speeds[i]) + 1 if p[i] % speeds[i] > 0 else p[i] // speeds[i])

    stack = []
    stack.append(results[0])
    for i in results[1:]:
        if i > stack[0]:
            answer.append(len(stack));
            stack.clear()
        stack.append(i);
    answer.append(len(stack))
        
    return answer