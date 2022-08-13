def solution(N, stages):
    
    dic = {} # 각 스테이지 별로 멈춰있는 유저 수 저장
    lst = [] # 각 스테이지 별 실패율을 튜플로 저장해줄 리스트

    # defaulltdict 쓰고 싶었지만 0명인 스테이지는 기록이안되서 그냥 노가다함
    for i in range(1, N + 2):
        dic[i] = 0
    for stage in stages:
        dic[stage] += 1
    
    n = len(stages) # 유저 수
    
    for stage, value in dic.items(): #딕셔너리의 key = 스테이지, value = 멈춰있는 유저수
        if stage == N + 1: # 종결조건
            break
        if value == 0: # 0을 나누는 것은 불가능하므로 예외 처리 해줌
            lst.append((0, stage))
            continue
        fail = value / n
        n -= value
        lst.append((fail, stage))
    
    # 튜플을 원소로 가진 리스트 정렬하기
    lst.sort(key = lambda x:(-x[0], x[1])) # lambda 활용: 튜플의 첫번째 원소로 내림차순 + 튜플의 두번째 원소로 오름차순
    answer = []
    for i in lst:
        answer.append(i[1])
    return answer
        
    