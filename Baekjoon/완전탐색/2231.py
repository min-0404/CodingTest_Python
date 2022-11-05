# 분해합: 너무 단순한 for문 완전탐색: 다시 볼 필요도 없음
import sys
n = int(input())

for i in range(1, n + 1):
    s = 0
    s += i
    lst = list(str(i))
    lst = list(map(int, lst))
    s += sum(lst)
    if s == n: # 생성자 찾으면 이게 가장 작은 것이므로 프로그램 끝내버림
        print(i)
        sys.exit() 

print(0) # 여기까지 왔다는 것은 = 생성자 없다는 뜻 = 0출력
