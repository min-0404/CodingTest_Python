def solution(phone_book):
    
    phone_book.sort() # 정렬이 핵심 -> for문으로 phone_book 탐색하면서 i와 i+1만 비교해도 될 수 있게해줌
    
    for i in range(len(phone_book)-1):
        
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            
            return False
    return True
