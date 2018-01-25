# -*- coding: utf-8 -*-
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

def add(x,y,f):
	return f(x)+f(y)

def myAbs(value):

	if value < 0:
		return (value*-1)
	return value
#传递自定义的函数	函数间的传递 ,函数名也是一个变量名称
f = myAbs
print(f(-5))
print(add(5,6,myAbs))


#Python内建了map()和reduce()函数。 map获得的还是一个存储的序列，reduce可以统计序列获得一个结果
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
#计算数值的平方
def f(x):
	return x*x

print(list(map(f,[1,2,3,4,5,6,7])))

#把这个list所有数字转为字符串：
print(list(map(str,[1,2,3,4,5,6,7])))

'''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
'''
from functools import reduce
def sums(x,y):
	return x+y
#使用reduce获得list下面数的和
print(reduce(sums,[1,2,3,4,5,6,7,8,9]))

#map 和 reduce结合起来,把一个'13579'转化为数值

#使用map获取到转化后的数值列表
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]

print(list(map(char2num,'13579')))

#使用reduce进行数值的转化

def fn(x,y):
	return x*10+y

#结果:
print(reduce(fn,map(char2num,'13579')))



#封装成字符串转化为int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))

print("结果:",str2int('1354789'))

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
	
	return name[0].upper()+name.lower()[1::]
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)

#求积

def prod(L):
	if not isinstance(L,list):
		raise TypeError('输入的类型错误')
	return reduce(lambda x,y:x*y,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
	#转化为数字
	def char2float(s):
	
		return s
		
	def fn(x,y):
	
		return int(x+y)/10**len(y)
		
	
	return reduce(fn,map(char2float,s.split('.')))


print(str2float('123.456'))












