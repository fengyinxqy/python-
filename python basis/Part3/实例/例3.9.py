tp1 = ('MUC', 'Python', 2020)
print(tp1)
print(type(tp1))
lst = ['abc', 'xyz', 123]
print(lst)
print(type(lst))
tp2 = tuple(lst)
print(tp2)
print(type(tp2))
print(tp2[-1])
tp = tp1[0]+tp2[0]
print(tp)
tp1 = tp1+tp2[0:2]
print(tp1)
