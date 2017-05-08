# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# 基础语法 -迭代


#遍历字典 
myDict = {'name':'张三','age':25,'sex':'男','address':'杭州市西湖区'}

#字典的遍历默认迭代的是key
for key in myDict:
	print('key: ',key);

#迭代value
for value in myDict.values():
	print('value: ',value);


#同时迭代key 和value 
for key,value in myDict.items() :
	print('key: ',key,', value: ',value);

#字符串的迭代
myString="abcdefg"
for value in myString:
	print('字符串 value: ',value);

#判断当前对象是否可以迭代
from collections import Iterable
print('字符串abs是否可以迭代-> ',isinstance('abc', Iterable) );
print('字典是否可以迭代-> ',isinstance({'key1','value1'}, Iterable) );
print('list是否可以迭代-> ',isinstance([1,2], Iterable) );
print('int是否可以迭代-> ',isinstance(1, Iterable) );


#获取下标和value - list
for i,value in enumerate(['value1','value2','value3']):
	print('i= ',i,', value= ',value)

#获取下标和value - dict
for i,value in enumerate({'key1':'value1','key2':'value2','key3':'value3'}):
	print('i= ',i,', value= ',value)






















