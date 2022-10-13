# 참고: defaultdict 를 사용하는 방법 말고도 리스트 -> 세트 -> 다시 리스트로 변환하는 방법으로 중복제거하는 좋은 방법이 있다.
from collections import defaultdict

def solution(nums):
    answer = 0
    
    n = len(nums) / 2
    
    new_hash = defaultdict(int)
    
    
    for i in nums:
        new_hash[hash(i)] += 1
    
    if n <= len(new_hash.keys()):
        answer = n
    else:
        answer = len(new_hash.keys())


    return answer