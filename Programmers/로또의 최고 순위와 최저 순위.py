# 너무 쉬워서 복습 필요 없음
def solution(lottos, win_nums):
    answer = []
    cnt = 0;
    cnt_0 = 0;
    for i in lottos:
        if i in win_nums:
            cnt += 1;
        if i == 0:
            cnt_0 += 1;
    best = cnt + cnt_0;
    worst = cnt;
    
    if best == 6:
        answer.append(1);
    elif best == 5:
        answer.append(2);
    elif best == 4:
        answer.append(3);
    elif best == 3:
        answer.append(4);
    elif best == 2:
        answer.append(5);
    else:
        answer.append(6);
        
    if worst == 6:
        answer.append(1);
    elif worst == 5:
        answer.append(2);
    elif worst == 4:
        answer.append(3);
    elif worst == 3:
        answer.append(4);
    elif worst == 2:
        answer.append(5);
    else:
        answer.append(6);
            
    return answer