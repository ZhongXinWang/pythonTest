# -*- coding:utf-8 -*-
"""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
"""
d = {"zhangshang":20,"LiSi":20,"wangwu":18}
print('根据name来获得age:',d['zhangshang'])

#添加一个值

d["zhaoliu"]=50
print("字典里的数值:",d)

#如果字典里的name不存在会报错，这时候可以使用in来判断name是否存在

print('zhangshang是否存在:','zhangshang' in d)
print('lisi是否存在:','lisi' in d)

#get获取一个值,不存在返回none

print('不存在的值：',d.get('dddddd'))

#删除一个name
print(d.pop('zhangshang'))

'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
'''

'''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
'''

#要创建一个set，需要提供一个list作为输入集合

s = set([1,2,3,1,5,1,7,9,7])
print(s)

#添加一个重复元素
s.add(1)
#删除一个元素
s.remove(7)

print(s)


















