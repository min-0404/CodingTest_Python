from collections import defaultdict
def solution(survey, choices):
    dic = {} # defaultdict 쓰려고 했지만 포기
    dic['R'] = 0
    dic['T'] = 0
    dic['C'] = 0
    dic['F'] = 0
    dic['J'] = 0
    dic['M'] = 0
    dic['A'] = 0
    dic['N'] = 0

    n = len(survey)
    for i in range(n):
        if choices[i] == 1:
            dic[survey[i][0]] += 3
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 7:
            dic[survey[i][1]] += 3
    answer = ""
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'    
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'    
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'    
           
    return answer