# 1. Написать функцию, принимающую одно числовое значение и печатающую квадрат этого числа.

def sq(a=0):
    print(a ** 2)


# sq(2)

# 2. Написать функцию, принимающую число и проверяющую, простое оно или нет.
# Возвращает True, если простое, False, если нет.
def check_num(n=0):
    b = True
    if n == 0 or n == 1 or n == 2:
        b = True
    else:
        for i in range(2, n):  # находим другие делители, кроме 1 и самого числа
            if n % i == 0:
                b = False
                break
    print(b)


# check_num (701)

# 3. Написать функцию, принимающую 2  числовых аргумента: первый – площадь круга,
# второй – площадь квадрата.
# Функция должна напечатать, впишется ли круг в квадрат,
# либо же квадрат впишется в круг, а также вариант полной несостыковки фигур.

def sq_in_circle(sc=0, ss=0):
    if sc == 0 or ss == 0:
        print('фигуры не существуют')
        return

    a = ss ** .5  # сторона квадрата
    r = (sc / 3.14) ** .5  # радиус уруга
    if (2 * r) == a:
        print('круг впишется в квадрат')
    elif (2 * a ** 2) ** .5 == 2 * r:
        print('квадрат впишется в круг')
    else:
        print('полная нестыковка')


# sq_in_circle(sc=12.56, ss=16)
# sq_in_circle(sc=12.56, ss=8)

# 4. Написать функцию, принимающую любое числовое значение и возвращающее строку,
#  где каждая цифра заменена соответствующим словом через пробел (например 12 – ‘one two’).
# Также учесть, что в вещественных числах есть точка, которую нужно заменить словом (‘point’).

def digits_write(n=0):
    d = {'.': 'point', '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', \
         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    n_str = ''
    for i in str(n):
        n_str += d.get(i) + ' '

    return n_str


# print(digits_write(102.56))

# 5. Написать функцию, имитирующую калькулятор. Принимает 3 аргумента: число 1, число 2,
# арифметический знак (например: 111, -120, ‘+’). Возвращает получившийся результат арифметической операции.
# Должна поддерживать: сложение, вычитание, умножение, деление, возведение в степень(одного числа в другое),
# целочисленное деление, взятие остатка. Помнить, что в математике есть ограничения на некоторые операции .

def culc(a=0, b=0, sign=''):

    zd = 'zero division'
    if sign == '*':
        return a * b
    elif sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '/':
        if b != 0:
            return a / b
        else:
            return zd
    elif sign == '**':
        return a ** b
    elif sign == '//':
        if b != 0:
            return a // b
        else:
            return zd
    elif sign == '%':
        if b != 0:
            return a % b
        else:
            return zd


#print(culc(4,-120, '+'))

# 6. Написать функцию, принимающую сколько угодно значений и возвращающую объект-генератор.
# Функция должна делать из каждого введённого аргумента 1-элементный словарь,
# где ключ – сам аргумент, а значение – строка из трёх случайных букв английского алфавита
#  ( например: ‘hello’ – {‘hello’: ‘abc’} ).


def sth(*args):

    from random import choice
    from string import ascii_letters

    for i in args:
        v = ''.join(choice(ascii_letters) for i in range(3))
        yield dict(i=v)

for x in sth(565,'klkjl','8908'):
    print(x)

# 7. *Задачка по желанию. Есть встроенная в Python библиотека time.
#  Создать функцию, которая не принимает аргументов и печатает при вызове
#  текущие дату и время в формате: день.месяц.год_часы:минуты:секунды.
# Например: 09.04.2018_15:55:25.

def t():
    import time
    return time.strftime('%d.%m.%Y_%H:%M:%S', time.localtime())

print(t())

# 8. Есть таблица расхода энергии человеком во время ходьбы.
# Функция принимает в себя 2 аргумента: количество потреблённых килокалорий и массу тела человека.
# Возвращает расстояние в МЕТРАХ(целым числом), которое нужно пройти человеку для расхода этой энергии
# на каждой из скоростей. Каким типом данных возвратить значения – решайте сами.
# Главное, чтобы всё было понятно (лучше всего строка или словарь).

def distance(kkal=0,weight=0):

    l_speed = list(i for i in range(2, 7))

    d_50_59 = dict([(l_speed[0], 1.3), (l_speed[1], 2.0), (l_speed[2], 3), (l_speed[3], 4.0), (l_speed[4], 4.5)])
    d_60_69 = dict([(l_speed[0], 2.2), (l_speed[1], 2.7), (l_speed[2], 3.3), (l_speed[3], 4.7), (l_speed[4], 5.2)])
    d_70_79 = dict([(l_speed[0], 2.6), (l_speed[1], 3.2), (l_speed[2], 3.8), (l_speed[3], 4.8), (l_speed[4], 5.6)])
    d_80_89 = dict([(l_speed[0], 2.8), (l_speed[1], 3.5), (l_speed[2], 4.2), (l_speed[3], 5.3), (l_speed[4], 6.4)])
    d_90_95 = dict({(l_speed[0], 3.0), (l_speed[1], 3.8), (l_speed[2], 4.5), (l_speed[3], 5.7), (l_speed[4], 7.0)})
    d_96_100 = dict([(l_speed[0], 4.0), (l_speed[1], 4.5), (l_speed[2], 5.0), (l_speed[3], 6.7), (l_speed[4], 7.7)])

    if weight > 49 and weight < 60:          #(d_50_59)

        for i in range(2,7):
            #minute =kkal / d_50_59.get(i)
            dist = int((i * 1000 / 60) * (kkal / d_50_59.get(i)))
            str_itog = 'со скоростью ' + str(i) + ' km/h нужно пройти ' + str(dist) + ' метров'
            print(str_itog)

    elif weight > 59 and weight < 70:        #(d_60_69)

        for i in range(2,7):
            dist = int((i * 1000 / 60) * (kkal / d_60_69.get(i)))
            str_itog = 'со скоростью ' + str(i) + ' km/h нужно пройти ' + str(dist) + ' метров'
            print(str_itog)

    elif weight > 69 and weight < 80:        #(d_70_79)

        for i in range(2,7):
            dist = int((i * 1000 / 60) * (kkal / d_70_79.get(i)))
            str_itog = 'со скоростью ' + str(i) + ' km/h нужно пройти ' + str(dist) + ' метров'
            print(str_itog)

    elif weight > 79 and weight < 90:       # (d_80_89)

        for i in range(2, 7):
            dist = int((i * 1000 / 60) * (kkal / d_80_89.get(i)))
            str_itog = 'со скоростью ' + str(i) + ' km/h нужно пройти ' + str(dist) + ' метров'
            print(str_itog)

    elif weight > 89 and weight < 96:        #(d_90_95)

        for i in range(2,7):
            dist = int((i * 1000 / 60) * (kkal / d_90_95.get(i)))
            str_itog = 'со скоростью ' + str(i) + ' km/h нужно пройти ' + str(dist) + ' метров'
            print(str_itog)

    elif  weight > 95 and weight < 101:        #(d_96_100)

        for i in range(2,7):
            dist = int((i * 1000 / 60) * (kkal / d_96_100.get(i)))
            str_itog = 'со скоростью ' + str(i) + ' km/h нужно пройти ' + str(dist) + ' метров'
            print(str_itog)



#distance(kkal=1300,weight=53)
# for i in range(1,101):
#     distance(1300,i)