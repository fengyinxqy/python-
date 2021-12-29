lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ['a', 'b', 'c', 'd', 'e']
print(str(lst1))
print(str(lst2))
print(len(lst1))
print(max(lst1))
print(min(lst2))
print(reversed(lst2))
for i in reversed(lst1):
    print(i)

lst3 = [2, 1, 5, 4, 6, 3]
print(sorted(lst3))
print(lst3)
lst4 = sorted(lst3)
print(lst4)
print(sum(lst1))
for i, j in zip(lst1, lst2):
    print(i, j)
