def solution(numlist, n):
    
    # step1: (원소와 n의 차이, 원소) 형태로 answer에 저장
    answer = []
    for i in numlist:
        result = abs(i - n)
        answer.append((result, i))
    
    # step2: 원소와 n의 차이는 오름차순, 원소는 내림차순 정렬
    answer.sort(key = lambda x :(x[0], -x[1]))
    
    # step3: answer에서 원소만 빼내서 저장
    answer2 = []
    for i in answer:
        answer2.append(i[1])

    return answer2