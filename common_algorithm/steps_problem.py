# coding=utf-8
# 一只青蛙每次可以跳1或2阶，问多少种方式跳上n层台阶的房子
def method_num(n):
    a, b = 0, 1
    num = 0
    for i in range(n):
        a,b = b, a+b
    return b

print(method_num(10))

# 第二种方法（记忆）
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@ memo
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))

# 一只青蛙可以跳任意阶台阶，问有多少中方法跳上n层台阶的房子
fib = lambda n: n if n < 2 else 2 * fib(n-1)
print(fib(10))





