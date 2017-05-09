# -*- coding: utf-8 -*-

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：	1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#普通方法实现
# def qblFunc(number):
# 	a=0
# 	sum=1
# 	index=0
# 	while index<number:
# 		print(sum)
# 		a,sum = sum,a+sum
# 		index=index+1
# 

#generation方法实现
def qblFuncBygeneration(number):
	a=0
	sum=1
	index=0
	print('著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到')
	while index<number:
		yield sum
		a,sum = sum,a+sum
		index=index+1

	return 'done'

#杨辉三角
def yanghui(n): 
    L=[1]
    for x in range(n):
        yield L
        L=[1]+ [L[i]+L[i+1] for i in range(x)] +[1]

print('杨辉三角')
for t in yanghui(10):
    print(t)


genertaion = qblFuncBygeneration(14)
while True:
	try:
		sum = next(genertaion)
		print(sum)
	except StopIteration as e:
		print(e.value)
		break



