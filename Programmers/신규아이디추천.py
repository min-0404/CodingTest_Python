# replace() 사용법과 문자열 슬라이싱에 익숙해지자
def solution(new_id):
    answer = ''
    
    # step_1: 전체 문자 소문자로 변환
    new_id = new_id.lower()
    
    #step_2: 소문자거나, 숫자거나, 해당 기호들이면 추가
    for id in new_id:
        if id.islower() or id.isdigit() or id in ['-', '_', '.']:
            answer += id
    
    # step_3: 마침표(.) 연속된 경우 하나로 바꿔버리기
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # step_4: 제일 앞이나 뒤가 마침표라면 슬라이싱 사용해서 없애버리기
    if answer[0] == '.':
        if len(answer) >= 2:
            answer = answer[1:]
    
    if answer[-1] == '.':
        answer = answer[:-1]
        
    # step_5: 문자열 공백이라면 a로 바꿔버리기
    if answer == '':
        answer = 'a'
        
    # step_6: 16자 이상이라면 뒤에 다 잘라버리기
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1] # 유용한 슬라이싱 활용법
            
    # step_7: 2글자 이하라면 3글자로 늘려주기
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer