"""
    Superprime
        农民约翰的母牛总是生产出最好的肋骨。你能通过农民约翰和美国农业部标记在每根肋骨上的数字认出它们。
        农民约翰确定他卖给买方的是真正的质数肋骨,是因为从右边开始切下肋骨,每次还剩下的肋骨上的数字都组成一个质数,举例来说:
        7 3 3 1
        全部肋骨上的数字7331是质数;
        三根肋骨733是质数;
        二根肋骨73是质数;
        当然,最后一根肋骨7也是质数。
        7331 被叫做长度 4 的特殊质数。
        写一个程序对给定的肋骨的数目 N (1< =N< =8),求出所有的特殊质数。数字1不被看作一个质数。
"""

from math import sqrt
from time import time


def is_prime(x):
    """
    判断所给数字是否为质数
    :param x: 输入数字
    :return: True/False
    """
    if x == 0 or x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def is_prime_variant(x):
    while x > 0:
        if not is_prime(x):
            return False
        x = int((x - x % 10) / 10)
    return True


def super_prime(N):
    """
    求解长度为N的特殊质数
    :param N: 长度
    :return: result列表，保存所有满足条件的质数
    """
    # result = []
    k = 10 ** (N - 1)
    low = 2 * k
    high = 8 * k

    for i in range(low, high):
        r = int(i / k)
        if r == 2 or r == 3 or r == 5 or r == 7:
            # 排除最高位不是质数的
            if is_prime_variant(i):
                # result.append(i)
                print(i)


N = int(input())
start = time()
super_prime(N)
end = time()
print("%.2f ms" % ((end - start) * 100))
# print(super_prime(N))

# if is_prime(2001):
#     print("yes")
# else:
#     print("no")
# if is_prime_variant(2334):
#     print("yes")
# else:
#     print("no")


# 新的方法
# def is_prime(x):
#     """
#     判断所给数字是否为质数
#     :param x: 输入数字
#     :return: True/False
#     """
#     if x == 0 or x == 1:
#         return False
#     for i in range(2, int(sqrt(x) + 1)):
#         if x % i == 0:
#             return False
#     return True
#
#
# end = [0, 1, 3, 5, 7, 9]
# begin = [2, 3, 5, 7]
#
#
# def is_prime_variant(x, y, n):
#     """
#     1.若当前长度=n则输出，并去除最后一位数字(递归出栈)
#     2.选取要添加的数字e，在当前数后增加数字e，得到新的数，判断是否为质数
#     3.若其是质数，重复1，2，3；（递归入栈）
#       若其不是质数，则回到1；（递归出栈：不满足条件）
#     :param x: 当前数字
#     :param y: 当前位数
#     :param n: 指定位数
#     :return:
#     """
#     if y == n:
#         print(x)
#     if y < n:
#         for e in end:
#             if is_prime(x * 10 + e):
#                 is_prime_variant(x * 10 + e, y + 1, n)
#
#
# def super_prime(N):
#     """
#     计算长为N的特殊质数
#     每轮加一位数字，判断是否为质数，若是则继续加，直至长为N，若不是换一个数字
#     :param N: 数字位数
#     :return: 所有满足条件的数字
#     """
#     for b in begin:
#         is_prime_variant(b, 1, N)
#
#
# N = int(input())
# # start = time()
# super_prime(N)
# # end = time()
# # print("%.2f ms" % ((end - start) * 100))
