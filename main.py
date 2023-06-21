""""""
"""
7-1 sdut-温度转换

f = float(input())
c = 5 * (f - 32) / 9
print("%.2f" %(c))

7-2 sdut-oop-1 简单的复数运算

x, y = map(int, input().split())
a = complex(x, y)
while True:
    q, w, e = map(int, input().split())
    if q == 0 and w == 0 and e == 0:
        break
    else:
        b = complex(q, w)
    if e == 1:
        a = a + b
    elif e == 2:
        a = a - b
    elif e == 3:
        a = a * b
print(int(a.real), int(a.imag))

7-3 sdut-入门-转换字母

a = input()
print(a.upper())

7-4 sdut-计算球体积

while 1:
    try :
        n = input()
        n = float(n)
        PI = 3.1415926
        m = 4.0/3 * PI * n * n * n
        print("%.3f" %m)
    except :
        break;   

sdut-数据类型-1-求班级男女生比例

n, m = input().split(" ")
n = float(n)
m = float(m)
n1 = float(n / (n+m)*100)
m1 = float(m / (n+m)*100)
print("%.2f%% %.2f%%" %(n1, m1))


7-6 sdut-常用类-骄傲的代价

while 1:
    try:
        n = int(input())
        while n:
            n -= 1
            a, b = map(int, input().split())
            print("%d+%d=%d" %(a, b, a + b))
            print("%d-%d=%d" %(a, b, a - b))
            print("%d*%d=%d" %(a, b, a * b))
            print("%d/%d=%d" %(a, b, a // b))
            print("%d%%%d=%d" %(a, b, a % b))
    except:
        break;
        
7-7 sdut-求奇数分之一序列的前N项近似和

import math
a=int(input())
sum,x=0,-1
for i in range(1,a+1):
    x=x+2
    sum=sum+1/x
print("sum≈%d" %(math.ceil(sum)))

7-8 sdut-求平方与倒数序列的近似和

import math
n, m = map(int, input().split())
sum = 0.0
for i in range(n, m + 1):
    sum = sum + i*i + (1.0/i)
 
print("sum≈%d" %(math.floor(sum)))    #输出：12


7-9 sdut-入门-三个整数和、积与平均值
import math
a, b, c = map(int, input().split())
x = a + b + c
y = a * b * c
z = x/3.0
print("%d %d %.2f"  %(x, y, z))


7-10 sdut-入门-买糖果
import math
n = int(input())
n *= 10
x = math.floor(n/3)
y = n%3
print(x, y)

7-1 sdut-sel-10 直角坐标系象限判断
while 1:
   try:
        x, y = map(int,input().split())
        if x > 0 and y > 0:
            print(1)
        elif x < 0 and y > 0 :
            print(2)
        elif x < 0 and y < 0:
            print(3)
        elif x >0 and y < 0 :
            print(4)
   except:
       break;


7-2 sdut-sel-2 汽车超速罚款（选择结构）

x, y = map(int, input().split())
c = y - x
if c <= 0:
    print("Congratulations, you are within the speed limit!")
elif c > 0:
    if 1 <= c <= 20:
        print("You are speeding and your fine is 100.")
    elif 21 <= c <= 30:
        print("You are speeding and your fine is 270.")
    else:
        print("You are speeding and your fine is 500.")


7-3 sdut-运输计费问题
ball=0
t,s=map(float,input().split( ))
if s<250:
    ball = s*t
elif 250<=s<500:
    ball = s*t*0.98
elif 500<=s<1000:
    ball = s*t*0.95
elif 1000<=s<2000:
    ball = s*t*0.92
elif 2000<=s<3000:
    ball = s*t*0.9
elif s>=3000:
    ball = s*t*0.85

print("%.0lf"%ball)


7-4 sdut-阶梯电价

s, t = map(float, input().split())
if 0 < s <= 50:
    print('cost=%.2f' % (s*0.53))
elif s > 50:
    print('cost=%.2f' % (50*0.53+(s-50)*(0.53+t)))
elif s <= 0:
    print("cost=0.00")
    
7-5 sdut-分段计算居民水费
x = float(input())
if 0 <= x <= 15:
    print('%.2f' % (4*x/3))
elif x > 15:
    print('%.2f' % (2.5*x-17.5))
    
7-6 sdut-循环-乘法运算
x = int(input())
for i in range(1, x+1):
    print('%d*%d=%d' % (i, x, i*x))

7-7 sdut-求π的近似值
import math
k = float(input())
m = 0
i = 1
h = 1
while h > k:
    h = 1 / pow(i, 2)
    m = m + h
    i += 1
p = math.sqrt(m*6)
print('%.6f' % p)

7-8 sdut-求误差小于输入值的e的近似值

def jc(n):
    a = 1
    for i in range(n + 1):
        if i > 0:
            a *= i
    return a
error = float(input())
sum = 0
n = 0
while 1 / jc(n) > error:
    sum += 1 / jc(n)
    n += 1
sum += 1/jc(n)
print("%.6f" % sum)


7-9 sdut-入门-2 A+B for Input-Output Practice (II)
n = int(input())
for i in range(0,n):
    x, y = map(int,input().split())
    print(x+y)

7-10 sdut0-入门-3 A+B for Input-Output Practice (III)
while 1:
    try:
        x, y = map(int, input().split())
        if x != 0 and y != 0:
            print(x+y)
    except:
        break


7-11 sdut-入门-4 A+B for Input-Output Practice (IV)
while 1:
    try:
        s =input().split()
        n = int(s[0])
        if n != 0:
            sum = 0
            for i in range(1,n+1):
                x = int(s[i])
                sum += x
            print(sum)
    except:
        break


7-12 sdut-入门-5 A+B for Input-Output Practice (V)
n = int(input())
while n > 0:
    n -= 1
    lis = [int(num) for num in input().split()]
    if lis[0] == 0 :
        break
    sum = 0
    for i in lis:
        sum += int(i)
    sum -= lis[0]
    print(sum)

7-13 sdut-九九乘法表
while 1 :
    try :
        n = int(input())
        for i in range (1, n + 1) :
            for j in range(1, i) :
                print("%d*%d=%d" %(j, i, i*j), end = ' ')
            print("%d*%d=%d" %(i, i, i*i), end = '\n')
    except:
        break


7-14 sdut-平方数（I）
import math
def pingfang(n) :
    n = int(n)
    if math.floor(math.sqrt(n)) == math.ceil(math.sqrt(n)):
        return 1
    return 0
t = int(input())
while t > 0 :
    t -= 1
    n, m = map(int, input().split())
    n, m = min(n, m), max(n, m)
    sum = 0
    for i in range(n, m + 1) :
        if pingfang(i) == 1 :
            sum += i
    print(sum)

7-15 sdut-求交错序列前N项和
n = int(input())
m = 1.0
sum = 0.0
for i in range(1, n + 1) :
    if i & 1 :
        sum += float(i/m)
    else :
        sum -= float(i/m)
    m += 2.0
print("%.3f" %(sum) )

7-16 sdut-生成输入数的乘方表
a,n = input().split()
n = int(n)
a = float(a)
ans = 1
print(a,end = "")
print("**0=1.00")
for i in range (1, n+1):
    ans = ans*a
    print(a,end = "")
    print("**",end = "")
    print(i,end = "")
    print("=",end = "")
    print("{0:.2f}".format(ans))


7-17 sdut-水仙花数
n=int(input())
for i in range(pow(10,n-1),pow(10,n)):
    sum=0
    for x in str(i):
        sum=sum+pow(int(x),n)
    if sum==i:
        print(i)


7-18 sdut-最大公约数和最小公倍数
try:
    while True:
        a,b = map(int,input().split( ))
        mul = a * b
        c = 0
        while a % b != 0:
            c = a % b
            a = b
            b = c
        print(b,int(mul/b))
except EOFError:
    pass


7-19 sdut-求满足条件的斐波那契数
def fib(n):
    a = 1
    b = 1
    c = 1
    while n >= 3:
        c = a+b
        a = b
        b = c
        n-=1
    return c
n = int(input())
for i in range(100000):
    if fib(i)>=n:
        print(fib(i))
        break

7-20 sdut-冒泡排序中数据交换的次数
n = int(input())
tmp = 1
count = 0
for i in range(n):
    count = 0
    lis = [int(num) for num in input().split()]
    del lis[0]
    for k in range(len(lis)):
        for d in range(len(lis)-k-1):
            if lis[d] > lis[d+1]:
                tmp = lis[d]
                lis[d] = lis[d+1]
                lis[d+1] = tmp
                count += 1
    print(count)


7-1 sdut-字符串排序
ls = list(input().split())
ls.sort()
print(*ls,sep=' ')

7-2 sdut-字符之比较大小
ls = [chr(int(c)) for c in input().split()]
ls.sort()
print(*ls, sep='<')

7-3 sdut-判断回文字符串
ls =[c for c in input().upper() if c.isalpha()]
if ls == ls[::-1]:
    print("yes")
else:
    print("no")
    
7-4 sdut-删除字符
s = input().strip()
c = input().strip()
if c.isalpha():
    s = s.replace(c.upper(), '').replace(c.lower(), '')
else:
    s = s.replace(c, '')
print("result: %s" % s)


7-5 sdut-逆序的N位数
print(int(input()[::-1]))

7-6 sdut-输出字符串中最大字符及其索引位置
ls = list(input())
c = max(ls)
pos = len(ls) - 1 - ls[::-1].index(c)
print("%c   %d" % (c, pos))

7-7 sdut-计算多个字符串中最长的字符串长度
n, ls = int(input()), []
for i in range(n):
    ls.append(input().strip())
ls.sort(key=len, reverse=True)
print("length=%d" % len(ls[0]))

7-8 sdut-十进制数转换成二进制后1和0的个数 
num = int(input())
s = bin(num).lstrip('0')
print(s.count('1'), s.count('0'))


7-9 sdut-整数的二进制相加 
a = int(input())
b = int(input())
s1 = bin(a)[2::]
s2 = bin(b)[2::]
s3 = bin(a + b)[2::]
print("%08d" % int(s1))
print("%08d" % int(s2))
print('-' * 8)
print("%08d" % int(s3))

7-10 sdut-汉明距离
def hanming(x, y):
    return bin(x ^ y).count('1')
    
x, y = map(int, input().split())
print(hanming(x, y))

7-11 sdut-输出一个字符串的字符的16-10-8-2进制数
import re
s = input()
mach = re.findall('[0-9A-Fa-f]', s)
s = "".join(mach)
s = s.lower()
j10 = int(s, 16)
j8 = format(j10, 'o')
j2 = format(j10, 'b')
print("{} {} {} {}".format(s, j10, j8, j2))

7-12 sdut-显示数字出现次数
s = hex(int(input()))
c = input()
print(s.count(c))

7-1 sdut-ASCII码排序
try:
    while True:
        ls = list(input())
        ls.sort()
        print(*ls, sep=' ')
except EOFError:
    pass

7-2 sdut-数据逆序
try:
    while True:
        ls = list(input().split())
        ls.reverse()
        print(*ls, sep=' ')
except EOFError:
    pass
    
7-4 sdut-统计身高超过平均值的学生
ls = [float(n) for n in input().split()]
avg = float(sum(ls) / len(ls) * 1.0)
for each in ls:
    if each > avg:
        print(int(each), end=' ')

7-5 sdut-求整数的位数及各位数字之和
ls = list(map(int, input()))
print(len(ls), sum(ls))

7-6 sdut-字母替换
s1 = input()
s2 = ""
for i in s1:
    if i.isupper():
        s2 += chr(155 - ord(i))
    else:
        s2 += i
print(s2)

7-7 sdut-输出字母在字符串中位置索引
s = input()
c1, c2 = input().split()
for i in range(len(s) - 1, -1, -1):
    if s[i] == c1 or s[i] == c2:
        print(i, s[i])

7-8 sdut- 输出10个不重复的英文字母
s1 = input()
s2 = ""
for each in s1:
    if each.isalpha() and each.upper() not in s2 and each.lower() not in s2:
            s2 += each
if len(s2) < 10:
    print("not found")
else:
    print(s2[0:10])

7-9 sdut-判断两个字符串是否为变位词
from collections import *

def slv(s1, s2):
    if Counter(s1) == Counter(s2):
        print("yes")
    else:
        print("no")

sa = input()
sb = input()
slv(sa, sb)

7-10 sdut-猴子选大王
n,p = int(input()),0
for i in range(2, n + 1):
    p = (p + 3) % i
print(p + 1)

7-11 sdut-找出两组数据中非公共元素
ls1 = list(input().split())
ls2 = list(input().split())
ls3 = []
for it in ls1:
    if it in ls1 and it in ls2:
        pass
    else:
        ls3.append(it)
for it in ls2:
    if it in ls1 and it in ls2:
        pass
    else:
        ls3.append(it)
print(*ls3, sep=' ')

7-13 sdut-矩阵行、列、对角线和的最大值
num=list(map(int,input().split()))
l=[]
l.append(num[0]+num[4]+num[8])
l.append(num[2]+num[4]+num[6])
for i in range(0,6,3):
    l.append(num[i]+num[i+1]+num[i+2])
for j in range(0,3):
    l.append(num[j]+num[j+3]+num[j+6])
print(max(l))

7-15 sdut-打印显示直角字母图形
s="ABCDEFGHIJ"
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(s[j],end='')
    print()


7-17 sdut-array2-5 打印“杨辉三角“ 品中国数学史 增民族自豪感（2）
from math import *

def c(n, r):
    if n == 0 or r == 0:
        return 1
    else:
        return int(factorial(n) / (factorial(r) * factorial(n - r)))

x = int(input())
all = []
l = []
for n in range(x):
    for r in range(n + 1):
        l.append(c(n, r))
    all.append(l[:])
    l.clear()
cnt = x*2-2
for n in range(x):
    print(' '*cnt, end='')
    for nn in range(n + 1):
        print("%-4d" % all[n][nn], end='')
    print()
    cnt -= 2

7-18 sdut-列表去重
ls1 = eval(input())
ls2 = sorted(set(ls1), key=ls1.index)
print(*ls2, sep=' ')

7-19 sdut-期末考试之排名次
n = int(input())
ls = []
for i in range(n):
    ls.append(sum(map(int, input().split())))
ls.sort(reverse=True)
for it in ls:
    print(it)


7-20 sdut- 矩阵转置(II)
n, m = map(int, input().split())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))
ls_re = list(zip(*ls))
for i in range(m):
    print(*ls_re[i], sep=' ')

7-23 sdut-对称矩阵的判定
while True:
    n = int(input())
    if n == 0:
        break
    else:
        ls, flag = [], 1
        for i in range(0, n):
            ls.append(list(input().split()))
        for i in range(n):
            for j in range(n):
                if ls[i][j] != ls[j][i]:
                    flag = 0
        if flag == 0:
            print("no")
        else:
            print("yes")


7-18 sdut-查验身份证
n = int(input())
quanzhong = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
jiaoyanma = ['1','0','X','9','8','7','6','5','4','3','2']
 
flag = 0
for i in range(n):
    jiaquanhe = 0
    id = input()
    if len(id) != 18:
        flag += 1
        print(id)
    else:
        f = 0
        for j in range(17):
            if id[j] in '0123456789':
                f = f + 1
        if f != 17:
            flag += 1
            print(id)
        else:
            for k in range(17):
                jiaquanhe += quanzhong[k] * int(id[k])
            if id[17] != jiaoyanma[jiaquanhe % 11]:
                flag += 1
                print(id)
if flag == 0:
    print('All passed')
    
7-19 sdut-统计两个字符串中相同的字符个数
st1 = set(input())
st2 = set(input())
print(len(st1 & st2))

7-20 sdut-分析每队活动投票情况
ls = list(map(int, input().split(',')))
s1, s2 = [], []
for i in range(1, 11):
    if i not in ls:
        if 1 <= i <= 5:
            s1.append(i)
        else:
            s2.append(i)
print(*s1, sep=' ')
print(*s2, sep=' ')


7-21 sdut-统计字符在字符串中出现的次数
s = input()
c = input()
print(s.count(c))


7-22 sdut-四则运算（用字典实现）
dic = {'+': 'x+y', '-': 'x-y', '*': 'x*y', '/': "x/y if y!=0  else 'divided by zero'"}
x = int(input())
opt = input()
y = int(input())
ans = eval(dic[opt])
if type(ans) is not str:
    print("%.2f" % ans)
else:
    print(ans)
    

7-23 sdut-统计工龄
n = int(input())
ls1 = list(map(int, input().split()))
dic = {}
for it in ls1:
    dic[it] = dic.get(it, 0) + 1
ls2 = sorted(dic.keys())
for i in ls2:
    print("%d:%d" % (i, dic[i]))


7-24 sdut-字典合并
a = dict(eval(input()))
b = dict(eval(input()))
for it in b.keys():
    a[it] = a.get(it, 0) + b[it]
ls1 = list(a.items())
ls1.sort(key=lambda x: ord(x[0]) if type(x[0]) == str else x[0])
ls2 = list(str(dict(ls1)).strip('{}').replace(' ', '').replace('"', "'").split(','))
for it in ls2:
    print(it)


7-25 sdut-集合相等问题
n = int(input())
st1 = set(map(int, input().split()))
st2 = set(map(int, input().split()))
if st1 == st2:
    print("YES")
else:
    print("NO")


7-26 sdut-植物与颜色
ls1 = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
ls2 = ['Rose', 'Poppies', 'Sunflower', 'Grass', 'Bluebells', 'Violets']
dic = dict(zip(ls1, ls2))
n=int(input())
for i in range(n):
    col=input()
    if col in ls1:
        print("%s are %s."%(dic[col],col))
    else:
        print("I don't know about the color %s."%col)


7-27 sdut-众数
while True:
    try:
        n=int(input())
        ls=list(map(int,input().split()))
        num=max(ls,key=ls.count)
        print(num,ls.count(num))
    except EOFError:
        break


6-1 sdut-使用函数求a+aa+aaa++⋯+aa.....aaa(n个a）之和。
def fn(a,n):
    s=0
    z=a
    for i in range(n):
        if i>0:
            z=z*10+a
        s=s+z
    return s
    
6-2 sdut-使用函数求区域内的素数之和
import math
def prime(p):
    flag=True
    if p<2:
        flag=0
    else:
        for j in range(2,int(math.sqrt(p)+1)):
            if p%j ==0:
                flag=False
                break
    return flag
 
def PrimeSum(m,n):
    s = []
    for i in range(m,n+1):
        if prime(i)==True:
            s.append(i)
    return sum(s)
    
    
6-3 sdut-使用函数统计数字字符在某数字中出现的个数
def CountDigit(number,digit):
    num =str(number)
    dig = str(digit)
    return num.count(dig)
    
6-4 sdut-使用函数输出Fibonacci数列的值与指定范围内Fibonacci数值的个数
def fib(n):
    f1 = 1
    f2 = 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
    return f1
    
def fibs(a, b):
    l = list()
    i = 0
    while True:
        if a <= fib(i) <= b:
            l.append(fib(i))
        if fib(i) > b:
            break
        i += 1
    return l

6-5 sdut-利用函数得到缩写词
def acronym(p):
    s=""
    p=p.title()
    a=p.split()
    for i in range(0,len(a)):
        s=s+a[i][0]
    return s

6-6 sdut-求嵌套列表的平均值
def Avg(lst):
    blst = []
    for i in range(len(lst)):
        fin = 0
        avg = 0
 
        for j in range(len(lst[i])):
            fin = fin + lst[i][j]
        avg = fin / len(lst[i])
        blst.append(avg)
    return blst
    
7-1 sdut-求全排列
from itertools import permutations
n=int(input())
for i in permutations(list(  range(1,n+1)  )):
    print("".join(map(str,i)))
 
 7-3 sdut-列表数字元素加权和(2)
ls=eval(input())  
def s(ls,level):   
    sum=0   
    for i in ls:   
        if type(i) == int:    
            sum+=i*level     
        else:                    
            sum+=s(i,level+1)    
    return sum   
sum=s(ls,1)   
print(sum)

7-4 sdut-列表或元组的数字元素求和（yeild)
a = eval(input())

def fn(base):
    if type(base) == int:
        return base
    else:
        return sum(fn(i) for i in base if type(i) != str)

print(fn(a))

7-6 sdut-学生互助组队
ls_w, ls_m, ls = [], [], []
n = int(input())
for i in range(n):
    id, name = input().split()
    if id == '0':
        ls_w.append(name)
    else:
        ls_m.insert(0, name)
    ls.append(name)
dic1, dic2 = dict(zip(ls_w, ls_m)), dict(zip(ls_m, ls_w))
for i in range(len(ls) // 2):
    if ls[i] in dic1.keys():
        print(ls[i], dic1[ls[i]])
    else:
        print(ls[i], dic2[ls[i]])

7-7 sdut-求指定层的元素个数
dic = {}
s = eval(input())
n = int(input())
def cycle(s, n):
    for it in s:
        dic[n] = dic.get(n, 0) + 1
        if isinstance(it, list):
            cycle(it, n + 1)

cycle(s, 1)
print(dic.get(n, 0))


7-6 sdut-oop-8 分数四则运算（类和对象）
from fractions import *

n = int(input())
for i in range(n):
    s = input()
    if '+' in s:
        f1, f2 = map(str, s.split('+'))
        f3 = Fraction(f1) + Fraction(f2)
    elif '-' in s:
        f1, f2 = map(str, s.split('-'))
        f3 = Fraction(f1) - Fraction(f2)
    elif '*' in s:
        f1, f2 = map(str, s.split('*'))
        f3 = Fraction(f1) * Fraction(f2)
    elif '\\' in s:
        f1, f2 = map(str, s.split('\\'))
        f3 = Fraction(f1) / Fraction(f2)
    print(f3)


7-7 sdut-分数加减法
from fractions import *
while True:
    try:
        s = input()
        if '+' in s:
            f1, f2 = map(str, s.split('+'))
            f3 = Fraction(f1) + Fraction(f2)
        elif '-' in s:
            f1, f2 = map(str, s.split('-'))
            f3 = Fraction(f1) - Fraction(f2)
        print(f3)
    except EOFError:
        break

7-1 sdut-oop-2 Shift Dot(类和对象）
class Point:
    x=0
    y=0
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def move(self,x1,y1):
       self.x+=x1
       self.y+=y1
    def toString(self):
        return "({},{})".format(self.x,self.y)    
while True:
    try:
        x,y,n=map(int,input().split())
        a=Point(x,y)
        for i in range(n):
            x1,y1=map(int,input().split())
            a.move(x1,y1)
        print(a.toString())
    except:
        break
        
7-3 sdut-谁是最强的女汉子
n = int(input())
x = 0
y = 0
anw = 0
m = 10000
c = 0
for i in range(0,n):
    a,b = input().split()
    x = int(a)
    y = int(b)
    if x < m:
        c = 1
        anw = y
        m = x
    elif x == m:
        c = c+1
        anw = anw + y
print('{} {}'.format(c,anw),end = '')
 
 
 7-4 sdut-oop-5 计算长方体和四棱锥的表面积和体积（类的继承）
import math as m
class Rect:
    l = 0.0
    h = 0.0
    z = 0.0
    def __init__(self, l, h, z):
        self.l = l
        self.h = h
        self.z = z

    def length(self):
        return (self.l + self.h) * 2

    def area(self):
        return self.l * self.h
# 立方体类Cubic
class Cubic(Rect):
    def __init__(self, l, h, z):
        super().__init__(l, h, z)

    def area(self):

        return (self.h * self.l + self.l * self.z + self.h * self.z) * 2

    def v(self):
        return self.h * self.l * self.z
# 四棱锥类Pyramid
class Pyramid(Rect):
    def __init__(self, l, h, z):
        super().__init__(l, h, z)

    def area(self):
        return m.sqrt(self.h*self.h+4*self.z*self.z)*self.l/2+self.h*self.l+m.sqrt(self.l*self.l+4*self.z*self.z)*self.h/2

    def v(self):
        return  self.h * self.l * self.z/3

while True:
    try:
        a, b, c = map(float, input().split())
        C = Cubic(a, b, c)
        P = Pyramid(a, b, c)
        if a<=0 or b<=0 or c<=0:
            print("0.00 0.00 0.00 0.00")
        else:

        # print(C.area, C.v, P.area, P.v)
            print("{:.2f} {:.2f} {:.2f} {:.2f}".format(C.area(), C.v(), P.area(), P.v()))
    except:
        break
        
7-5 sdut-oop-6 计算各种图形的周长（多态）
from abc import ABCMeta, abstractmethod
import math
from webbrowser import BaseBrowser

class Shape:
    __metaclass__=ABCMeta

    @abstractmethod
    def length(self):
        pass

class Triangle(Shape):
    def __init__(self ,a,b,c):
        if a<=0 or b<=0 or c<=0:
            a=0
            b=0
            c=0
        if a+b<=c or c+b<=a or c+a<=b:
            a=0
            b=0
            c=0
        self.a=a
        self.b=b
        self.c=c
    def length(self):
        return self.a+self.b+self.c

class Rectangle(Shape):
    def __init__(self ,a,b):
        if a<=0 or b<=0:
            a=0
            b=0
        self.a=a
        self.b=b
    def length(self):
        return 2.0*(self.a+self.b)

class Circle(Shape):
    def __init__(self ,r):
        if r<=0:
            r=0
        self.r=r
    def length(self):
        return (self.r)*2.0*3.14

while True:
    try:
        nums=[eval(x) for x in input().split()]
        n=len(nums)
        ans=0.0
        if n==1:
            ans=(Circle(nums[0]).length())
        elif n==2:
           ans=(Rectangle(nums[0],nums[1]).length())
        else: 
            ans=(Triangle(nums[0],nums[1],nums[2]).length())
        print("{:.2f}".format(ans))
    except:
        break

7-6 sdut-oop-9 计算长方形的周长和面积（类和对象）
class Rect:
    __length = 0
    __width = 0
 
    def __init__(self, l, w):
        self.__length = l
        self.__width = w
 
    @classmethod
    def initsec(self, l):
        return self(l, l)
 
    def leng(self):
        return self.__length
 
    def widt(self):
        return self.__width
 
    def e(self):
        return self.__width * self.__length
 
    def z(self):
        return 2 * (self.__width + self.__length)
 
 
while True:
    try:
        num = [int(x) for x in input().split()]
        if len(num) == 1:
            if num[0] <= 0:
                num[0] = 0
            t = Rect.initsec(num[0])
 
        else:
            if num[0] <= 0 or num[1] <= 0:
                num[0] = 0
                num[1] = 0
            t = Rect(num[0], num[1])
 
        print(t.leng(), t.widt(), t.z(), t.e())
    except:
        break

7-7 sdut-oop-7 答答租车系统（类的继承与多态 面向对象综合练习）
class Car:
    def __init__(self, n, p, t, m):
        self.n, self.p, self.t, self.m = n, p, t, m

car = dict()
car[1] = Car("A", 5, 0, 800)
car[2] = Car("B", 5, 0, 400)
car[3] = Car("C", 5, 0, 800)
car[4] = Car("D", 51, 0, 1300)
car[5] = Car("E", 55, 0, 1500)
car[6] = Car("F", 5, 0.45, 500)
car[7] = Car("G", 5, 2.0, 450)
car[8] = Car("H", 0, 3, 200)
car[9] = Car("I", 0, 25, 1500)
car[10] = Car("J", 0, 35, 2000)

opt = int(input())
if opt == 1:
    N = int(input())
    sum_p, sum_t, sum_m = 0, 0.0, 0
    for i in range(N):
        m, n = map(int, input().split())
        sum_p += car[m].p * n
        sum_t += car[m].t * n * 1.0
        sum_m += car[m].m * n
    print("%d %.2f %d" % (sum_p, sum_t, sum_m))
elif opt == 0:
    print("0 0.00 0")


7-1.有一个英文文件"example.txt".编写一个程序把大写字母变小写，小写字母变大写，其他字符不变. 结果写入文件"result.txt"。@
程序压缩后(zip)以文件形式上传！
score1 = open('example.txt','r')
back1 = open('result.txt','a')
s = ''
for i in score1.read():
    if i.isupper():
        s += i.lower()
    elif i.islower():
        s += i.upper()
    else:
        s += i
back1.write(s)
score1.close()
back1.close()

7-2.统计文本文件"letter.txt"中各类字符个数：分别统计字母( 大小写不区分)，数字及其他字符的个数。@
程序压缩后(zip)以文件形式上传！
count = [0, 0, 0]
with open('letter.txt', 'r') as f:
    s = f.readlines()
    for i in range(len(s)):
        s[i] = s[i].lower()
    for i in s:
        for j in range(len(i)):
            if i[j].isalpha():
                count[0] += 1
            elif i[j].isdigit():
                count[1] += 1
            else:
                count[2] += 1
print(count[0], count[1], count[2])

7-3. 马丁路德金的"I have a dream"节选存放在"freedom.txt"中：
编程实现词汇表，计算每一个单词出现的次数，大小写不区分，输出到"dic.txt" 文件保存。
程序压缩后(zip)以文件形式上传！
count = {}
with open('freedom.txt', 'r') as f:
    s = f.readlines()
    print(s)
    for i in range(len(s)):
        s[i] = s[i].lower()
        s[i] = s[i].replace('\n', '')
    for i in s:
        a = i.split()
        for j in range(len(a)):
            if a[j] in count:
                count[a[j]] += 1
            else:
                count[a[j]] = 1
with open('dic.txt', 'w')as f:
    for i in count:
        f.write(i + ":" + str(count[i]))
        f.write('\n')

7-4. 用水量文件"water.txt"的第一列为账号，下面是每个月的用水量（后一个数-前一个数），共十二个月。每立方米需付1.05元。编程计算每户一年的水费，结果保存在fee.txt文件中。程序和结果文件压缩后（zip格式）以文件形式上传！
score=open('water.txt', 'r')
back = open('fee.txt', 'a')
s =''

for i in score.readlines():
    i=i[:-1]
    i=i.split()
    pay=float('%.2f'%((int(i[-1])-int(i[1]))*1.05))
    #将水费保留前2位
    s +=i[0] + ' ' +'%.2f' % pay + '\n'
back.write(s)
score.close()
back.close()


9-1 求文件行数
下载题目附件，编辑src/目录下的test.py文件，实现读取统计data.txt文件的有效行数，
并将结果输出保存到result.txt文件。(20分) **
**说明： **
（1）有效行指至少包括一个字符行，空行不计为有效行
（2）程序文件名 test.py 不能修改
（3）本地编写测试完成后，将src文件夹打包为 src.zip文件后上传提交

c = 0
with open('data.txt','r',encoding = 'utf-8') as f:
    for x in f.readlines():
        if x != '\n':
            c = c+1

with open('result.txt','w') as g:
    g.write('有效行数为:{0}行'.format(str(c)))
g.close()



"""
