def solution(keyinput, board):
    
    answer = [0,0]
    
    row = (board[0] - 1) / 2
    col = (board[1] -1) / 2 
    
    for key in keyinput:
        # 일단 이동
        if key == 'left':
            answer[0] -= 1
        elif key == 'right':
            answer[0] += 1
        elif key == 'up':
            answer[1] += 1
        else:
            answer[1] -= 1
            
        # x축 벗어날 시
        if answer[0] > row:
            answer[0] = row
        elif answer[0] < row * -1:
            answer[0] = row * -1 
        
        # y축 벗어날 시    
        if answer[1] > col:
            answer[1] = col
        elif answer[1] < col * -1:
            answer[1] = col * -1
            
    return answer