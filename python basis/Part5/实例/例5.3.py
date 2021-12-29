
print("文本内原始信息: ")
with open('User.txt', 'r', encoding='utf-8') as f:
    userlist = []
    for line in f.readlines():
        print(line.strip('\n'))
        user = line.strip('\n').split(' ')
        userlist.append(user)
flag = 0
for item in userlist:
    if item[0] == "hello":
        item[1] == "123456"
        flag = 1
if flag == 0:
    newUser = ["hello", "123456"]
    userlist.append(newUser)
print("修改后文本信息: ")
with open('User.txt', 'w', encoding='utf-8') as f_w:
    for item in userlist:
        f_w.write(item[0]+" "+item[1]+'\n')
        print(item[0]+" "+item[1])
if flag == 1:
    print("hello用户已存在,密码已修改!")
else:
    print("hello用户不存在,已创建此用户")
