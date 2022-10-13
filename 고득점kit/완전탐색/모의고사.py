def solution(answers):
    first = [1,2,3,4,5]; # 1번째 수포자 패턴
    second = [2,1,2,3,2,4,2,5]; # 2번째 수포자 패턴
    third = [3,3,1,1,2,2,4,4,5,5]; # 3번째 수포자 패턴
    
    score = [0, 0, 0]; # 점수 저장
    result = []; 
    
    for idx, answer in enumerate(answers):
        if answer == first[idx % 5]:
            score[0] += 1;
        if answer == second[idx % 8]:
            score[1] += 1;
        if answer == third[idx % 10]:
            score[2] += 1;
    
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1);
    return result