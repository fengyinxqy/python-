import sys
flag = 1
data = []
while(1):
    print("***************")
    print("   1、添加信息")
    print("   2、删除信息")
    print("   3、查找信息")
    print("   4、统计人数")
    print("   5、显示信息")
    print("   0、退出")
    print("***************")
    ch = int(input("请输入功能编号:"))
    if ch == 0:
        sys.exit(0)
    elif ch == 1:
        person = []
        info = input("请输入姓名，电话，工作地点(中文逗号分隔)")
        person = info.strip(" ").split("，")
        data.append(person)
    elif ch == 2:
        flag = 0
        if(len(data) == 0):
            print("通讯录为空!")
        else:
            name = input("请输入要删除的姓名:").strip(" ")
            for line in data:
                if(line[0] == name):
                    flag = 1
                    data.remove(line)
                    break
            if(flag == 0):
                print("没有找到{}的信息".format(name))
    elif ch == 3:
        flag = 0
        if(len(data) == 0):
            print("通讯录为空!")
        else:
            name = input("请输入要查找的姓名:").strip(" ")
            for line in data:
                if(line[0] == name):
                    flag = 1
                    print("查询结果为:")
                    print(line[0], line[1], line[2])
                    break
            if(flag == 0):
                print("没有找到{}的信息".format(name))
    elif ch == 4:
        if(len(data) > 0):
            p_dict = {}
            for line in data:
                p_dict[line[2]] = p_dict.get(line[2], 0)+1
            print("统计结果为:")
            for key, value in p_dict.items():
                print(key, value, "人")
        else:
            print("通讯录为空!")
    elif ch == 5:
        if len(data) > 0:
            for line in data:
                for item in line:
                    print(item, end=' ')
                print("\n")
        else:
            print("通讯录为空!")
    else:
        print("您输入的编号错误!!!")
