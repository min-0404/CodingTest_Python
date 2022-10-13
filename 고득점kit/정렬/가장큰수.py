# permutations 사용한 풀이: 시간 초과
# lambda 사용한 풀이
def solution(numbers):

    numbers = list(map(str, numbers)) # 일단 원소들을 문자열로 변경

    numbers.sort(key = lambda x : x * 3, reverse=True) # 문자열의 자릿수 * 3배 

    return str(int("".join(numbers)))