from math import sqrt


def get_point_list():
    points = []
    points_num = int(input())
    for i in range(points_num):
        x, y = map(float, input().split())
        points.append([x, y])
    return points


def calculate_distance(p, q):
    """
    #     计算p,q两点间的距离
    #     :param p: p:[x,y]
    #     :param q: q:[x,y]
    #     :return: d=sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
    #     """
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def get_closest_pair_of_points(points, left_edge, right_edge):
    """
    获取最近点对
    :param points: 存储点坐标的列表
    :param left_edge: 列表起始下标
    :param right_edge: 列表结束下标
    :return: [left_edge,right_edge,distance]
    """
    if right_edge <= left_edge:  # 一个点，返回无限大
        return [0, 0, float('inf')]
    if right_edge - left_edge == 1:  # 两个点，直接求解
        return [left_edge, right_edge, calculate_distance(points[left_edge], points[right_edge])]
    if right_edge - left_edge == 2:  # 三个点，求距离找最小
        left_points_distance = calculate_distance(points[left_edge], points[left_edge + 1])
        mid_points_distance = calculate_distance(points[left_edge + 1], points[right_edge])
        right_points_distance = calculate_distance(points[left_edge], points[right_edge])
        min_distance = max(left_points_distance, mid_points_distance, right_points_distance)
        if min_distance == left_points_distance:
            return [left_edge, left_edge + 1, left_points_distance]
        elif min_distance == mid_points_distance:
            return [left_edge + 1, right_edge, mid_points_distance]
        else:
            return [left_edge, right_edge, right_points_distance]
    # 四个点，进行分治
    mid_position = left_edge + (right_edge - left_edge) // 2
    result_left = get_closest_pair_of_points(points, left_edge, mid_position)
    result_right = get_closest_pair_of_points(points, mid_position + 1, right_edge)
    d = min(result_left[2], result_right[2])
    # 计算中线附近的点中的最近点对
    i = j = mid_position
    while i >= left_edge:  # 寻找左侧横坐标x满足条件的值
        if points[mid_position][0] - points[i][0] < d:
            i -= 1
        else:
            break
    while j <= right_edge:  # 寻找右侧横坐标x满足条件的值
        if points[j][0] - points[mid_position][0] < d:
            j += 1
        else:
            break

    result_mid = [0, 0, float('inf')]
    for left_point in range(i + 1 if i < mid_position else i, mid_position + 1):  # i会停在左边第一个不满足条件的横坐标处
        for right_point in range(mid_position + 1, j):  # j会停在右边第一个不满足条件的横坐标处
            distance = calculate_distance(points[left_point], points[right_point])
            if distance < result_mid[2]:
                result_mid = [left_point, right_point, distance]
    min_distance = min(result_left[2], result_mid[2], result_right[2])
    if min_distance == result_left[2]:
        return result_left
    elif min_distance == result_mid[2]:
        return result_mid
    else:
        return result_right


points_list = get_point_list()
# print(p)
points_list = sorted(points_list)
# p = sorted(p, key=lambda x: x[0])
# p = sorted(p, key=lambda x: x[1])
# print(p)
result = get_closest_pair_of_points(points_list, 0, len(points_list) - 1)

# print("最近的两个点：" + str(points_list[result[0]]) + ", " + str(points_list[result[1]]))
print('%.2f' % result[2])

