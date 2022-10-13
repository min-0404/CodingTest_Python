import heapq # 왠만하면 PriorityQueue 말고 heapq 써주자
def solution(scoville, K):
    
    answer = 0;
    heapq.heapify(scoville); # scoville 배열을 힙 형태로 바꿔주자
    
    while scoville[0] < K:
        
        # heappop() 사용법 숙지
        x = heapq.heappop(scoville);
        y = heapq.heappop(scoville);
        z = x + (2 * y);
        
        # heappush() 사용법 숙지
        heapq.heappush(scoville, z);
        answer += 1;
        
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우를 잘 고려
        if len(scoville) <= 1 and scoville[0] < K:
            return -1;
        
    return answer