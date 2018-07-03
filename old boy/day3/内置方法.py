#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-02 20:45:04
# @Author  : flying

print(abs(-5))  #>>>5   取绝对值
print(all([0,-5,3]))    #>>>False   都为真返回为真   print(all([1,2,3]))  >>>True
print(any([0,-5,3]))    #>>>True    有一个为真就是真    print(any([]))  >>>False 为空返回False
print(bin(8))   #>>>0b1000  十进制转二进制
print(oct(9))   #>>>0o11    转8进制
print(hex(15))  #>>>0xf    转成16进制
print(bool(0))  #>>>0是False 1是True  [1]{1}是True  []{}是False
a = bytes("flying",encoding='utf-8')
print(a.capitalize(),a)    #>>>b'Flying' b'flying'  字符串不可以修改
b = bytearray("flying",encoding='utf-8')
b[1] = 50
print(b)    #>>>bytearray(b'f2ying')    把二进制变成一个列表的形式并修改
print(callable([])) #判断是否可以调用》》》False
print(chr(97))  #>>>a   返回ASCII对应的字符
print(ord("a")) #>>>97  返回字符对应的数字

code = '''
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
'''
py_obj = compile(code,'','exec')    #把一段代码转成字符串，之后调用
exec(py_obj)

a = {}
print(dir(a))   #查看有什么内置方法
print(divmod(10,3)) #>>>(3, 1)  返回商和余数

res = filter(lambda n:n>5,range(10))    #过滤出合格的结果
for i in res:
    print(i)    #>>>6,7,8,9

res = map(lambda n:n*n,range(10))   #对传入的值进行处理  [i*i for i in range(10)]
for i in res:
    print(i)    #>>>0.1.4.9.16.25.36.49.64.81

import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res)  #>>>45  累计1+2+3...+9=45

a = frozenset([1,3,3,9,2])  #冻结不可变

print(globals())    #返回当前程序所有的全局变量key：value
#hash对应一个数字 映射关系    折半算法很高效 查找500万的数据折半算法只需要20多次
print(hash("flying"))   #>>>933392888581024306
print(hash("flying"))   #>>>933392888581024306
print(hash("flying"))   #>>>933392888581024306

def test():
    locals_var = 333
    print(locals())
test()
print(globals())
print(globals().get('locals_var'))  #>>>None
print(pow(2,3)) #>>>8   2的3次方

