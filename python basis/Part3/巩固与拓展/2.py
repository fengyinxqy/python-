lst = [5, 2, 3, 9, 4, 1, 8, 2, 3, 4, 7]
print("排序前:")
print(lst)
n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            t = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = t
print("排序后:")
print(lst)
