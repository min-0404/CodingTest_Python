from collections import defaultdict

def solution(clothes):
    
    # clothes 돌면서 defaultdict 완성
    dic = defaultdict(int)
    for i in clothes:
        dic[i[1]] += 1
    
    # 조합의 원리 활용: a가 2개, b가 1개 있다면 가능한 조합은: (2+1) * (1+1)
    lst = [] 
    for key, value in dic.items():
        lst.append(value + 1)
    
    # 결과 처리: 아무것도 안입을때는 제외하므로 -1 처리
    answer = 1
    for i in lst:
        answer *= i
    return answer - 1