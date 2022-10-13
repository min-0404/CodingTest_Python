# Permutations 이용
from itertools import permutations

# 소수 판별 함수
def sosu(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):

    numbers = list(numbers) # 일단 문자열을 리스트로 바꿔줌
    
    perm  = []
    for i in range(1, len(numbers) + 1):
        perm += list(permutations(numbers, i))
    
    # join() 함수 활용 
    answer = []
    for p in perm:
        answer.append(int("".join(p)))

    # 중복 제거를 위해 소수판별 결과를 리스트에 저장한 다음, 
    result = []
    for i in answer:
        if sosu(i):
            result.append(i)
    
    # 세트로 바꿔서 중복제거
    result = set(result)
    
    # 중복제거된 개수를 반환
    return len(result)

