def solution(n, costs):
    
    costs.sort(key = lambda x : x[2])
    connected = set()
    set.add(costs[0][0])
    set.add(costs[0][1])
    
    answer = 0
    answer += costs[0][2]
     
    while len(connected) != n:
        for i in range( )