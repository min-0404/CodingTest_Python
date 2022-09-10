from collections import defaultdict
def solution(clothes):
    
    dic = defaultdict(int) # 의상종류별 의상이 몇개인지 저장할 딕셔너리
    for i in clothes:
        dic[i[1]] += 1
    
    lst = [] # (의상종류별 의상 개수 + 1) 저장해놓을 임시 리스트
    for key, value in dic.items():
        lst.append(value + 1)
    
    answer = 1
    for i in lst:
        answer *= i
        
    return answer - 1 # 아무것도 안입는건 안되므로 한개의 경우 빼줌