from collections import defaultdict # 딕셔너리 사용시, 왠만하면 defaultdictionary 사용하자

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report = set(report); # 신고내역의 중복 제거를 위해 set로 바꿔주기
    
    reportUsers = defaultdict(set); # "신고한" 유저 목록 (key = 아이디 value = 세트)
    reportedUsers = defaultdict(int); # "신고당한" 유저목록 (key = 아이디 value = 신고당한 횟수)
    suspended = []; # 신고당한 유저 리스트
    
    for i in report:
        fro_m, to = i.split() # fro_m = 신고한유저, to = 신고당한유저
        
        reportUsers[fro_m].add(to);  # 신고한 유저에 신고당한 유저 추가
        reportedUsers[to] += 1; # 신고당한 유저목록에 당한 횟수 추가
        
        if reportedUsers[to] == k: # k 도달시 suspended 리스트에 해당 유저 추가
            suspended.append(to); 

    for i in range(len(id_list)): # 밴 먹은 유저들을 신고한 유저들에게 메일 보내고, 그 횟수를 answer 에 기록
        for j in suspended:
            if j in reportUsers[id_list[i]]:
                answer[i] += 1;
                
    return answer