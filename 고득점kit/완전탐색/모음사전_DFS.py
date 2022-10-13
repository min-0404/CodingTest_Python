    
def solution(word):
    
    def DFS(idx):
        nonlocal answer, dic
        
        # 종결조건
        if idx == 5:
            return
        
        # 수행동작
        for i in words:
            answer.append(i)
            dic.append("".join(answer))
            DFS(idx + 1)
            answer.pop()

    words = ['A', 'E', 'I', 'O', 'U']
    answer = []
    dic = []
    DFS(0)
    return dic.index(word) + 1
