def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)] # 일단 bride를 0으로 다 채움
    
    while bridge: # bridge가 비워질때까지
        
        answer += 1
        bridge.pop(0) # bridge의 맨 앞에서 하나씩 pop
        
        if truck_weights: # 대기중인 트럭이 남아있는 동안
            if sum(bridge) + truck_weights[0] <= weight: # 다리위에 있는 놈들의 무게 + 이제 들어올 트럭 무게 <= 하중 
                t = truck_weights.pop(0) # 대기목록에서 pop해서
                bridge.append(t) # bridge에 집어넣음
            else:
                bridge.append(0) # 하중 못버티는 경우 트럭말고 그냥 0을 집어넣음(bridge의 길이는 유지해야하므로)
                 
         
    return answer