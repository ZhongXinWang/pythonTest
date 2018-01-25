# -*- coding:utf-8 -*-

#条件判断 注意好":"

age = int(input("输入年龄："))
if age>=18:
	print('你的年龄:',age)
	print('恭喜你成年了')
else:
	print('你还未满18岁')
	
"""练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖"""

print('---------------练习---------------')
height=1.75
weight=80.5
result = weight/(height*height)
print(result)
if result<18.5:
	print('过轻')
elif result>=18.5 and result<=25:
	print('正常')
elif result>25 and result<=28:
	print('过重')
elif result>28 and result<=32:
	print('肥胖')
else:
	print('严重肥胖')
	

#循环 
#一种是for...in循环
element = ["zhangshang","lisi","wangwu"]
for name in element:
	print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8]:
	sum+=x
print(sum)

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
#注意格式的缩进

length = len(element)
i = 0
while i < length:
	print(element[i])
	i+=1
	if i == 1:
	   break


















