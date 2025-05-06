'''
Напишите на C# или Python библиотеку для поставки внешним клиентам,
которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам.
Дополнительно к работоспособности оценим:

Юнит-тесты
Легкость добавления других фигур
Вычисление площади фигуры без знания типа фигуры в compile-time
Проверку на то, является ли треугольник прямоугольным
'''
import math

class Area:
    @staticmethod
    def is_exist(a,b,c):
        return (a + b > c) and (a + c > b) and (c + b > a)


    @staticmethod
    def is_right_tri(a, b, c):
        a, b, c = sorted([a, b, c])
        if round(a ** 2 + b ** 2, 5) == round(c ** 2, 5):
            return True, (a, b, c)
        return False, (a, b, c)

    @staticmethod
    def tri_sq(a, b, c):
        if Area.is_exist(a, b, c):
            is_right, (x, y, z) = Area.is_right_tri(a, b, c)
            if is_right:
                return f'Площадь прямоугольного треугольника = {(x * y) / 2}'
            else:
                s = (a + b + c) / 2
                S = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                return f'Площадь треугольника = {S}'
        else:
            return 'Такой треугольник не существует'


    @staticmethod
    def check_nums(values:list):
        return all(isinstance(x, (int, float)) for x in values)

    def __init__(self, *args):
        if self.check_nums(args):
            self.a = list(args)
        else:
            raise ValueError('Аргументы должны быть числами')


    def get_area(self):
        count = len(self.a)
        match count:
            case 1: return print(f'площадь круга = {math.pi * (self.a[0] ** 2)}')
            case 2: return print(f'площадь прямоугольника = {self.a[0] * self.a[1]}')
            case 3: return print(self.tri_sq(*self.a))
            case _: return print(f'неверные данные')

if __name__ == '__main__':
    s = Area(1,5,5)
    s.get_area()

