#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name = input()
#格式化字符串和C语音类似%s,%d,%f,%x
print(name,'%s a=%d,b=%.2f' %('中文测试',100,200.2133))

print('%是一个特殊的字符需要转义')

#格式化字符串根据占位符进行匹配的
print('Hello,{0}成绩提升了{1:.1f}'.format('小明',12.343))

s1 = 72
s2 = 85
r = (s2-s1);
print('提升的百分数%.1f' %r)

#python内置的list集合

#声明一个空的list
empty=[]
#定义一个list
element = ["Michael","zhangshang","李四"]
print("所有list的元素=",element)#输出所有的
print("获取第0个元素%s" %element[0])
print("长度=%d" %len(element))

#获取倒数元素
print("最后一个元素element[-1]=",element[-1])

#越界会报IndexError 异常


#追加元素
element.append('赵六')

print('追加后的元素：',element)

#插入一个元素，需要指定位置，不指定位置会报错

print('插入前的一个长度=%d' %len(element))
element.insert(1,'王五')
print('插入后的一个长度=%d' %len(element))

#删除尾巴元素 删除指定元素的  element.pop(i)
print("element.pop()删除了尾巴元素:",element.pop())

#不同元素的List
list = ["张三",20,"李四"];
print("不同元素的list=",list)

#list里面包含另外一个list
p = ['hello','world']
list.append(p)
print(list)
#获取到p下面的'world 采用p[1]或list[3][1]
print('获取list中p的值=',p[1])

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，
#没有append，insert,pop操作，只能读取
classmates=("zhangshang","李四",20)
print("tuple元组的内容：",classmates)

#练习

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
