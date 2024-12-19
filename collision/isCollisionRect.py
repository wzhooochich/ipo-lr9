from collision.isCorrectRect import *

def isColisionRect (list1,list2) :
    if not isCorrectRect(list1):
        raise Exception("1й прямоугольник некоректный")
    # переменные для 1 прямоугольника
    cortege1_1=list1[0]
    cortege2_1=list1[1]
    # переменные для 2 прямоугольника
    cortege1_2=list2[0]
    cortege2_2=list2[1]

    if (cortege2_1[0] < cortege1_2[0] or cortege2_2[0] < cortege1_1[0] or cortege2_1[1] < cortege1_2[1] or cortege2_2[1] < cortege1_1[1]):
        return False  # прямоугольники не пересекаются
    else:
        return True   # прямоугольники пересекаются
