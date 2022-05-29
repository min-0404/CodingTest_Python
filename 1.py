lst = [5, 3, 1, 2];



for i in range(len(lst)):
    min_idx = i;
    for j in range(i, len(lst)):
        if lst[min_idx] > lst[j]:
            min_idx = j;
    lst[i], lst[min_idx] = lst[min_idx], lst[i];

print(lst);


