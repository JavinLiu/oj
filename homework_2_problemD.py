"""

"""


def f(n, m):
    """
    对长度为n的集合进行子集划分，将其划分为m个元素互不重复的子集
    :param n: 集合元素数量
    :param m: 划分后所含子集的数量
    :return: 可以得到的不同划分数
    """
    if m == 1:
        return 1
    elif m == n:
        return 1
    else:
        return f(n - 1, m - 1) + m * f(n - 1, m)


# n = int(input())
# result = 0
# for i in range(1, n + 1):
#     result += f(n, i)
# print(result)

while True:
    try:
        n = int(input())
        result = 0
        for i in range(1, n + 1):
            result += f(n, i)
        print(result)
    except:
        break
