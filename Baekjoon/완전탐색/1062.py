# 가르침: 완전 탐색
import sys
n, k = map(int, input().split())

# k가 5이하라면 어떤 단어도 읽을 수 없음
if k < 5:
    print(0)
    sys.exit()
    
# k가 26(즉, 모든 알파벳)이라면 모든 단어를 읽을 수 있음
elif k == 26:
    print(n)
    sys.exit()


answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0 for _ in range(26)]

for c in ('a', 'c', 'i', ' n', 't'):
    learn[ord(c) - ord('a')] = 1

result = set() # 배운 단어를 저장하는 세트
set.update()
def DFS(idx, cnt):

    # 종결조건
    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    
    for i in range(start, 26):
        if i not in result: # 중복 제거
            result.append(i)
            DFS(i+1)
            result.pop()
        

            