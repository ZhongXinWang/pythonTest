# -*- coding: utf-8 -*-
#定义一个函数

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
		
print(my_abs(99))


#带有检测函数类型是否符合的函数

def my_abs1(x):
	if not isinstance(x,(int,float)):
		raise TypeError('类型不对应')
	if x >= 0:
		return x
	else:
		return -x
		
		
print(my_abs1(50))
#print(my_abs1('50'))


#返回多个值得函数
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x,y)
'''原来返回值是一个tuple！但是，在语法上，
返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''