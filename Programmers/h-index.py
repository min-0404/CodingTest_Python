def solution(citations):
    
    citations.sort(reverse=True)
    
    for idx, cit in enumerate(citations):
        if idx >= cit:
            return idx;
        
    return len(citations) # 끝까지 답이 없다면 결국 전체 길이를 반환하게 됨
