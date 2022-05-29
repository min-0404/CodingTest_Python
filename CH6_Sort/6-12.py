n, k = map(int, input().split());

lst_A = list(map(int, input().split()));
lst_B = list(map(int, input().split()));

lst_A.sort();
lst_B.sort(reverse=True);
print(lst_A)
print(lst_B)

for i in range(k):
    if lst_A[i] < lst_B[i]:
        lst_A[i], lst_B[i] = lst_B[i], lst_A[i];
    else:
        break;
print(sum(lst_A));
