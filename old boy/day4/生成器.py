#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 19:40:17
# @Author  : flying
'''
生成器 只有在调用的时候才会生成相应的数据
只记录当前位置
只有一个__next__()方法
如果推算的算法比较复杂，用类似列表生成器的for循环不能实现时，可以用函数来实现
'''
'''
b = [i*2 for i in range(10)]#列表
print(b)    #>>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18] 列表直接存在内存中，耗费空间
c = ( i*2 for i in range(100000))#生成器
print(c)    #>>><generator object <genexpr> at 0x0000000000843E08>
# for i in c:
#     print(i)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
'''
'''
比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''
'''
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return "game over"
fib(64)
'''
#变成生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b   #变成生成器   yield作用，保存当前状态并返回
        a,b = b,a+b
        n += 1
    return "game over"

#print(fib(64))
f = fib(10)
while True:
    try:
        x = next(f)
        print("f:",x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break


# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())


print("====start loop====")
for i in f:
    print(i)

