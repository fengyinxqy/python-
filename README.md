# <!-- TOC -->

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
