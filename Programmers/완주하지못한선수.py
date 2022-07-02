# Hash 이용한 방법
def solution(participant, completion):
    
    dict = {}
    sum = 0;
    
    for i in participant:
        dict[hash(i)] = i;
        sum += hash(i);
    for i in completion:
        sum -= hash(i);
        
    return dict[sum];

# Counter 이용한 방법 (딕셔너리와 비슷한데, key 는 이름, value 는 값)
# import collections
# def solution(participant, completion):

    # answer = collections.Counter(participant) - collections.Counter(completion)
    
    # return list(answer.keys())[0];