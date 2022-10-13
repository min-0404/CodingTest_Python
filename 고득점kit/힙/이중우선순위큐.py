import heapq
def solution(operations):
    
    q = []
    for i in operations:
        
        # 삽입 연산
        if i[0] == 'I':
            number = i[2:]
            number = int(number)
            heapq.heappush(q, number)
            
        # 삭제 연산
        else:
            # 최솟값 삭제 -> 최소힙(디폴트)에서 pop
            if i == 'D -1':
                if len(q) == 0:
                    continue
                heapq.heappop(q)
            # 최댓값 삭제 -> 최대힙 만들기 귀찮으니깐 그냥 sort 해서 pop 해버리자
            else:
                if len(q) == 0:
                    continue
                q.sort()
                q.pop()
            
    # 출력값 미무리      
    answer = []
    if len(q) == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(q))
        answer.append(min(q))
    return answer
            