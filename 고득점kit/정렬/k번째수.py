def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0] # 시작
        j = command[1] # 끝
        k = command[2] # k번째 수
        
        new_array = array[i-1 : j] # 슬라이싱
        new_array.sort() # 정렬
        answer.append(new_array[k-1]) # k번째 수 찾아서 answer에 추가
        
    return answer