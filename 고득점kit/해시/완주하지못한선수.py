# Hash 이용한 방법
from collections import Counter
def solution(participant, completion):

    dict = {}
    sum = 0
    
    # 참여자의 해시값 sum 에 더함
    for i in participant:
        dict[hash(i)] = i
        sum += hash(i)
        
    # 완주자의 해시값 sum 에서 뺌
    for i in completion:
        sum -= hash(i)
        
    # sum = 유일하게 완주못한자의 해시값 -> 이 sum으로 딕셔너리에서 탐색
    return dict[sum]

# Counter 이용한 방법 (딕셔너리와 비슷한데, key 는 이름, value 는 값)
# import collections import Counter
# def solution(participant, completion):

    # answer = collections.Counter(participant) - collections.Counter(completion)
    
    # return list(answer.keys())[0];
