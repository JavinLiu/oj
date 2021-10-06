"""
    Hanoi双塔问题
        给定A,B,C三根足够长的细柱，在A柱上放有2n个中间有孔的圆盘，共有n个不同的尺寸
        每个尺寸都有两个相同的圆盘，注意这两个圆盘是不加区分的。现要将这些圆盘移到C柱上，在移动过程中可放在B柱上暂存
        要求:
            (1)每次只能移动一个圆盘；
            (2) A、B、C三根细柱上的圆盘都要保持上小下大的顺序；
            任务:设An为2n个圆盘完成上述任务所需的最少移动次数，对于输入的n，输出An。
"""


def num_of_hanoi(n):
    """
    计算汉诺塔问题的移动次数
    :param n:
    :return:
    """
    if n == 1:
        return 1
    return 2 * num_of_hanoi(n - 1) + 1


def num_of_bi_hanoi(n):
    """
    汉诺双塔与单塔移动的区别在于：在汉诺单塔移动一次圆盘时，汉诺双塔移动两次
    故汉诺双塔的移动次数为汉诺单塔移动词数的2倍
    :param n:
    :return:
    """
    return 2*num_of_hanoi(n)


n = int(input())
print(num_of_bi_hanoi(n))
