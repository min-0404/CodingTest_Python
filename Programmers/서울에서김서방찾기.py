def solution(seoul):
    answer = "김서방은 "
    
    for idx, val in enumerate(seoul):
        if val == "Kim":
            answer += str(idx)
    # for i in seoul:
    #     if i == "Kim":
    #         answer += str(seoul.index(i))
    return answer + "에 있다"
            