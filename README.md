7<!-- TOC -->

- [Python 学习笔记](#python-学习笔记)
  - [第一章 Python 概述](#第一章-python-概述)
  - [第二章 程序基本结构](#第二章-程序基本结构)
    - [2.1 顺序结构](#21-顺序结构)
      - [2.1.1 程序的 IPO 模型](#211-程序的-ipo-模型)
      - [2.1.2 输入和输出](#212-输入和输出)
    - [2.2 分支结构](#22-分支结构)
      - [2.2.1 单分支结构](#221-单分支结构)
      - [2.2.2 多分支结构](#222-多分支结构)
      - [2.2.3 多分支结构](#223-多分支结构)
    - [2.3 循环结构](#23-循环结构)
      - [2.3.1 while 语句](#231-while-语句)
      - [2.3.2 for 循环语句](#232-for-循环语句)
      - [2.3.3 循环的嵌套](#233-循环的嵌套)
  - [第 3 章 列表、元组和字典](#第-3-章-列表元组和字典)
    - [3.1 组合数据类型](#31-组合数据类型)
    - [3.2 列表](#32-列表)
      - [3.2.1 列表的基本操作](#321-列表的基本操作)
      - [3.2.2 列表常用操作符](#322-列表常用操作符)
      - [3.2.3 列表常用函数或方法](#323-列表常用函数或方法)
      - [巩固与拓展:](#巩固与拓展)
    - [3.3 元组](#33-元组)
    - [3.4 字典](#34-字典)
      - [3.4.1 字典的基本操作](#341-字典的基本操作)
      - [3.4.2 字典的内置函数和方法](#342-字典的内置函数和方法)
    - [3.5 应用实例](#35-应用实例)
    - [第 4 章 函数](#第-4-章-函数)
      - [4.1 函数的定义和调用](#41-函数的定义和调用)
      - [4.2 函数的参数传递](#42-函数的参数传递)
      - [4.3 变量的作用域](#43-变量的作用域)
      - [4.4 函数模块化编程](#44-函数模块化编程)
      - [4.5 应用实例](#45-应用实例)
    - [第 5 章 文件](#第-5-章-文件)
      - [5.1 文件的打开和关闭操作](#51-文件的打开和关闭操作)
      - [5.2 文件的读写操作](#52-文件的读写操作)
      - [5.3 文本文件操作](#53-文本文件操作)
      - [5.4 CSV 文件的读写](#54-csv-文件的读写)
      - [5.5 应用实例](#55-应用实例)
    - [第 6 章 面向对象编程](#第-6-章-面向对象编程)
      - [6.1 类和对象的概念](#61-类和对象的概念)
        - [6.1.1 类和对象](#611-类和对象)
        - [6.1.2 对象属性和方法](#612-对象属性和方法)
        - [6.1.3 构造方法和非构造方法](#613-构造方法和非构造方法)
        - [6.1.4 类的属性和方法](#614-类的属性和方法)

<!-- /TOC -->

# Python 学习笔记

2021/11/12 重新开始学习 Python 基础

`print("Hello World!") //输出 hello world`

## 第一章 Python 概述

略

## 第二章 程序基本结构

### 2.1 顺序结构

#### 2.1.1 程序的 IPO 模型

I: 输入
P: 处理
O: 输出

> 例 1:输入两个数求平均值

```
num1 = input("输入第一个数:")
num2 = input("输入第二个数:")
avg_num = (float(num1)+float(num2))/2
print(avg_num)
```

#### 2.1.2 输入和输出

> 例 2.2 输入同学姓名和成绩，输出姓名和成绩的值及其值的类型

```
name = input("请输入姓名: ")
score = input("请输入成绩: ")
print(name, score)
print(type(name), type(score))

```

知识要点：

变量：变量是一个标识符，要遵循两个规则 1.只能由字母、数字和下划线组成 2.不能由数字开头。

输入：input()函数，里面可以填写输入提示

数据类型：Python3 中支持 6 中数据类型:数字、str(字符串)、list(列表)、tuple(元组)、set(集合)、dict(字典)

数字类型：int(整型)、float(浮点型)、bool(布尔型)、complex(复数型)

输出：print()函数，

> 例 2.3 假设标准体重(KG)的计算公式为:体重=[身高(厘米)-100]x0.9,请根据输入的身高计算一个人的体重

```
length = int(input("请输入身高(厘米): "))
weight = (length-100)*0.9
print("身高为:%d厘米,标准体重为:%fkg" % (length, weight))
```

知识点：

类型转换：int(),float(),str()三种之间的互相转换，其中 int()转换是向下取整

格式化输出：和 C 语言中的格式化输入一样，保留小数点，占用列宽都一样
print("格式串"%(输出对象 1，输出对象 2))

巩固与拓展：

（1）从键盘输入 3 名同学的数学成绩，输出平均分。要求平均分用 3 种形式输出:保留 2 位小数的结果、四舍五入的结果（例如 3.62 得 4）和向下取整（例如 3.62 得 3）的结果

```
score1 = int(input("第一位同学的成绩："))
score2 = int(input("第二位同学的成绩："))
score3 = int(input("第三位同学的成绩："))
avg_score = (float(score1+score2+score3))/3
print("平均成绩:%.2f" % (avg_score)) #保留两位小数
print("平均成绩:%d" % (round(avg_score))) #四舍五入
print("平均成绩:%d" % (int(avg_score))) #向下取整

```

（2）从键盘输入两个正整数 a 和 b，输出 a 除以 b 的商和余数。

```
a = int(input("请输入两个正整数:"))
b = int(input("请输入两个正整数:"))
print("商为:%d" % (divmod(a, b)[0]))
print("余数为:%d" % (divmod(a, b)[1]))
```

（3）从键盘输入一个三位数的正整数，输出其各位数字反转后得到的三位数

```
num1 = input("请输入一个三位数:")
num2 = num1[::-1]
print(num2)

```

（4）将 a 和 b 的值交换过来。例如:交换前:a ＝ 2，b ＝ 3；交换后:a ＝ 3，b ＝ 2

```
num1 = int(input("请输入一个整数:"))
num2 = int(input("请输入一个整数:"))
print("交换前:(%d,%d)" % (num1, num2))
t = num1
num1 = num2
num2 = t
print("交换后:(%d,%d)" % (num1, num2))
```

（5）小明练习游泳，有一天他从 a 时 b 分一直游泳到当天的 c 时 d 分（时间按 24 小时制）请计算小明这天游泳的时长是多少小时多少分钟？

```
a, b = eval(input("开始游泳的时间："))
c, d = eval(input("结束游泳的时间："))
minutes = (c-a-1)*60+(60-b)+d
print("小明游了%d小时%d分钟" % (divmod(minutes, 60)[0], divmod(minutes, 60)[1]))

```

### 2.2 分支结构

#### 2.2.1 单分支结构

> 从键盘输入两个整数，按从大到小的顺序输出

```
num1 = int(input("请输入一个整数:"))
num2 = int(input("请输入一个整数:"))
if num1 < num2:
    t = num1
    num1 = num2
    num2 = t
print("从大到小为:%d,%d" % (num1, num2))
```

知识点:

1.单分支——if 语句

单分支结构代码块执行次数为 1 次或 0 次

2.关系表达式

表达式的值一定是布尔值(True 或 False)

#### 2.2.2 多分支结构

> 例 2.5 如果年份能被 100 整除但不能被 4 整除或者能被 400 整除则是闰年，否则，不是闰年，从键盘输入一个年份，判断其是不是闰年。

```
year = int(input("请输入一个年份:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d年是闰年" % (year))
else:
    print("%d年不是闰年" % (year))
```

知识点：

1. 双分支——if...else 语句 两个都必须加:

2. 逻辑运算符及表达式

   Python 中逻辑运算符有三个(not>and>or)

#### 2.2.3 多分支结构

> 例 2.6 从键盘输入一个字符串(全部由字母字符组成)，如果串的长度为 1，则输出字符的 ASCLL 码，如果串长度为 2，则将字符重复 5 次并输出，如果串长度为 3，则将字符串中的所有字符大写并输出，如果串长度大于 3，统计子串'ab'在字符串中出现的次数

```
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
```

知识点：

1. order()函数：返回字符 ASCLL 码
2. 输出 5 次可以写成 s\*5,其他次数也一样
3. 将所有字母大写是 s.upper()
4. 统计子串出现的次数用 s.count()
5. ......

巩固与拓展

（1）编写程序，计算长方形、圆和梯形的面积。程序运行时，显示如下功能列表:
a、计算长方形的面积
b、计算圆的面积
c、计算梯形面积
例如，输入 a，计算长方形的面积。输入 b，计算圆的面积。输入 c，计算梯形面积。输入其他值则报错。计算面积前，根据需要输入图形的尺寸。比如计算长方形面积，需要输入长和宽的值。计算圆的面积，要输入半径值。

```
import math
print("a、计算长方形的面积\nb、计算圆的面积\nc、计算梯形面积\n")
s = input("请选择要使用的功能:")
if s == 'a':
    x = float(input("请输入长方形的长:"))
    y = float(input("请输入长方形的宽:"))
    print("长方形的面积为:%.2lf" % (x*y))
elif s == 'b':
    r = float(input("请输入半径:"))
    print("半径为:%lf的圆的面积为:%.2lf" % (r, math.pi*r*r))
else:
    x = float(input("请输入梯形的上底:"))
    y = float(input("请输入梯形的下底:"))
    z = float(input("请输入梯形的高:"))
    print("该梯形的面积为:%.2lf" % ((x+y)*z/2))
```

（2）输入三角形的三条边，判断是否能构成三角形。

```
a = float(input("请输入三角形的一个边:"))
b = float(input("请输入三角形的一个边:"))
c = float(input("请输入三角形的一个边:"))
if a+b > c and a+c > b and b+c > a:
    print("这三个边可以构成三角形")
else:
    print("这三个边不能构成三角形")
```

（3）已知 2020 年 9 月 1 日是周二，计算经过 n 天后是星期几，n 从键盘输入。

```
print("2020 年 9 月 1 日是周二")
n = int(input("请输入n:"))
if n % 7 == 0:
    print("%d天后是周二" % (n))
elif n % 7 == 1:
    print("%d天后是周三" % (n))
elif n % 7 == 2:
    print("%d天后是周四" % (n))
elif n % 7 == 3:
    print("%d天后是周五" % (n))
elif n % 7 == 4:
    print("%d天后是周六" % (n))
elif n % 7 == 5:
    print("%d天后是周日" % (n))
else:
    print("%d天后是周一" % (n))
```

（4）从键盘输入 2 个字符串，将其拼接在一起，去除串中的空格字符并输出。

```
s1 = input("请输入一个字符串:")
s2 = input("请输入一个字符串:")
s3 = s1+s2
print(s3.replace(" ", ""))
```

（5）从键盘输入一个字符串，如果串中只有数字字符，则将字符串转成整数输出，如果串中只有字母字符，则将字符串中的首字母大写输出，否则，输出串的长度。

```
s = input("请输入一个字符串:")
if s.isdecimal() is True:
    print(int(s))
elif s.isalpha() is True:
    print(s.capitalize())
else:
    print(len(s))
```

### 2.3 循环结构

在 python 中是没有 do while 的

#### 2.3.1 while 语句

> 例 2.7 假设程序运行时，需要输入密码，如果密码正确，显示“欢迎使用本系统”，否则，显示“c”，知道密码输入正确，结束程序。(密码设为:admin2021)

```
password = "admin2021"
password1 = input("请输入密码:")
while password1 != password:
    password1 = input("密码错误，请重新输入!\n")
print("欢迎使用本系统")
```

知识点:

1.  while 语句:

    > while 条件：
    >
    > 代码块

2.  循环次数必须是有限的，不能死循环
3.  break 和 continue 语句

    break:结束所在层的所有循环

    continue:结束所在层的一次循环，转而执行下一次循环

#### 2.3.2 for 循环语句

> 例 2.8 假设登录一个系统需要输入密码，但只有 5 次机会。如果第 1 次输入不正确，显示“密码错误！还剩 4 次机会！”和“请重新输入:，第 2 次还不对，显示“密码错误！还剩 3 次机会！”和“请重新输入:”。如果密码正确，显示欢迎使用本系统！”，结束程序。如果 5 次输入都错误，则显示“密码错误，次数用完，请下次再试！”结束程序。（假设密码为 1234xyz）

```
key = "1234xyz"
password = input("请输入密码:")
for i in range(1, 6):
    if password == key:
        print("欢迎使用本系统!")
        break
    else:
        if i < 5:
            print("密码错误！还剩%d次机会！" % (5-i))
            password = input("请重新输入:")
        else:
            print("密码错误，次数用完，请下次再试！")
```

知识点:

1.  range()函数

    语法格式:range(start=0, end, step=1)

2.  for 语句

    格式:for 变量 in 序列:

            代码块

#### 2.3.3 循环的嵌套

> 例 2.9 利用 1、2、3.....、6 共六个数字组成一个 2 位数，个位只能取 1~3 共 3 个数字，能组成多少个无重复数字的 2 位数？输出这些 2 位数，每五个数一行。

```
count = 0
for i in range(1, 7):
    for j in range(1, 4):
        if i != j:
            print(i*10+j, end="   ")
            count += 1
            if count % 5 == 0:
                print("")
print("总共有:%d个" % (count))
```

巩固与拓展

（1）输出 1 ～ 100（包括）之间能被 3 但不能被 7 整除的所有整数。

```
for i in range(1, 101):
    if i % 3 == 0 and i % 7 != 0:
        print(i, end="  ")

```

（2）编写程序，输出 100 ～ 2000 之间最大的 10 个素数。

```
sushu = []
for i in range(100, 2001):
    for j in range(2, i):
        if i % j == 0:
            break
    if i == j+1:
        sushu.append(i)
print(sushu[-10:])
```

（3）求出两个整数 m~n 之间所有整数各个位上的奇数数字之和。例如 m ＝ 7，n ＝ 12，则 m~n 之间的所有整数是:7、8、9、10、11、12，各个位上的奇数数字之和 7 ＋ 9 ＋ 1 ＋ 1 ＋ 1 ＋ 1 ＝ 20

```
m = int(input("请输入一个整数:"))
n = int(input("请输入一个整数:"))
sum = 0
for i in range(m, n+1):
    if i < 10:
        if i % 2 != 0:
            sum += i
    else:
        if i % 2 != 0:
            sum += i % 10
            i = i//10
            if i % 2 != 0:
                sum += i
        else:
            i = i//10
            if i % 2 != 0:
                sum += i
print(sum)
```

（4）韩信点兵。如果从 1 到 5 报数，最末一个兵报数为 1，从 1 到 6 报数，最末一个兵报数为 5，从 1 到 7 报数，最末一个士兵报数为 4 ,从 1 到 11 报数，最末一个兵报数为 10，请帮韩信计算他至少有多少兵。

```
i = 0
while(1):
    if i % 5 == 1 and i % 6 == 5 and i % 7 == 4 and i % 11 == 10:
        print(i)
        break
    i += 1
```

算术游戏:

```
import sys
import random
for i in range(3):
    psd = input("请输入密码")
    if psd.strip(" ") == "123":
        break
    else:
        if(i == 2):
            print("密码错误3次,程序停止运行!")
            sys.exit(1)
        else:
            print("密码错误,请重新输入!")
signs = ['+', '-', '*', '//']
right = 0
error = 0
for i in range(10):
    op1 = random.randint(0, 100)
    op2 = random.randint(0, 100)
    sign = random.choice(signs)
    if sign == '+':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1+op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1+op2))
            error += 1
    elif sign == '-':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1-op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1-op2))
            error += 1
    elif sign == '*':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1*op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1*op2))
            error += 1
    if sign == '//':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1//op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1//op2))
            error += 1
print("答对的次数: ", right, "答错的次数: ", error)
```

## 第 3 章 列表、元组和字典

### 3.1 组合数据类型

1. 序列类型

序号访问单个元素是直接使用编号如 list[0],首元素是从 0(-n)开始的，而不是 1，末元素编号是 n-1(也可以是-1)

切片操作:比如说 list[1:8]就是第二个元素到第八个元素(7)不包含第九个元素

### 3.2 列表

#### 3.2.1 列表的基本操作

> 例 3.1 创建列表

```
""" 创建列表 """

list1 = []
list2 = ["MUC", "Python", 1, 2, 3]
list3 = list("Hello!Python")

print(list1)
print(list2)
print(list3)
```

知识点:

1. 使用方括号将一组 Python 对象括起来,各个对象之间用逗号分隔,就创建了一个列表,也可以创建一个空列表
2. 可以使用 list()函数创建列表,如果带的参数是字符串,则会将字符串中的每个字符解析成列表的元素

> 例 3.2 访问列表

```
""" 访问列表 """
lst = ["MUC", "Python", 1, 2, 3, "Hello"]
print(lst[1])  # 输出第二个元素
print(lst[1:3])  # 输出第二，第三两个元素
print(lst[0: 5: 2])  # 从第一个到第第五个元素之间，步长为2输出，1,3,5三个元素
```

知识点:

1. 列表元素使用列表名加下标进行访问，列表的首元从下标 0 开始依次递增；也可以从末元素开始倒序进行标示，末元素下标为-1 倒序依次往前递减。
2. 访问列表元素时可以指定开始位置和结束位置，从而实现多个元素的访问和抽取，这个操作称为切片操作，在切片操作时还可以在切片范围后指定步长。
3. 列表的切片操作时，包含指定的第一个元素，不包含区间最后一个元素；若从指定元素一直取到列表最后一个元素，可以省略区间范围后面的数字；不能够指定超出列表范围的数字，否则就会出错。

> 例 3.3 更新和删除列表中的元素

```
lst = ["MUC", "Python", 1, 2, 3, "Hello"]
print(lst)
lst[2:5] = 4, 5, 6
print(lst)
lst[2] = 'Sec'
print(lst)
del lst[2]
print(lst)
lst.append('Sec')
print(lst)
lst.pop()
print(lst)
lst.pop(0)
print(lst)
```

知识点:

1. 可以使用下标方法更新指定列表元素的值，也可以更新切片元素的多个值。
2. 可以使用 appendo 方法追加新的列表元素，追加的元素放在列表的最后。
3. 删除列表中元素:
   1. 使用 del 语句
   2. 使用 remove()方法删除指定内容
   3. 使用 pop()方法删除指定位置元素，如不指定则为删除末尾元素

#### 3.2.2 列表常用操作符

> 例 3.4 列表操作符

```
lst1 = ['hello', 'hi', 'hiya']
lst2 = [1, 2, 3]
print(lst1+lst2)
lst3 = lst2*3
print(lst3)
print(lst1*2)
print('hiya' in lst1)
print('howday' not in lst1)
print('hi' in lst2)

结果:
['hello', 'hi', 'hiya', 1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
['hello', 'hi', 'hiya', 'hello', 'hi', 'hiya']
True
True
False
```

知识点:

1. 列表的连接: 使用+直接连接，但是这种方法的代价比较大，建议使用 extend()
2. 列表操作符

| 操作符          | 功能描述       |
| --------------- | -------------- |
| >,<,>=,<=,==,!= | 对象值比较     |
| is, not is      | 对象值身份比较 |
| not, or, and    | 布尔运算符     |
| in, not in      | 成员关系运算符 |
| +               | 连接操作符     |
| \*              | 重复操作符     |
| [],[:],[::]     | 切片操作符     |

3. 两个列表比较时，如果都只有一个元素,就直接比较大小

4. 如果有多个元素，先比较第一个元素，哪个列表第一个元素大，则该列表大，相等比较后面的，以此类推。

#### 3.2.3 列表常用函数或方法

> 3.5 列表处理(使用内置函数)

```
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

运行结果:
[1, 2, 3, 4, 5, 6]
['a', 'b', 'c', 'd', 'e']
6
6
a
<list_reverseiterator object at 0x0000022308A467C0>
6
5
4
3
2
1
[1, 2, 3, 4, 5, 6]
[2, 1, 5, 4, 6, 3]
[1, 2, 3, 4, 5, 6]
21
1 a
2 b
3 c
4 d
5 e
```

> 例 3.6 列表处理(使用方法)

```
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

运行结果:
['b', 3, 'd', 2, 'c', 1, 'a', 5, 4, 'e']
['e', 4, 5, 'a', 1, 'c', 2, 'd', 3, 'b']
['e', 4, 5, 'a', 1, 'c', 2, 'd', 3, 'b', 'f']
['e', 4, 5, 'a', 1, 'c', 2, 'd', 3, 'b', 'f', 0, 6, 'g']
[0, 'e', 4, 5, 'a', 1, 'c', 2, 'd', 3, 'b', 'f', 0, 6, 'g']
2
0
3
```

知识点:

1. 处理列表的内置函数和方法

   1. 内置函数
      1. str()将列表转成字符串
      2. len()计算列表中元素个数
      3. min()找列表中最小值
      4. reversed()将列表中数据逆序排列
   2. 常用方法
      |方法名|功能描述|
      |-----|--------|
      |append()|在列表添加一个元素|
      |extend()|将序列 seq 内容添加到列表中|
      |insert|在索引位置插入元素|
      |pop()|删除并返回指定位置元素,默认为-1|
      |count()|返回指定元素出现的次数|
      |index()|返回指定区间内指定对象的索引值|
      |sort()|对列表进行排序|
      |reverse()|将列表反序|

2. 内置函数 sorted()和列表方法 sort()区别

   sort()方法直接在原列表上操作，sorted()不改变原来的列表

   不同类型的数据不能混合来排序

> 3.7 将若干同学的某门课程的成绩存入到一个列表中，实现成绩列表的添加，删除，排序，输出前五名成绩的相关操作

```
score_python = [65, 88, 79, 95, 100, 58, 81, 58, 90, 77]
score_python.append(33)
print(score_python)
print(score_python.index(100))
score_python.insert(4, 99)
print(score_python)
score_python.remove(99)
score_python.pop()
print(score_python)
score_python.sort(key=None, reverse=True)
print(score_python)
print(score_python[0:5])

结果:
[65, 88, 79, 95, 100, 58, 81, 58, 90, 77, 33]
4
[65, 88, 79, 95, 99, 100, 58, 81, 58, 90, 77, 33]
[65, 88, 79, 95, 100, 58, 81, 58, 90, 77]
[100, 95, 90, 88, 81, 79, 77, 65, 58, 58]
[100, 95, 90, 88, 81]
```

> 构建一个学生成绩的信息列表，要求表中的每个元素又是一个包含学生基本信息(学号、姓名、成绩)的列表数据，程序能够实现学生信息的添加，删除，统计，排序等操作。

```
score = [[1901, '张三', 80], [1902, '李四', 69], [
    1903, '王二', 70], [1904, '赵六', 68], [1905, '孙七', 58]]
for item in score:
    print(item)
print("******><><******")
while(1):
    print("1.增加一条学生成绩")
    print("2.按照学号删除成绩")
    print("3.全部学生成绩平均值")
    print("4.输出成绩的前三名")
    print("0.Exit")
    choice = int(input("请输入你的选择:").strip(" "))
    if choice == 0:
        break
    elif choice == 1:
        new_score = input("按学号、姓名和成绩的顺序输入一条信息(逗号隔开):\n").strip(" ")
        new_score = new_score.strip(" ").split(",")
        new_score[0] = int(new_score[0])
        new_score[2] = int(new_score[2])
        score.append(new_score)
    elif choice == 2:
        num = int(input("请输入要删除的学号:").strip(" "))
        for item in score:
            if item[0] == num:
                score.remove(item)
                break
    elif choice == 3:
        sum = 0
        for item in score:
            sum += item[2]
        average = sum/len(score)
        print(average)
    elif choice == 4:
        score.sort(key=lambda x: x[2], reverse=True)
        print(score[0:3])
    else:
        print("编号输入错误!")
```

知识点:

1. 字符串处理:字符串常用操作包括:替换、删除、截取、赋值、连接、比较、查找、分割等。
   1. strip()方法可以移除字符串头尾指定的字符或字符串，返回删除后得到的新序列
   2. slip()方法是对字符串进行分隔
2. 转义字符
   1. 输出特殊字符
   2. 表示一些特殊的控制字符，如\r(回车),\n(换行符),\t(制表符)
   3. 如 s='It's me',会报错应该写成 s='It\'s me'
   4. 如果在字符串中要使用'\'时就要写成'\\'
3. lambda 表达式

   常用形式:lambda 形参 1,形参 2...........:表达式

   ```
   如 add=lambda a,b:a+b
   print(add(6,8))
   结果:14
   ```

4. 升序和降序
   1. 不指定参数默认是升序排列
   2. 带参数:sort(key=None,reverse=True)
      1. key 是可以指定对哪些元素进行排序
      2. reverse 指定排序规则,True 降序,False 升序

#### 巩固与拓展:

1. 编写程序，从 0-9 十个数字当中随机抽取 4 个数字，组成一个随机数密码

```
import random
list = []
for i in range(4):
    list.append(random.randint(0, 9))
print(list)
```

2. 编写程序，用冒泡排序算法对列表内的数字元素进行排序，排序完成后分别打印排序前后的列表内容

```
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

运行结果：
排序前:
[5, 2, 3, 9, 4, 1, 8, 2, 3, 4, 7]
排序后:
[1, 2, 2, 3, 3, 4, 4, 5, 7, 8, 9]
```

### 3.3 元组

元组是序列数据类型，和列表有很多相似的地方，但是又和列表有根本上的不同，元组属于不可变对象，而列表是可变的对象。

> 例 3.9 创建元组

```
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

运行结果:
('MUC', 'Python', 2020)
<class 'tuple'>
['abc', 'xyz', 123]
<class 'list'>
('abc', 'xyz', 123)
<class 'tuple'>
123
MUCabc
('MUC', 'Python', 2020, 'abc', 'xyz')
```

知识点:

1. 使用圆括号将一组 Python 对象括起来，各个对象之间用逗号分隔，就创建了一个元组也可以使用空的圆括号创建一个空元组；还可以使用 tuple 函数创建元组。
2. 若使用圆括号创建只有一个元素的元组时，要在元素后加上逗号，否则不能创建一个元组。
3. 元组与列表一样，可以使用下标进行索引访问，下标索引从 0 开始；也可以从最后个元素开始按照负数逆序进行索引访问；还可以进行切片操作。
4. 元组中的元素值不可以修改，但可以对元组进行连接操作，使得原先的元组指向新的元组组合；注意修改元组内的元素和元组的重新组合是两个概念。
5. del 语句操作可以删除元组，在上例中最后删除 tp2 组后，再次访问 tp2 则会出现错误提示。

> 例 3.10 对特定元组进行操作，理解元组的独特性

```
tp = ('MUC', 'Python', 2020, ['abc', 'xyz', 123])
print(tp)
tp[3][2] = 'end'
print(tp)
结果:
('MUC', 'Python', 2020, ['abc', 'xyz', 123])
('MUC', 'Python', 2020, ['abc', 'xyz', 'end'])
```

知识点:

1. 如果一个元组中的元素是可变对象，那么这个可变对象是可以修改的，仅限于可变对象的元素。
2. 对于一组用逗号隔开的数据，没有明确定义时，Python 默认该组数据是元组数据。
3. 元组和列表可以通过相应的函数转换
4. 元组的其他运算符操作与列表是一致的，元组的内置函数和方法操作则是和序列的方法和函数一致

### 3.4 字典

> 字典是映射数据类型，是键值对元素组成的无序集合，键是不可变对象且不能重复，而值是可以改变的。且可以重复出现。

#### 3.4.1 字典的基本操作

> 例 3.11 创建字典数据，并对字典数据进行简单的操作

```
dict1 = {}
print(dict1)
print(type(dict1))
dict2 = {'Jerry': 8, 'Tom': 5, 'Mary': 10}
print(dict2)
dict3 = {'name': 'Tom', 'Age': 22, 'Sex': 'male', 123: 'China USA US'}
print("dict2['Jerry']:", dict2['Jerry'])
dict2['Tom'] = 7
dict2['Mary'] = 12
print(dict2)
del dict3[123]
print(dict3)
dict3.clear()
print(dict3)

运行结果:
{}
<class 'dict'>
{'Jerry': 8, 'Tom': 5, 'Mary': 10}
dict2['Jerry']: 8
{'Jerry': 8, 'Tom': 7, 'Mary': 12}
{'name': 'Tom', 'Age': 22, 'Sex': 'male'}
{}
```

知识点:

1. 字典的键是不可变对象，在命名是可以使用数字，字符串或者是元组，但是不能是可变对象如列表。
2. 访问是用键来作为索引的，删除单个使用 del，清空字典使用 clear()方法，

#### 3.4.2 字典的内置函数和方法

> 例 3.12 使用字典的内置函数和方法对字典数据进行操作

```
dict2 = {'Jerry': 8, 'Tom': 10, 'Lily': 9}
print(len(dict2))
print(type(dict2))
print(str(dict2))
print(dict2.items())
print(dict2.keys())
print(dict2.values())
print(dict2.get('Lily', 20))
print(dict2.get('Luck', 18))
print(dict2.pop('Lily', 20))
print(dict2.popitem())
print(dict2)
dict3 = dict2.fromkeys('ABCDEF', 9)
print(dict3)
print(dict2)
dict3.update(dict2)
print(dict3)
dict2.setdefault('Jerry', 16)
print(dict2)
dict2.setdefault('Lily', 10)
print(dict2)

运行结果:
3
<class 'dict'>
{'Jerry': 8, 'Tom': 10, 'Lily': 9}
dict_items([('Jerry', 8), ('Tom', 10), ('Lily', 9)])
dict_keys(['Jerry', 'Tom', 'Lily'])
dict_values([8, 10, 9])
9
18
9
('Tom', 10)
{'Jerry': 8}
{'A': 9, 'B': 9, 'C': 9, 'D': 9, 'E': 9, 'F': 9}
{'Jerry': 8}
{'A': 9, 'B': 9, 'C': 9, 'D': 9, 'E': 9, 'F': 9, 'Jerry': 8}
{'Jerry': 8}
{'Jerry': 8, 'Lily': 10}
```

> 例 3.13 二维列表中存放有若干名学生的基本信息，每个学生的信息包括:姓名、性别和年龄，将男生和女生的人数存入字典并保存。

```
StuInfo = [["王硕", "男", 18], ["李梅", "女", 21], ["赵翔", "男", 20], ["王楠", "女", 19], [
    "张力", "男", 20], ["陈昊", "男", 18], ["丁宁", "女", 19], ["王飞", "男", 20]]
StuDict = {}
for item in StuInfo:
    sex = item[1]
    StuDict[sex] = StuDict.get(sex, 0)+1
print("统计结果为:")
for key, value in StuDict.items():
    print(key, value, "人")

运行结果:
统计结果为:
男 5 人
女 3 人
```

知识点:

1. get()方法:

   > 字典名.get(键[,默认值])

2. 字典常用方法
   |方法|功能描述|
   |----|-------|
   |clear()|清空字典|
   |copy()|返回字典的浅复制副本|
   |items()|返回字典键值对元组组成的列表|
   |keys()|返回字典键组成的列表|
   |values()|返回字典值组成的列表|
   |get()|返回字典某个键所对应的值|
   |pop()|删除并返回指定键对应的字典元素|
   |popitem()|随机删除并返回一个字典元素组成的元组|
   |fromkeys()|使用指定序列和值创建一个字典|
   |update()|更新字典的键值对|
   |setdefault()|返回键对应的默认值,缺少默认值时用参数值更新字典|

巩固与拓展

1. 使用字典来管理一个系统所有的账户密码

```
dict = {"username": "xiaoqiyan", "password": 123456}
username = input("请输入用户名:")
password = int(input("请输入密码:"))
if username == dict["username"]:
    if password == dict["password"]:
        print("用户名，密码正确!")

运行结果:
请输入用户名:xiaoqiyan
请输入密码:123456
用户名，密码正确!
```

### 3.5 应用实例

> 设计一个通讯录管理系统，包括信息的添加、删除和查找等功能。通讯录中每个人的信息如表 3-4 所示。程序运行后，会在屏幕上显示功能列表，按编号选择相应的功能，执行完一项功能后，会继续显示功能列表，可以选择相应的功能继续执行，直到输入编号 0，结束整个程序。功能列表如下所示:

0. 退出
1. 添加信息
2. 删除信息
3. 查找信息
4. 统计人数
5. 显示信息

| 姓名 | 电话 | 工作地点    |
| ---- | ---- | ----------- |
| 张三 | 北京 | 13812345678 |
| 李四 | 上海 | 18512345678 |
| 王五 | 广州 | 13912345678 |

```
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

```

### 第 4 章 函数

使用函数的目的:

1. 分解问题，降低编程难度
2. 代码的重复利用

#### 4.1 函数的定义和调用

> 例 4.1 编写一个函数，实现机器人自动问好的功能

```
def hello():
    print("Hello!")
    print("I am Robot A. ")
    print("Nice to meet you!")


hello()
```

> 例 4.2 编写一个函数，实现机器人自动问候的功能，并能够指出问候的对象

```
def hello(name):
    print("Hello!{}!".format(name))
    print("I am Robot A. ")
    print("Nice to meet you!")


hello("Jack")
```

知识点:

1. 函数的定义格式

   > def <函数名>(<参数列表>):
   > <函数名>
   > return <返回值列表>

2. 函数的调用

   > <函数名>(<参数列表>)

3. 形参和实参
   定义函数时参数列表里的是形式参数

调用时是实际参数

#### 4.2 函数的参数传递

> 例 4.3 编写一个函数进行数学运算，要求有三个形参且形参中有默认值

```
def jisuan(x, y, z=8):
    print(x*y)
    print(x+y+z)
    print(6*'*')


jisuan(3, 2)

jisuan(1, 2, 3)

运行结果:
6
13
******
2
6
******
```

> 例 4.4 编写一个带默认值的函数，在函数中运算后将结果用 return 语句返回

```
def jisuan(x, y, z=2):
    return (x+y+z)


s = jisuan(3, 4)
print(s)
print(jisuan(3, 8, 3))

运行结果:
9
14
```

#### 4.3 变量的作用域

> 例 4.5 分析下面程序中同名变量的不同作用

```
number = 0


def add(num1, num2):
    number = num1+num2
    print("函数内变量number: ", number)
    return number


add(1, 2)
print("函数外变量number: ", number)
```

> 例 4.6 编写程序，使得函数内部可以操作全局变量

```
number = 0


def add(num1, num2):
    global number
    number = num1+num2
    print("函数内变量number: ", number)
    return number


add(1, 2)
print("函数外变量number: ", number)
```

知识点:

1. 局部变量:函数内部定义的变量，只能在声明的函数内部访问
2. 全局变量:在函数外部定义的变量，在程序全过程都有效，如果要在函数内部使用要先使用保留字 global 声明

#### 4.4 函数模块化编程

> 例 4.7 将第 3 章中的例 3.8 改写，将每一种类型的操作改写成一个可被调用的函数

```
def add_student():
    new_score = input("按学号、姓名和成绩的顺序输入一条信息(逗号隔开):\n").strip(" ")
    new_score = new_score.strip(" ").split(",")
    new_score[0] = int(new_score[0])
    new_score[2] = int(new_score[2])
    return score.append(new_score)


def del_student():
    num = int(input("请输入要删除的学号:").strip(" "))
    count = len(score)
    for item in score:
        count = count-1
        if item[0] == num:
            score.remove(item)
            print("删除成功!")
            break


def average():
    sum = 0
    for item in score:
        sum += item[2]
    if sum == 0:
        print("学生数据为空!")
    else:
        average = sum/len(score)
        print(average)


def top3(line):
    line = sorted(line, key=(lambda item: item[2]), reverse=True)
    print(line[0:3])


score = [[1901, '张三', 80], [1902, '李四', 69], [
    1903, '王二', 70], [1904, '赵六', 68], [1905, '孙七', 58]]

for item in score:
    print(item)
print("******><><******")
while(1):
    print("1.增加一条学生成绩")
    print("2.按照学号删除成绩")
    print("3.全部学生成绩平均值")
    print("4.输出成绩的前三名")
    print("0.Exit")
    try:
        choice = int(input("请输入你的选择:").strip(" "))
        if choice == 0:
            break
        elif choice == 1:
            add_student()
        elif choice == 2:
            del_student()
        elif choice == 3:
            average()
        elif choice == 4:
            top3(score)
        else:
            print("输入编号错误!")
    except:
        print("请输入数字!")

```

知识点:

1. 函数的定义与调用
2. 异常处理:Python 中的错误有语法错误，逻辑错误，运行错误三种。

| 异常名            | 异常含义                       |
| ----------------- | ------------------------------ |
| Exception         | 常规异常基类，可以捕获任意异常 |
| NameError         | 未声明或未初始化的变量被引用   |
| SytaxError        | 语法错误                       |
| ZeroDivisionError | 除数为 0                       |
| IndexError        | 索引超出范围                   |
| FileNotFoundError | 要打开的文件不存在             |
| AttributeError    | 对象的属性不存在               |

1. try....except
2. try....except...else
3. try....except...finally

#### 4.5 应用实例

> 将 3.5 应用实例中的添加信息，删除信息，查询信息，统计人数和显示信息 5 个功能分别用 5 个函数实现

```
import sys
flag = 1
data_end = []


def insert(data):
    person = []
    info = input("请输入姓名，电话，工作地点(中文逗号分隔)")
    person = info.strip(" ").split("，")
    data.append(person)
    return data


def delete(data):
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
    return data


def search(data):
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


def count(data):
    if(len(data) > 0):
        p_dict = {}
        for line in data:
            p_dict[line[2]] = p_dict.get(line[2], 0)+1
        print("统计结果为:")
        for key, value in p_dict.items():
            print(key, value, "人")
    else:
        print("通讯录为空!")


def show(data):
    if len(data) > 0:
        for line in data:
            for item in line:
                print(item, end=' ')
            print("\n")
    else:
        print("通讯录为空!")


while(1):
    print("***************")
    print("   1、添加信息")
    print("   2、删除信息")
    print("   3、查找信息")
    print("   4、统计人数")
    print("   5、显示信息")
    print("   0、退出")
    print("***************")
    try:
        ch = int(input("请输入功能编号:"))
        if ch == 0:
            sys.exit(0)
        elif ch == 1:
            data_end = insert(data_end)
        elif ch == 2:
            data_end = delete(data_end)
        elif ch == 3:
            search(data_end)
        elif ch == 4:
            count(data_end)
        elif ch == 5:
            show(data_end)
        else:
            print("功能编号错误!")
    except:
        print("输入的不是数字!")

```

### 第 5 章 文件

#### 5.1 文件的打开和关闭操作

> 打开一个当前目录下的文件，进行简单的操作后，关闭这个文件

```
paper = open('first', 'x')
paper.write("Welcome to Python File World!")
paper.close()
paper2 = open('first', 'r')
hello = paper2.readline()
print(hello)
```

知识点:

1. open()函数打开模式
   |打开模式|功能含义|
   |--|--|
   |'r'| 只读模式(默认) |
   |'w'| 只写模式，如果文件存在则覆盖原文件，不存在则新建 |
   |'x'| 创建新文件，以只写方式打开 |
   |'a'| 追加写方式打开文件，文件不存在则创建，存在则在文件最后追加写入 |
   |'b'| 二进制文件模式 |
   |'t'| 文本模式(默认) |
   |'+'| 用于模式叠加操作，在原有模式上同时增加读写模式 |
2. 打开文件后记得关闭文件

#### 5.2 文件的读写操作

文本文件的读写是按照字符串方式进行，二进制文件的读写是按照字节流进行

> 例 5.2 新建一个文件，并向文件内写入几行数据，写完后重新定位读写指针位置到文件的开头，输出全部文件的内容

```
paper = open('first', 'w+')
print(paper.read())

paper.write('Welcome to Python File World!\r\n')
paper.write('Python is very powerful!\r\n')

paper.write('Python is also interesting!\r\n')
print(paper.read())
paper.seek(0)
print(paper.read())
paper.close()

```

知识点:

1. 文件的读写方法
   |方法函数|功能含义|
   |---|---|
   |read()|返回字符或字符串，可设定参数指定返回数量，不指定或指定为负数全部返回|
   |readline()|读取一行数据，指定参数时返回参数指定字节数的字符|
   |readlines()|以行为单位读取多行数据，指定参数时表示返回的行数|
   |write()|将指定的数据写入文件，参数就是要写入的数据，返回写入的字节数大小|
   |writelines()|写入一个字符串的列表到文件中，不返回结果|
   |seek()|设定读写指针的指向位置，0 为开头，1 为当前位置，2 为文件末尾|
   |tell()|返回读写指针的指向位置|

#### 5.3 文本文件操作

> 例 5.3 读取一个记录了用户信息(账号和密码)的文本文件，用户信息包括账号名和密码两部分，文本中每行记录一条用户信息，账号和密码之间用空格隔开，查找文件是否存在一个账户名为 hello 的账号，如存在将其密码修改为 123456；若不存在，则在文件尾部追加一个 hello 账户信息，并设定密码为 123456.

```

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

```

#### 5.4 CSV 文件的读写

> 例 5.4 有一个存放学生信息的文件 student.csv，存有五名学生的学号、姓名、成绩信息，读取并显示文件内容，计算学生成绩的平均值，根据学生的成绩进行排序，并将排序后的结果写入新文件 student123.csv 中

```
student_xy = []
print("原文件的内容是:")
with open('student.csv', 'r', encoding='gb18030') as data:
    for line in data:
        print(line.strip())
        line = line.strip()
        student_xy.append(line.split('，'))
print("转换成列表后是: ")
print(student_xy)
print("课程的平均成绩是: ")
score = student_xy[1:]
sum = 0
for item in score:
    sum = sum+int(item[2])
average = sum/len(score)
print(average)
print("按照成绩排名是: ")
score = sorted(score, key=(lambda item: int(item[2])), reverse=True)
print(score)
with open('student123.csv', 'w', encoding='utf-8')as data:
    data.write('，'.join(student_xy[0])+'\n')
    for s in score:
        data.write('，'.join(s)+'\n')
print("排序后的新文件内容是: ")
with open('student123.csv', 'r', encoding='utf-8')as data:
    for line in data:
        print(line.strip())

```

知识点:

1. with 语句:使用 with 语句可以不用关闭
2. 文件目录方法
   |方法函数|功能含义|
   |---|---|
   |remove()|删除文件，参数为文件名或带路径的文件名|
   |rename()|文件重命名，参数为新文件名和旧文件名|
   |mkdir()|创建新目录，参数为目录名|
   |chdir()|切换其他目录为当前目录|
   |getcwd()|返回当前工作目录|
   |rmdir()|删除目录，参数为目录名|
   |listdir()|返回当前目录下的子目录和文件名|

#### 5.5 应用实例

> 问题描述:现有两个文件：一个是保存星座及其时间信息的文本文件，另一个是保存若干人姓名及其生日的“生日.csv”文件，现在要求将“生日.csv”文件中所有人的姓名、生日和星座写入文件“生日星座.csv”，同时将各个星座的人数统计出来，保存到文件“星座统计.txt”中。4 个文件的内容格式如图 5-1 所示。

```
import csv


def readtxt(filename):
    with open(filename, "r")as f:
        ls = []
        for line in f:
            s = line.strip("\n").split("，")
            ls.append(s)
        xing_all = []
        for row in ls:
            xing_one = []
            if len(row[2]) == 3:
                yue1 = row[2][0]
                ri1 = row[2][1:3]
            else:
                yue1 = row[2][0:2]
                ri1 = row[2][2:4]
            if len(row[3]) == 3:
                yue2 = row[3][0]
                ri2 = row[3][1:3]
            else:
                yue2 = row[3][0:2]
                ri2 = row[3][2:4]
            xing_one.append(row[1])
            xing_one.append(int(yue1))
            xing_one.append(int(ri1))
            xing_one.append(int(yue2))
            xing_one.append(int(ri2))
            xing_all.append(xing_one)
    return xing_all


def readcsv(filename, xing):
    with open(filename, "r") as f:
        f.readline()
        sr = f.readlines()
        people = []
        for item in sr:
            person = []
            per = item.strip("\n").split("\t")
            date = per[1].split("-")
            person.append(per[0])
            person.append(date[1]+"月"+date[2]+"日")
            for line in xing:
                if (int(date[1]) == line[1] and int(date[2]) >= line[2]) or (int(date[1]) == line[3] and int(date[2]) <= line[4]):
                    per.append(line[0])
                    break
            people.append(per)
    return people


def writecsv(filename, people):
    with open(filename, "w", newline="")as f:
        w = csv.writer(f)
        w.writerow(["姓名", "生日", "星座"])
        w.writerows(people)


def Stats(people):
    dict_num = {}
    for line in people:
        dict_num[line[2]] = dict_num.get(line[2], 0)+1
    return dict_num


def writetxt(filename):
    with open(filename, "w")as f:
        f.write("星座    人数"+"\n")
        f.write("-------------"+"\n")
        for key, value in dict_num.items():
            f.write(key+"  "+str(value)+"\n")


if __name__ == '__main__':
    list_xing = readtxt("星座.txt")
    list_people = readcsv("生日.csv", list_xing)
    writecsv("生日星座.csv", list_people)
    dict_num = Stats(list_people)
    writetxt("星座统计.txt")

```

### 第 6 章 面向对象编程

#### 6.1 类和对象的概念

##### 6.1.1 类和对象

> 例 6.1 定义一个 Person 类，能说出姓名和职业，比如：“大家好，我叫张三，职业是教师”

```
class Person:
    def say(self, name, occupation):
        print("大家好,我叫"+name)
        print("职业是"+occupation)


teacher = Person()
doctor = Person()
teacher.say("张三", "教师")
doctor.say("李四", "医生")
```

知识点:

1. 类和对象的概念:对象指具体的事物，类是指事物的属性
2. 类和对象的关系:具有共性的若干事物可以抽象成一个类，一个类可以实例化出若干对象

##### 6.1.2 对象属性和方法

> 例 6.2 定义一个类 Person，该类包含三个对象属性:姓名，性别，年龄和职业；三个对象方法，一个方法的功能是输出姓名和年龄，另外两个方法的功能分别是判断给定职业或年龄是否与已有相同

```
class Person(object):
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say(self):
        print("大家好，我叫"+self.name+"，今年"+str(self.age) + ",职业是:"+self.occupation)

    def judge_occupation(self, work):
        if self.occupation == work.strip(" "):
            print("职业相同")
        else:
            print("职业不同")

    def judge_age(self, age):
        if self.age == age:
            print("年龄相同")
        else:
            print("年龄不同")


Person1 = Person("张三", 20, "教师")
Person2 = Person("李四", 30, "医生")
Person1.say()
Person2.say()
Person1.judge_occupation("律师")
Person2.judge_occupation("医生")
Person2.judge_age(21)

```

知识点:

1. 什么是对象属性

   类的定义包括两个方面，数据成员和成员函数，数据成员用于描述对象的共性特征，也叫对象属性

2. 什么是对象方法

   对象方法也叫成员函数，用来描述对象的行为，用函数方式实现

3. 对象属性的定义

   对象属性是指定义在构造方法**init**()里面的属性，对象属性由两部分组成，前面是“self.”，后面是任意合法标识符，其中 self 表示对象本身。

4. 对象方法的定义

   对象方法定义形式如下

   > def 方法名(self,[参数 1，参数 2,.....]):
   > 代码块

5. 对象方法的调用

   > 对象名.方法名([参数列表])

##### 6.1.3 构造方法和非构造方法

> 例 6.3 系统登录时，需要验证用户名和密码的合法性，如果户名和密码正确，则输出“登录成功！”，结束程序。否则，输出“用户名或密码错误！”，重新输人，直到输入正确，结束程序。所有用户名和密码信息保存在“账号密码.txt”中，该文件中的每行对应一个人的账号和密码（逗号分隔），假设用户名和密码都是长度在 3 ～ 16 之间的字符串。定义登录验证的 Login 类，并通过实例化对象验证类的正确性。

```
class Login(object):
    def __init__(self):
        self.userlist = self.setvalue()

    def setvalue(self):
        userlist = []
        with open('账号密码.txt', "r", encoding="utf-8")as f:
            for line in f.readlines():
                info = line[:-1].split(",")
                userlist.append(info)
        return userlist

    def Check(self, name, password):
        flag = 0
        if self.isLegalUser(name, password):
            for line in self.userlist:
                if line[0] == name and line[1] == password:
                    print("登录成功")
                    flag = 1
                    return flag
            if flag == 0:
                print("用户名或密码错误")
        else:
            print("账号或密码长度非法!")

    def isLegalUser(self, name, password):
        if len(name) >= 3 and len(name) < 16:
            if len(password) >= 3 and len(password) <= 16:
                return True
        return False


if __name__ == "__main__":
    login = Login()
    while(True):
        str_name = input("请输入用户名:")
        str_pwd = input("请输入密码:")
        if login.Check(str_name, str_pwd):
            break

```

知识点:

1. 构造方法

类中的两个特殊方法:一个是构造方法**init**():，一个是析构方法**def**()。一般会自动调用

2. 构造方法的定义

   > def **init**(self,[参数 1，参数 2]):
   > 代码块
   > 第一个参数是对象本身

3. 对象方法的调用

   1. 构造方法可以调用除本身之外任何方法
   2. 其他对象方法之间可以互相调用
   3. 其他对象方法不可以调用构造方法
   4. 调用对象方法形式:
      > self.方法名([参数 1，参数 2，.....])
      > 参数位置没有 self

4. if **name** == "**main**":
   程序文件的两种使用方法:
   1. 作为脚本直接执行
   2. 作为模块导入其他文件执行
      > if **name** == "**main**":后面的代码只在第一种情况下才执行

##### 6.1.4 类的属性和方法

> 例 6.4 创建一个学生选课的类，对象属性是姓名和成绩，类属性是课程名称和学分。除构造方法外，有 3 个对象方法，其功能分别是显示课程信息，修改课程学分和修改课程名称。

```
class CourseSelect(object):
    credit = 3
    cname = "计算机"

    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 显示课程信息

    def CourseInfo(self):
        print("课程名:"+CourseSelect.cname)
        print("学分为:"+str(CourseSelect.credit))
    # 修改课程学分

    def set_credit(self, n):
        CourseSelect.credit = n
    # 修改课程名称

    @classmethod
    def set_name(cls, c):
        cls.cname = c


if __name__ == "__main__":
    stu1 = CourseSelect("张三", 90)
    stu2 = CourseSelect("李四", 100)
    stu1.CourseInfo()
    stu2.CourseInfo()
    stu2.set_credit(5)
    stu1.CourseInfo()
    stu2.CourseInfo()
    CourseSelect.set_name("英语")
    stu1.CourseInfo()
    stu2.CourseInfo()
```

知识点:

1. 类属性的定义
   类属性是在所有对象方法(包括构造方法)外定义
2. 类属性的访问
   类属性对于整个类都是课件的，在类内部和外部都可以调用
3. 类方法的定义
   类中定义的方法有 3 种:对象方法，类方法和静态方法
   1. 类方法
      > @classmethod
      > def 方法名(cls,[可选参数列表])
      > 代码块
      > 第一个参数代表类
4. 类方法的调用

类方法不需要实例化，直接调用

> 类名.类方法(参数列表)

注意：
对象方法只能由实例化的对象调用，类方法两种都可以调用

巩固与拓展:

> （1）定义一个学生类，包含 2 个对象属性：姓名和学号；1 个对象方法：output()输出学生的姓名和学号。创建 2 个学生对象，验证类的正确性。

```
class Student():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def output(self):
        print("姓名:"+self.name)
        print("学号:"+str(self.number))


Student1 = Student("张三", 1)
Student2 = Student("李四", 2)
Student1.output()
Student2.output()
```

> （2）定义一个圆类，包含 1 个对象属性：半径；2 个对象方法：area()计算圆的面积，circum()计算圆的周长。创建两个不同半径的对象，测试类的正确性。

```
import math


class circular(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("圆的面积是:%.2f" % (math.pi*pow(self.radius, 2)))

    def circum(self):
        print("圆的周长是:%.2f" % (2*math.pi*self.radius))


radius1 = circular(5)
radius1.area()
radius1.circum()

```

> （3）定义 Compute 类，包含 2 个对象属性：两个整数；4 个对象方法：Add()、Sub()、Mult()和 Div() 分别实现加、减、乘、除运算。创建一个对象，验证类的正确性。

```
class compute(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        print("a+b=%d" % (self.num1+self.num2))

    def Sub(self):
        print("a-b=%d" % (self.num1-self.num2))

    def Mult(self):
        print("a*b=%d" % (self.num1*self.num2))

    def Div(self):
        print("a/b=%.2f" % (self.num1/self.num2))


compute1 = compute(8, 4)
compute1.Add()
compute1.Sub()
compute1.Mult()
compute1.Div()
```

> （4）设计一个系统管理员类，包含 2 个类属性：Acount 和 password，初始值分别设为“admin＇和“2020”。2 个类方法：Change() 修改管理员的账号和密码，Prnt()输出管理员账号和密码。分别使用对象调用和类名直接调用验证类方法的正确性。

```
class manager(object):
    Acount = "admin"
    password = "2020"

    def __init__(self, Acount, password):
        self.Acount = Acount
        self.password = password

    @classmethod
    def Change(cls, a, p):
        cls.Acount = a
        cls.password = p

    def pnf(self):
        print("账号:"+manager.Acount + " 密码:"+str(manager.password))


manager1 = manager("admin", "2020")
manager1.pnf()
manager.Change("xiaoqiyan", "2001")
manager1.pnf()

```
