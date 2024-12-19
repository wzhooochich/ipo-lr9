from collision.isCorrectRect import *
from collision.intersectionAreaRect import *


def intersectionAreaMultiRect(rectangles):
    
    if not rectangles:
        return 0

    for rect in rectangles:
        if not isCorrectRect(rect):
             raise Exception("Обнаружен некорректный прямоугольник")

    total_area = 0
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            total_area += intersectionAreaRect(rectangles[i], rectangles[j])
    return total_area
