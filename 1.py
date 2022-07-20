from collections import deque
from re import S

# replace 사용법 숙지하기
answer = "minseok";

answer = answer.replace(answer[0], 'e');

answer = answer.replace("e", "k", 1);

name = "abcd";

name = name[:2];

q = deque()

q.append(10);
q.append(20)

print(len(q))

print(answer)
print(name);
