from collision.isCorrectRect import *
from collision.isCollisionRect import *


def intersectionAreaRect(list1, list2):
    if not isCorrectRect(list1):
        raise Exception("1-й прямоугольник некорректный")
    if not isCorrectRect(list2):
        raise Exception("2-й прямоугольник некорректный")
    
    if not isColisionRect(list1, list2):
        return 0
    
    cortege1_1 = list1[0]
    cortege2_1 = list1[1]
    cortege1_2 = list2[0]
    cortege2_2 = list2[1]

    x1 = cortege1_1[0]
    y1 = cortege1_1[1]
    x2 = cortege2_1[0]
    y2 = cortege2_1[1]
    x3 = cortege1_2[0]
    y3 = cortege1_2[1]
    x4 = cortege2_2[0]
    y4 = cortege2_2[1]

    x_intersect = max(0, min(x2, x4) - max(x1, x3))
    y_intersect = max(0, min(y2, y4) - max(y1, y3))

    return x_intersect * y_intersect
