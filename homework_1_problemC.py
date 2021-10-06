"""
    全排列
        输入两个自然数m,n 1< =n< =20，1< =m< =n!
        输出n个数的第m种全排列。
"""

from math import factorial


def find_permutations(n, m):
    """
    找到n个数的第m个全排列
    :param n: 数字个数
    :param m: 所需找到的全排列位置
    :return: 保存全排列数字的列表
    """
    if n == 1:
        r.append(l[0])
    else:
        x = int((m - 1) / factorial(n - 1))  # 当前输出数字
        r.append(l[x])  # 结果中添加数字
        l.remove(l[x])  # 原列表去除已确定数字
        y = int((m - 1) % factorial(n - 1)) + 1  # 剩余n-1位数的第y个排列
        n = n - 1
        m = y
        find_permutations(n, m)

    return r


n, m = map(int, input().split())
r = []
l = list(range(1, n + 1))
# print(find_permutations(n, m))

# 输出元素用空格隔开（注意：最后一个元素后没有空格）
print(" ".join(str(x) for x in find_permutations(n, m)))
