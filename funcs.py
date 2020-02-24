import numpy as np
from sympy import *

# 反函数inverse function
x,y = symbols('x y')

def inv_func(func,x):
    '''
    计算反函数
    :param func: 原函数
    :param x: 自变量
    :return:
    '''
    return solve(func,x)[0]

def func_density(fx, func, x, y):
    '''
    已知原分布概率密度求函数的概率密度
    :param fx: 自变量的分布
    :param func: 原函数
    :param x: 原分布的自变量
    :param y: 因变量，新分布的自变量
    :return:
    '''
    x1 = solve(func,x)[0]
    fy = fx.subs({x:x1})*Abs(diff(x1,y)) # 导数的绝对值
    return fy

def combine(n,m):
    '''
    计算组合数
    :param n:
    :param m:
    :return:
    '''
    return factorial(n)/(factorial(m)*factorial(n-m))

if __name__ == '__main__':

    print(0)