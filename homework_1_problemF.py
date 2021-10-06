"""
    24点游戏
        几十年前全世界就流行一种数字扑克游戏，至今仍有人乐此不疲．在中国我们把这种游戏称为“算24点”。
        您作为游戏者将得到4个1-13（在扑克牌里用A代替1，J代替11，Q代替12，K代替13）之间的自然数作为操作数，
        而您的任务是对这4个操作数进行适当的算术运算，判断运算结果是否等于24。能输出1，不能输出0。
"""


def game_of_24(numbers):
    """
    递归计算列表numbers中n个数字可以通过四则运算所得到的数字：
        每次选取两个数字进行某一种运算，将结果存入列表，此时列表中数字的个数为n-1，计算n-1个数字可以通过四则运算所得到的数字
    :param numbers: 输入数字
    :return:
    """
    l = len(numbers)
    if len(numbers) == 1:
        if numbers[0] == 24:
            return 1
        else:
            return 0
    # 任意选取两个数
    for i in range(l):
        for j in range(i + 1, l):
            # 去除已经选取的数字
            new_numbers = numbers.copy()
            new_numbers.pop(i)
            new_numbers.pop(j - 1)
            # 暴力求解，遍历四种运算
            # 计算加法，并将结果添加仅列表，计算当前列表内数字可通过四则运算所得的数字
            if game_of_24(add(new_numbers, numbers[i], numbers[j])):
                return True
            # 计算减法，并将结果添加仅列表，计算当前列表内数字可通过四则运算所得的数字
            elif game_of_24(minus(new_numbers, numbers[i], numbers[j])):
                return True
            elif game_of_24(minus(new_numbers, numbers[j], numbers[i])):
                return True
            # 计算乘法，并将结果添加仅列表，计算当前列表内数字可通过四则运算所得的数字
            elif game_of_24(mul(new_numbers, numbers[i], numbers[j])):
                return True
            # 计算除法，并将结果添加仅列表，计算当前列表内数字可通过四则运算所得的数字
            elif numbers[j] != 0 and game_of_24(div(new_numbers, numbers[i], numbers[j])):
                return True
            elif numbers[i] != 0 and game_of_24(div(new_numbers, numbers[j], numbers[i])):
                return True
    return False


# def clear_num():
#     """
#     删除已经使用的数字
#     （令写一个函数是因为连续使用两次pop会导致第二次的pop掉的索引发生变化）
#     :return:
#     """


def add(nums, a, b):
    new_nums = nums.copy()
    new_nums.append(a + b)
    return new_nums


def minus(nums, a, b):
    new_nums = nums.copy()
    new_nums.append(a - b)
    return new_nums


def mul(nums, a, b):
    new_nums = nums.copy()
    new_nums.append(a * b)
    return new_nums


def div(nums, a, b):
    new_nums = nums.copy()
    new_nums.append(a / b)
    return new_nums


a, b, c, d = input().split()
input_number = [a, b, c, d]
number = []
for x in input_number:
    if x == 'A':
        number.append(1)
    elif x == 'J':
        number.append(11)
    elif x == 'Q':
        number.append(12)
    elif x == 'K':
        number.append(13)
    else:
        number.append(int(x))

if game_of_24(number):
    print(1)
else:
    print(0)



# def game_of_24(n):
#     if n == 1:
#         if number[0] - 24 == 0:
#             return True
#         else:
#             return False
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             a = number[i]
#             b = number[j]
#             number[j] = number[n - 1]
#
#             number[i] = a + b
#             if game_of_24(n - 1):
#                 return True
#
#             number[i] = a - b
#             if game_of_24(n - 1):
#                 return True
#             number[i] = b - a
#             if game_of_24(n - 1):
#                 return True
#
#             number[i] = a * b
#             if game_of_24(n - 1):
#                 return True
#
#             if b != 0:
#                 number[i] = a / b
#                 if game_of_24(n - 1):
#                     return True
#             if a != 0:
#                 number[i] = b / a
#                 if game_of_24(n - 1):
#                     return True
#             number[i] = a
#             number[j] = b
#
#
# a, b, c, d = input().split()
# input_number = [a, b, c, d]
# number = []
# for x in input_number:
#     if x == 'A':
#         number.append(1)
#     elif x == 'J':
#         number.append(11)
#     elif x == 'Q':
#         number.append(12)
#     elif x == 'K':
#         number.append(13)
#     else:
#         number.append(int(x))
#
# # print(number)
#
# flag = 0
#
# if game_of_24(4):
#     print(1)
# else:
#     print(0)
