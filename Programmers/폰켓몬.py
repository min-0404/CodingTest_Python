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