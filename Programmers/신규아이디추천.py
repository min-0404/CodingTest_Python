# replace() 사용법과 문자열 슬라이싱에 익숙해지자
def solution(new_id):
    answer = ''
    
    # step_1
    new_id = new_id.lower()
    
    #step_2
    for id in new_id:
        if id.islower() or id.isdigit() or id in ['-', '_', '.']:
            answer += id
    
    # step_3
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # step_4
    if answer[0] == '.':
        if len(answer) >= 2:
            answer = answer[1:]
    
    if answer[-1] == '.':
        answer = answer[:-1]
        
    # step_5
    if answer == '':
        answer = 'a'
        
    # step_6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    # step_7
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer