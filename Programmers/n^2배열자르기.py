# 문제 그대로 구현법 -> 시간 초과
# def solution(n, left, right):
    
#     # 첫번째 배열 구현
#     arr1 = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             m = max(i,j) + 1
#             arr1[i][j] = m
    
#     # 두번째 배열 구현 및 슬라이싱
#     arr2 = []
#     for i in arr1:
#         for j in i:
#             arr2.append(j)
#     arr2 = arr2[left: right+1]
    
#     return arr2

def solution(n, left, right):
    
    answer = []
    for i in range(left, right+1):
        answer.append(max(i // n, i % n) + 1)
        
    return answer