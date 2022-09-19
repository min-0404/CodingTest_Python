def solution(arr):
    

    m = min(arr)
    arr.remove(m)
    answer = arr
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return answer