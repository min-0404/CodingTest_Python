from collections import defaultdict
def solution(array):
    
    # defaultdict 에 저장
    dic = defaultdict(int)
    for i in array:
        dic[i] += 1
    
    # 최댓값 선정
    max = 0
    for key,value in dic.items():
        if value >= max:
            max = value
    
    # 최빈값 result에 저장
    result = []
    for key in dic.keys():
        if dic[key] == max:
            result.append(key)

    # 출력 처리
    if len(result) >= 2:
        return -1
    if len(result) == 1:
        return result[0]