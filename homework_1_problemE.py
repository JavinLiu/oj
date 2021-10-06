"""
    岳麓山上打水
        今天天气好晴朗，处处好风光，好风光！蝴蝶儿忙啊，蜜蜂也忙，信息组的同学们更加忙。
        最近，由于XX原因，大家不得不到岳麓山去提水。55555555~，好累啊。
        信息组有一个容量为q升的大缸，由于大家都很自觉，不愿意浪费水，所以每次都会刚好把缸盛满。
        但是，信息组并没有桶子（或者瓢）来舀水，作为组内的生活委员，你必须肩负重任，到新一佳去买桶子。
        新一佳有p种桶子，每种桶子都有无穷多个^_^，且价钱一样。由于大家都很节约，所以你必须尽量少买桶子。
        如果有多种方案，你必须选择“更小”的那种方案，即：
            把这两个方案的集合（不同大小的桶子组成）按升序排序，比较第一个桶，选择第一个桶容积较小的一个。
            如果第一个桶相同，比较第二个桶，也按上面的方法选择。否则继续这样的比较，直到相比较的两个桶不一致为止。
            例如，集合{3，5，7，三} 比集合 {3，6，7，8} 要好。
        为了把缸装满水，大家可以先从岳麓山的井里把桶装满水提回来，然后倒进缸里。
        为了不十分麻烦或者浪费宝贵的水资源，大家决不把缸里的水倒出来或者把桶里的水倒掉，也不会把桶里的水再倒回井中，（这样会污染井水）。
        当然，一个桶可以使用多次。例如，用一个容积为 1 升的桶可以将任意容量的大缸装满水。而其它的组合就要麻烦些。
"""

p = int(input())  # 缸容量
q = int(input())  # 桶种类
w = []  # 桶容量
result = []  # 记录当前组合
r = []  # 存储满足条件的组合
flag = p  # 最后一次跳出递归时用于判定
for i in range(q):
    w.append(int(input()))
# v = list(range(q, 0, -1))  # 为每一个桶假定一个价值, 桶容量越小价值越高，越优先选

# print(p, q, w, v)


def find_combination(i, p, q, w, result, r):
    """
    寻找可以满足条件的桶的组合搭配
    :param i: 当前所选桶的类型
    :param p: 挡墙缸的容量
    :param q: 桶的种类个数
    :param w: 桶的容量
    :param result: 当前组合
    :param r: 满足条件的各种组合
    :return: r
    """
    if p == 0:
        temp = result.copy()  # 创建当前组合的副本，避免pop元素后一起改变
        r.append(temp)  # 添加满足条件的组合
        result.pop()  # 跳出递归，去除最后一个元素
        return
    if i >= q:
        if p != flag:  # 若是最底层递归，此时result为空，不能pop
            result.pop()  # 跳出递归，去除最后一个元素
        return
    if w[i] > p:
        result.pop()  # 跳出递归，去除最后一个元素
        return
    else:
        result.append(w[i])  # 添加到当前组合
        find_combination(i, p - w[i], q, w, result, r)  # 继续选取当前类型
        find_combination(i + 1, p, q, w, result, r)  # 选取下一类型


find_combination(0, p, q, w, result, r)
# print(r)
# print(len(r))
min = sum(list(set(r[0])))
k = []
for i in range(1, len(r)):
    now = list(set(r[i]))
    if sum(now) < min:
        k = now
        min = sum(now)

print(len(k), " ".join(str(x) for x in k))
