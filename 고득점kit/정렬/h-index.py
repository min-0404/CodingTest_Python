def solution(citations):
    
    citations.sort(reverse=True)
    
    # idx 가 value 보다 커질때 H-Inedx 라고 부른다.
    for idx, cit in enumerate(citations):
        if idx >= cit:
            return idx;
        
    return len(citations)
