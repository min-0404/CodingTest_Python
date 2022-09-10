# 주의할점: 리스트나 덱을 이용해서 pop하는 방식으로 진행하면 효율성 에러가 뜸
# 따라서 인덱싱을 증가/감소 하는 방식으로 진행시켜야 효율성 에러 안뜸
def solution(people, limit):
    
    answer = 0 
    people.sort()
    
    # 시작인덱스부터 증가시키고, 마지막 인덱스부터 감소시키는 방식으로 진행
    start = 0
    end = len(people) - 1
    
    while start <= end: # 
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1
    return answer