# 일곱 난쟁이: 전형적인 완전 탐색 -> combiantations 유형
# 9명의 주어진 난쟁이들 중 합쳐서 100을 만족하는 7난쟁이의 경우 아무거나 찾으면 됨
import sys
def DFS(start):

    # 종결조건
    if sum(result) == 100 and len(result) == 7: 
        result.sort()
        for i in result:
            print(i)
        sys.exit()

    # 수행동작
    for i in range(start, 9): # start부터 시작
         if lst[i] not in result: # 중복 제거
            result.append(lst[i])
            DFS(i+1) # DFS(i + 1) 인 것 항상 주의하자
            result.pop()



# 9명의 난쟁이 데이터 저장
lst = []
for _ in range(9):
    x = int(input())
    lst.append(x)

# 결과처리
result = []
DFS(0)
