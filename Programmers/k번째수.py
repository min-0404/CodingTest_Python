def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0];
        j = command[1];
        k = command[2];
        
        new_array = array[i-1 : j];
        
        # sort() 와 sorted()의 차이점 숙지하기
        # 배열.sort(): 해당 배열 정렬시키기
        # 배열.sorted(): 해당 배열을 정렬한 값 반환 (해당 배열자체가 정렬되는게 아님)
        new_array.sort(reverse = False);
        
        answer.append(new_array[k-1]);
        
    return answer