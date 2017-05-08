# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# 基础语法 -列表生成式 即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 通用格式 ... for ... in ... if ... 


# 生成x*x的list
arrList = [1,2,3,4,5,6,7,8,9,10]
print('原始list: ',arrList)
print('arrList每一个数字的平方， list ',[x*x for x in arrList])
print('arrList每一个数字的平方 + 偶数， list ',[x*x for x in arrList if x%2 ==0])
print('两个字符串所有可能的不重复排列， list ',[x+y for x in 'xyz' for y in 'xyabc'])



arrTest= ['Hello', 'World', 18, 'Apple', None]
resultTest=arrTest[:]
print('resultTest 原始数据',resultTest)
for i,value in enumerate(resultTest):
	if isinstance(value,str):
		resultTest[i]=value.lower()
print('resultTest 所有字母转成小写: ',resultTest)











