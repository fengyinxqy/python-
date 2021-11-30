s = input("请输入一个字符串:")
length = len(s)
if length == 1:
    print(ord(s))
elif length == 2:
    print(s*5)
elif length == 3:
    print(s.upper())
else:
    print(s.count('ab'))
