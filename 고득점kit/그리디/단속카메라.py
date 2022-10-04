def solution(routes):
    
    # 일단 진입시점으로 내림차순 정렬
    routes.sort(key=lambda x:x[0], reverse=True)
    
    # 마지막 차량의 진입시점에 카메라 한대 세움
    camera = routes[0][0]
    answer = 1 # 일단 하나 세우고 시작하느라 1로 둬야함
    
    # 나머지 차량들이 카메라 지나는지 확인
    routes = routes[1:] # 슬라이싱 꿀팁
    for route in routes:
        if route[1] >= camera: # 차량의 진출시점이 카메라보다 크다면 = 카메라 지났다는 뜻
            continue
        else: # 차량의 진출시점이 카메라보다 작다면 = 카메라 못지났다는 뜻
            camera = route[0] # 따라서 그 차량의 진입시점에 카메라를 세움
            answer += 1
    
    return answer

    def DFS(x):
        for i in range(x):
            DFS(i)
        for j in 