<!-- TOC -->

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

<!-- /TOC -->

# Python 学习笔记

2021/11/12 重新开始学习 Python 基础，最多用一个月的时间把基础学完。

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
