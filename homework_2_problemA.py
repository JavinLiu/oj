"""
    肥猫的游戏:
        野猫与胖子，合起来简称肥猫，是一个班的同学，他们也都是数学高手，所以经常在一起讨论数学问题也就不足为奇了。
        一次，野猫遇到了一道有趣的几何游戏题目，便拿给胖子看。
        游戏要求在一个有n个顶点凸多边形上进行，这个凸多边形的n-3条对角线将多边形分成n-2个三角形，这n-3条对角线在多边形的顶点相交。
        三角形中的一个被染成黑色，其余是白色。双方轮流进行游戏，当轮到一方时，他必须沿着画好的对角线，从多边形上切下一个三角形。
        切下黑色三角形的一方获胜。胖子一看觉得确实很有趣，不如就一起玩玩吧。假设游戏由野猫先开始，那么野猫是否有必胜的策略呢？
        请写一个程序帮助野猫算一算。
    输入数据：
        第一行为一个整数 n (4≤n<5×10^3)，表示多边形的顶点数，多边形的顶点由 0 至 n－1 顺时针标号。
        接着的 n−2 行描述组成多边形的三角形。第 i+1 行  (1≤i≤n−2) 有三个空格分隔的非负整数 a,b,c，它们是第 i 个三角形的顶点编号。
        第一个给出的三角形是黑色的。
    输出数据：
        只有一行，倘若野猫有必胜策略，输出JMcat Win；否则，输出 PZ Win 。（注意大小写和空格）

"""

n = int(input())
black = list(map(int, input().split()))
white = []
for i in range(1, n - 2):
        temp = list(map(int, input().split()))
        white.append(temp)
# print(black)
# print(white)
if n % 2 == 0:
    print('JMcat Win')
else:
    min_num = black[0]
    max_num = black[0]
    for i in range(1, 3):
        if black[i] < min_num:
            min_num = black[i]
        if black[i] > max_num:
            max_num = black[i]
    if min_num == 0:
        if max_num == n - 1 or max_num - min_num == 2:
            print('JMcat Win')
        else:
            print('PZ Win')
    else:
        if max_num - min_num == 2:
            print('JMcat Win')
        else:
            print('PZ Win')


