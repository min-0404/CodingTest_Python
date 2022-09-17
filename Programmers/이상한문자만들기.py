# 이중 for문 사용시 효율성통과 못함
# def solution(s):
#     answer = ''
    
#     lst = s.split()
    
#     for word in lst:
#         for i in range(len(word)):
#             if i == 0 or i % 2 == 0:
#                 answer += word[i].upper()
#             elif i % 2 == 1:
#                 answer += word[i].lower()
#         answer += " "
    
#     answer = answer.rstrip()
#     return answer

# 노가다식 선형 탐색으로 해결해야함
def solution(s):
    
    answer = ''
    cnt = 0 # s전체 인덱스 카운트용
    tmp = 0 # 각 word의 인덱스 카운트용
    
    while 1:
        
        if cnt == len(s): # 종결조건
            break
            
        if s[cnt] == ' ': # 공백일 경우
            answer += ' '
            tmp = 0 # tmp를 다시 0으로 초기화
            cnt += 1
            continue
            
        if tmp == 0:  # word의 인덱스 = 0 일 경우
            answer += s[cnt].upper()
            cnt += 1
            tmp += 1
            
        elif tmp % 2 == 0: # word의 인덱스 = 짝수 일 경우
            answer += s[cnt].upper()
            cnt += 1
            tmp += 1
            
        elif tmp % 2 == 1: # word의 인덱스 = 홀수 일 경우
            answer += s[cnt].lower()
            cnt += 1
            tmp += 1

        
    return answer