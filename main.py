import time
from math import sqrt


def decorator(func):
    def wrapper():
        start_time = time.time()
        print(f'Была вызвана функция {func.__name__}.')
        func()
        print(f'Время затраченное на выполненеие функции равно {time.time()-start_time}')
    return wrapper


@decorator
def square():
    SQFT_PER_ACRE = 0.00002295684113830358 * length * width
    print('{} акров'.format(SQFT_PER_ACRE))


@decorator
def object_speed():
    a = 9.8
    vf = sqrt(2 * a * d)
    print(f'Скорость объекта во время его соприкосновения с землей: {vf} м/с^2.')


length = float(input('Длина: '))
width = float(input('Ширина: '))
square()

d = float(input('Дистанция: '))
object_speed()
