# permutations 사용한 풀이: 시간 초과
'''
from itertools import permutations
def solution(numbers):
    
    # 일단 모든 원소들을 문자열로 바꾸고
    numbers = list(map(str, numbers))
    
    perm = list(permutations(numbers, len(numbers)))
    
    # 문자열을 조인시키며 자연스럽게 정수로 변환해줌
    answer = []
    for p in perm:
        answer.append(int(''.join(p)))

    # max() 이용해 최댓값 반환
    return str(max(answer))
'''

# lambda 사용한 풀이
def solution(numbers):

    numbers = list(map(str, numbers))

    numbers.sort(key = lambda x : x*3, reverse=True)

    return str(int("".join(numbers)))
