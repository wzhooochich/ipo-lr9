from collision.intersectionAreaMultiRect import *


def get_float_input(prompt):
    """Запрашивает у пользователя ввод числа с плавающей точкой."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка ввода: Пожалуйста, введите число.")

def get_coordinates_from_input(prompt):
  """Запрашивает у пользователя пару координат."""
  while True:
    try:
        x = get_float_input(prompt + " x-координату: ")
        y = get_float_input(prompt + " y-координату: ")
        return (x,y)
    except ValueError as e:
      print(f"Ошибка: {e}. Попробуйте еще раз.")

def get_rectangle_from_input(prompt):
    """Запрашивает у пользователя координаты прямоугольника."""
    print(f"Введите координаты для {prompt}:")
    coord1 = get_coordinates_from_input("левого нижнего угла")
    coord2 = get_coordinates_from_input("правого верхнего угла")
    return [coord1, coord2]

status = True

while status:
    decor = "=" * 20
    print(f"{decor}{decor}")
    print("Выберите функцию, чтобы применить ее")
    print("1 - isCorrectRect")
    print("2 - isCollisionRect")
    print("3 - intersectionAreaRect")
    print("4 - intersectionAreaMultiRect")
    print("5 - Выйти из программы")
    print(decor + decor)
    a = input("Введите номер операции: ")
    print(decor + decor)

    if a == '1':
        rect = get_rectangle_from_input("Введите координаты для isCorrectRect")
        print(isCorrectRect(rect))
    elif a == '2':
        rect1 = get_rectangle_from_input("Введите координаты первого прямоугольника для isCollisionRect")
        rect2 = get_rectangle_from_input("Введите координаты второго прямоугольника для isCollisionRect")
        print(isColisionRect(rect1, rect2))
    elif a == '3':
        rect1 = get_rectangle_from_input("Введите координаты первого прямоугольника для intersectionAreaRect")
        rect2 = get_rectangle_from_input("Введите координаты второго прямоугольника для intersectionAreaRect")
        print(f'площадь пересечения равна : {intersectionAreaRect(rect1, rect2)}.')
    elif a == '4':
        rectangles = []
        while True:
            add_more = input("Хотите добавить еще прямоугольник для intersectionAreaMultiRect? (да/нет): ").lower()
            if add_more == "нет" :
                break
            else :
                rect = get_rectangle_from_input("Введите координаты прямоугольника")
                rectangles.append(rect)
        print(intersectionAreaMultiRect(rectangles)) if rectangles else print("Не введен ни один прямоугольник")
    elif a == '5':
        status = False
    else:
        print("Введите корректное значение")
