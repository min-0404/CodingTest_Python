from itertools import product
def solution(word):
    
    words = ['A', 'E', 'I', 'O', 'U']
    
    result = []
    for i in range(1, 6):
        lst = list(product(words,repeat=i))
        for j in lst:
            result.append("".join(j))
    result.sort()
    
    return result.index(word) + 1