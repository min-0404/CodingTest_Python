def solution(genres, plays):
    
    # tmp 생성: [[장르, 재생횟수, 고유번호], [], ...]
    tmp = []
    for i in range(len(genres)):
        tmp.append((genres[i], plays[i], i))
    tmp.sort(key = lambda x : (x[0], -x[1], x[2]))

    # dic 생성: {장르: 노래들 재생횟수 합, ...}
    dic = {}
    for i in tmp:
        if i[0] not in dic:
            dic[i[0]] = i[1]
        else:
            dic[i[0]] += i[1]
    
    # dic을 value 값으로 정렬하는법
    dic = sorted(dic.items(), key = lambda x : -x[1])
    
    # answer 생성
    answer = []
    for i in dic:
        cnt = 0
        for j in tmp:
            if i[0] == j[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(j[2])
    return answer