# -*- coding: utf-8 -*-
#切片

#不使用切片获取list中前n个元素

def getListEle(n,l=None):
	if l == None:
		l = ['zhangsang','lisi','wangwu','ddddd']
	if n>=len(l):
		print('获取的元素个数越界')
		return
	rs = []
	for i in range(n):
		rs.append(l[i])
		
	return rs
	

print(getListEle(2))

#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。

def getListEle1(n,l=None):
	if l == None:
		l = ['zhangsang','lisi','wangwu','ddddd']
	if n>=len(l):
		print('获取的元素个数越界')
		return
	return l[0:n]
	
print(getListEle1(2))

#从索引0开始取，直到索引n为止，但不包括索引n
#记住倒数第一个元素的索引是-1   L[-2:-1]  后10个数  L[-10:]
'''
def trim(s):

	i = 0
	#去除前空格
	for item in s:
		if(item == ' '):
			i+=1
		else:
			break
	s = s[i::]
	#判断是否为空
	l = len(s)
	if l == 0:
		return s
	#去除尾巴的空格	
	i = -1
	while 1:
		if s[i] != ' ':
			break
		i-=1
	#判断是否是有空格
	if i == -1:
		s = s[0::]
	else:
		s = s[0:i+1]
		
	return s
'''
def trim(s):
    if len(s)==0:
        return s
    elif s[0]==' ':
        return trim(s[1:])
    elif s[-1]==' ':
        return trim(s[:-1])
    else:
        return s
		
if trim('hello  ') != 'hello':
	print('测试失败!')
elif trim('  hello') != 'hello':
	print('测试失败!')
elif trim('  hello  ') != 'hello':
	print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
	print('测试失败!')
elif trim('') != '':
	print('测试失败!')
elif trim('       ') != '':
	print('测试失败!')
else:
	print('测试成功!')
	
#迭代

#判断一个对象是否可以被迭代
from collections import Iterable
if isinstance(213,Iterable):
	print('可以被迭代')
else:
	print('该值无法被迭代')
	
	
#带下标的for循环
for i,value in enumerate(['A','B','C']):
	print("i=",i,"value=",value)

	
	
#请使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(l):
	if len(l) == 0:
		return (None,None)
	min = l[0] #默认第一个数最小
	max = l[0] #默认第一个数最大
	for i,value in enumerate(l):
		if i == 0:
			continue
		if value<min:
			min = value
		if value>max:
			max = value
			
	return (min,max)



# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

	
'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
'''

for i in range(10):
	print(i)
#生成列表 生成[1x1, 2x2, 3x3, ..., 10x10]

L = [x*x for x in range(1,11)]
print('列表生成：',L)

#还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']
print('全排列：',L)

#引入os模块
import os
print([d for d in os.listdir('.')])

#x.lower()转化为小写，如果遇到数字会报错，那么在末尾添加，约束isinstance(x,str)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)


#生成器 generator  只要把一个列表生成式的[]改成()

L = (x*x for x in range(1,10))
#迭代数据
for i in L:
	print("生成器生成的数据",i)










	
	