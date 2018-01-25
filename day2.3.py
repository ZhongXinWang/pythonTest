# -*- coding: utf-8 -*-
'''
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
#在一个list中，删掉偶数，只保留奇数，可以这么写

def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))


#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
	s = str(n)
	return  s == s[::-1]

output = filter(lambda x:str(x)==str(x)[::-1], range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')