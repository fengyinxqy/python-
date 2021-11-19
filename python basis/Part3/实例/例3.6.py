lst = ['b', 3, 'd', 2, 'c', 1, 'a', 5, 4, 'e']
print(lst)
lst.reverse()
print(lst)
lst.append('f')
print(lst)
lst0 = [0, 6, 'g']
lst.extend(lst0)
print(lst)
lst.insert(0, 0)
print(lst)
print(lst.count(0))
print(lst.index(0))
print(lst.index(5))
