"""
    最小公倍数和最大公约数问题:
        输入二个正整数x0,y0(2≤x0≤100000，2≤y0≤1000000)，求出满足下列条件的P、Q的个数。
            条件:
                1.P、Q是正整数
                2.要求P、Q以x0为最大公约数，以y0为最小公倍数。
        试求，满足条件的所有可能的两个正整数的个数。
"""


# 计算最大公约数函数
def gcd(x: int, y: int) -> int:
    """
    递归实现欧几里得算法，计算x与y的最大公约数，
    :param x: 整数x
    :param y: 整数y
    :return: 返回x与y的最大公约数
    """
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def gcd_non_rec(x: int, y: int) -> int:
    """
    非递归实现欧几里得算法，计算x与y的最大公约数，
    :param x: 整数x
    :param y: 整数y
    :return: 返回x与y的最大公约数
    """
    while y != 0:
        r = x % y
        x = y
        y = r

    return x


# 计算最小公倍数（基于最大公约数）
def lcm(x: int, y: int) -> int:
    """
    基于最大公约数实现求解最小公倍数
    :param x: 整数x
    :param y: 整数y
    :return: 返回x与y的最小公倍数
    """
    mul = int(x * y / gcd(x, y))
    return mul


# print(gcd(12, 15), lcm(12, 15))
# print(gcd_non_rec(12, 15))

def num_of_gcd_and_lcm(x, y):
    count = 0
    mul = x * y
    for p in range(x, y + 1, x):
        q = mul / p
        if p <= q:
            if gcd_non_rec(p, q) == x:
                count += 1
        # for q in range(x, y + 1, x):
        #     if p <= q:
        #         if gcd(p, q) == x and lcm(p, q) == y:
        #             count += 1
        #             # print(p, " ", q)
    return count * 2
    # return count


a, b = map(int, input().split())
print(num_of_gcd_and_lcm(a, b))
# print(gcd(a, b), lcm(a, b))
