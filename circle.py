import math

def area(r: int):
    '''
    Принимает радиус окружности, возвращает её площадь.

        Параметр:
            r (int): радиус окружности (целое число)

        Возвращаемое значение:
            square (float): площадь окружности
    '''
    return math.pi * r * r


def perimeter(r: int):
    '''
    Принимает радиус окружности, вощвращает её длину.

        Параметр:
            r (int): радиус окружности (целое число)

        Возвращаемое значение:
            perimeter (float): длина окружности
    '''
    return 2 * math.pi * r
