"""
    Easy Selection
        这个游戏是这样的，wind先写下一排数。既然是一排，当然有首尾咯。
        wind和小杉(lolanv)每次只能从这排数的头或尾取一个数。
        最后谁取的数的和多，谁就赢了。如果两人的和一样多，先取者胜。
        有天swgr看到他们俩在玩这个游戏，很好奇。
        他想知道，在两人总是做出最优决策的情况下（两个人的智商都是很高的……），
        谁能取得最终的胜利呢？
    输入数据
        第一行为一个数 k (k≤10)， 表示有 k 组测试数据。
        以下 k 组测试数据。
        每组测试数据中，第一行仅有一个偶数 n (0<n<104)
        第二行也仅有一个数 ，0 表示wind先取数 ，1 表示小杉  (lolanv) 先取数
        第三行有 n 个数，是wind给出的一排数。这 n 个数的绝对值均不超过1e6
    输出数据
        对每组测试数据输出一行
        表示在两人总是做出最优决策的情况下，
        最终的胜利者的名字，即"wind"或"lolanv"（引号不输出）。
"""

k = int(input())
first = []
for i in range(k):
    n = input()
    first.append(int(input()))
    num_list = input().split()

for i in range(k):
    if first[i] == 0:
        print('wind')
    else:
        print('lolanv')