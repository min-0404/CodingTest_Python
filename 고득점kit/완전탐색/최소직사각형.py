def solution(sizes):
    
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    
    max_row = sizes[0][0]
    max_col = sizes[0][1]
    for i in sizes:
        if i[0] > max_row:
            max_row = i[0]

    for i in sizes:
        if i[1] > max_col:
            max_col = i[1]
    
    return max_row * max_col