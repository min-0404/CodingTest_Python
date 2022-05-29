import sys

n = int(input());

array = list(map(int, input().split()));
def Search(target, start, end):
    mid = (start + end) // 2;
    if target == arr[mid]:
        return mid;
    elif target > arr[mid]:
        return Search(target, mid + 1, end);
    else:
        return Search(target, start, end - 1);

