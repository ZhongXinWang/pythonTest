# -*- coding: utf-8 -*-
'''
Python的函数定义非常简单，但灵活度却非常大。
除了正常定义的必选参数外，还可以使用默认参数、
可变参数和关键字参数，使得函数定义出来的接口，
不但能处理复杂的参数，还可以简化调用者的代码。
'''
#定义一个计算平方的函数

def power(x):
	return x*x;

print(power(2))


#计算x 的 n次方的函数,使用默认参数

def power(x,n=2):
	sum = 1;
	while n >=1:
			sum*=x
			n-=1
	return sum
	
print(power(2,3))

"""
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。
"""

#可变参数

"""
在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
"""

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
	
print(calc(1, 2))
#传递的时候是传递一个list
l = [1,2]
print(calc(*l))

#关键字参数
"""可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
"""
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Bob', 35, city='Beijing')

#传入一个dict
d = {'address':'漳州','code':'350624'}
person('zhangshang',20,**d)


#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
def person1(name,*,age):
	print('name=',name,'age=',age)

#带有一个*。调用的时候使用age=1       命名关键字参数和可变参数只能存在一个
person1('zhangshang',age=1)


#多参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def student(name,age=12,*address,**score):
	print('name=',name,'age=',age,address,score)
	
ll = ['厦门','湖里']
dd = {"语文":100,"数学":80}
student('李四',*ll,**dd)

#任何的多参数都可以使用  student(*ll,**dd) 来进行调用
	
	
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积

def product(x,*y):
	sum = x
	for item in y:
		sum*=item
	
	return sum
	
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
		
#递归函数
#求n的阶乘
def fact(n):
	if(n == 1):
		return 1
	else:
		 return n*fact(n-1)
		
		

print("3的阶乘=",fact(3))	
print("5的阶乘=",fact(100))
	
	
#求汉偌塔

def move(n,a,b,c):
	if(n == 1):
		print(a,'-->',c)
	else:
	
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
	
move(4,'A','B','C')
	
