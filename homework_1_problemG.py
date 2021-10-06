"""
    课堂作业-7-4
    对于一个长为n的数组A0,A1,A2......An-1，
    定义这个数组的得分为(A0 xor A1)+(A1 xor A2)+(A2 xor A3）+......+(An-2 xor An-1) ，
    即相邻两项的异或值的加和，比如数组1 1 2 2的得分为(1 xor 1) + (1 xor 2) + (2 xor 2) = 0+3+0 = 3
    现在你可以重新排列这个数组，问最大得分是多少?
"""

from itertools import permutations
from math import factorial


def next_permutation(nums):
    if len(nums) <= 1:
        return
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            for k in range(len(nums) - 1, i, -1):
                if nums[k] > nums[i]:
                    nums[i], nums[k] = nums[k], nums[i]
                    nums[i + 1:] = sorted(nums[i + 1:])
                    break
            break

        else:
            if i == 0:
                nums.sort()


n = int(input())
a = list(map(int, input().split()))

result = 0
a.sort()
# print(a)
count = 0
all = factorial(n)

while count < all:
    next_permutation(a)
    l = a
    # print(l)
    sum = 0
    for i in range(n - 1):
        sum += l[i] ^ l[i + 1]
    result = max(sum, result)
    count += 1

# for l in list(permutations(a)):
#     sum = 0
#     for i in range(n - 1):
#         sum += l[i] ^ l[i + 1]
#     result = max(sum, result)

# print(1 ^ 2)
# print(a)
print(result)
