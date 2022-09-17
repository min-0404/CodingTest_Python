def solution(n):
    
    lst = []
    n = str(n) # n = "12345"
    
    for i in n:
        lst.append(int(i)) # lst = [1,2,3,4,5]
    
    # sort() 자체가 reverse() 보다 훨씬 비효율적 -> 굳이 정렬 사용할 이유가없음
    #lst.sort(reverse = True)
    
    lst.reverse()
    
    return lst
