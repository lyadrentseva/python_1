# 1. Исключения.
# Написать функцию, принимающую бесконечное количество аргументов.
# Внутри функции должна быть задана переменная a = 100.
# Функция должна попытаться последовательно поделить переменную a на каждый
# из аргументов и возвратить результат.
# - При ошибке «операция применена к объекту несоответствующего типа» - должна
# выдаваться надпись «Ошибка в типе данных» и функция должна пройтись по каждому аргументу.
# Если аргумент типа int или float, то переменная a делится на него,
# если другого типа – переменная a умножается на 10.
# - При наличии нуля среди аргументов – выдаётся надпись «Деление на ноль».
#  Функция должна пройтись по каждому аргументу. Если аргумент равен нулю,
# то переменная a делится на 10, если нет – переменная a делится на сам аргумент.
# - Функция в любом случае при завершении программы выдаёт надпись
# «Программа выполнена» и возвращает значение переменной a.

def f1(*args):
    a = 100
    try:
        for i in args:
            print(a/i)
    except TypeError:
        print('Ошибка в типе данных. a*10 = ' + str(a*10))
    except ZeroDivisionError:
        print('Деление на ноль. a*10 =' + str(a*10))
    finally:
        print('Программа выполнена. a = ' + str(a))

# f1(10,12,'a')

# 2. Исключения. Напишите функцию, которая бы принимала в аргументы значения,
# необходимые для решения квадратного уравнения. Если ваши значения приведут к ответу:
# - не имеет вещественных корней – должна вызываться ошибка с соответствующим текстом;
# - имеет один вещественный корень(т.е. два одинаковых корня) -
# должна вызываться ошибка с соответствующим текстом;
# - имеет два вещественных корня – функция возвращает красивую строку
# с корнями данного уравнения.

class MyException1(Exception):      # создаю свои классы исключений, они
    pass                            # наследуются от класса Exception
class MyException2(Exception):
    pass

def f2(a,b,c):
    try:
        d = b**2 -4*a*c             # расчитываю дискриминант d
        if d < 0:
            raise MyException1      #  в случае d < 0 бросаю исключение MyException1
        elif d == 0:
            raise MyException2      #  в случае d = 0 бросаю исключение MyException2
        else:
            sqrt_d = d**0.5
            print('first: ' + str((-b + sqrt_d)/(2*a)))
            print('second: ' + str((-b - sqrt_d)/(2*a)))
    except MyException1:
        print('Уравнение не имеет вещественных корней')
    except MyException2:
        print('Уравнение имеет один вещественный корень(т.е. два одинаковых корня)' + str(-b/(2*a)))

# f2(2,7,0)
# f2(2,1,3)
# f2(1,4,4)

# 3. Hashlib. Декодировать 16-ричное значение. Исходная строка может состоять
# из английских букв в верхнем и нижнем регистрах, а также цифр.
# Длина строки может быть от 1 символа до 4.
# Код: 'f62ad8510f5d33be07ad33bd1b1a05ad0c1844b7512bbc06a27ad54923f403e4'

import string
import time
import hashlib
def f3(s_check):
    t1 = time.time()
    alph = string.ascii_letters + string.digits
    for n in range(1,5):
        for i in range(len(alph)):
            if n == 1:
                s = alph[i]
                s2 = hashlib.sha256(bytes(s, encoding='utf-8')).hexdigest()
                if s_check == s2:
                    print(s)
                    break
                else:
                    pass
            else:
                for j in range(len(alph)):
                    if n == 2:
                        s = alph[i] + alph[j]
                        s2 = hashlib.sha256(bytes(s, encoding='utf-8')).hexdigest()
                        if s_check == s2:
                            print(s)
                            break
                        else:
                            pass
                    else:
                        for k in range(len(alph)):
                            if n == 3:
                                s = alph[i] + alph[j] + alph[k]
                                s2 = hashlib.sha256(bytes(s, encoding='utf-8')).hexdigest()
                                if s_check == s2:
                                    print(s)
                                    break
                                else:
                                    pass
                            else:
                                for m in range(len(alph)):
                                    s = alph[i] + alph[j] + alph[k] + alph[m]
                                    s2 = hashlib.sha256(bytes(s, encoding='utf-8')).hexdigest()
                                    if s_check == s2:
                                         print(s)
                                         break
                                    else:
                                         pass


    t2 = time.time()
    print(t2 - t1)

# f3('f62ad8510f5d33be07ad33bd1b1a05ad0c1844b7512bbc06a27ad54923f403e4')
# answer == '9May'


# 4. Pillow. Создать функцию, принимающую в себя 5 аргументов:
# - ширину изображения в пикселях;
# - высоту изображения в пикселях;
# - толщину линии(размер промежутка) в пикселях;
# - путь для сохранения изображения;
# - название изображения.
# Функция должна создавать изображение заданной ширины и высоты,
# которое бы из центральной точки изображения разрисовывалось бы
# линиями заданной толщины с интервалом, равным ширине линии.
# Цвет полотна и линий – рандомится.

from PIL import Image, ImageDraw
from random import randint

def f4(w,h,th,path,name):
    color_canvas = (randint(0,255),randint(0,255),randint(0,255))
    color_line= (randint(0,255),randint(0,255),randint(0,255))
    x = Image.new('RGB', (w, h), color=color_canvas)
    #найти центр полотна
    cx = x.size[0]/2
    cy = x.size[1]/2
    draw = ImageDraw.Draw(x)
    #тут будет меняться конечная точка прямой
    lx = []
    ly = []
    for i in range(0,h+th,th):
        lx.append(i)
        ly.append(0)
    for j in range(0,w+th,th):
        lx.append(0)
        ly.append(j)

    for i in range(0,h+th,th):
        lx.append(i)
        ly.append(w)
    for j in range(0,w+th,th):
        lx.append(h)
        ly.append(j)


    # я отклонилась от задания и приняла толщину линии меньше th1 = 20
    th1 = 20
    for n in range(0,len(lx)):
        draw.line((cx,cy,lx[n],ly[n]), fill=color_line, width=th1)
    x.save(path + name)

f4(500,500,100,r"C:\Users\eyadrenceva\PycharmProjects\python_belhard", "picture.jpg")


# 5. Hashlib + pillow. Функция принимает один аргумент – строку.
# Если функция получила другой тип данных – то преобразовывает его в строку.
# Затем данную строку превращает в
# 16-ричный ключ с помощью алгоритма hashlib sha256.
#  Из полученной строки-ключа необходимо вычленить:
# - все цифры в отдельную строку(строка digits);
# - все буквы в отдельную строку(строка alphas).
# Строку из букв с помощью встроенной функции ord полностью переводим в цифровую строку (строка ords).
# Сумма цифр в этой строке – это высота и ширина вашего будущего изображения.
# Сумма цифр в строке digits – это параметр, до которого будет рандомится цвет вашего изображения.
# Если полученная сумма не укладывается в рамки 0-255, то отнимайте от него по 31, пока оно не войдёт в рамки.
#  Например, если сумма получилась = 175, то цвет фона будет кортежем
#  из 3-х рандомных чисел от 0 до 175 – (23, 170, 111)
# Далее получите строку ords_digits, представляющую собой объединение строк ords и digits.
# Если длина строки нечётная – обрежьте её на 1.
# Каждые 2 цифры этой строки – координаты линии, которую нужно
# нарисовать на вашем изображении.
#  Ширина линии – рандомится от 1 до 25.
#  Цвет линии – 3 рандомных числа: от 0 до длины строки ords_digits,
# длина строки ords_digits, от длины строки ords_digits до 255.
# Например, если длина ords_digits = 99, то цвет будет – (34, 99, 248).
# Полученный шедевр должен куда-то сохраняться под каким-то именем в формате jpg.

###библиотеки нужные, уже заимпортированы###
# import hashlib # from PIL import Image, ImageDraw # from random import randint

def f5(s):
    if str(type(s)) != "<class 'str'>":      # Если функция получила другой тип данных – то преобразовывает его в строку.
        s = str(s)
    else:
        s = s
    s2 = str(hashlib.sha256(bytes(s, encoding='utf-8')).hexdigest())  # 16-ричный ключ с помощью алгоритма hashlib sha256

    l_d = []
    l_a = []
    digits = ''
    for i in s2:
        if i.isalpha():
            l_a.append(i)
        elif i.isdigit():
            digits += i
            l_d.append(int(i))
        else:
            pass

    # Строку из букв с помощью встроенной функции ord полностью переводим в цифровую строку (строка ords)
    # получаем высоту == ширину рисунка
    hight = 0
    ords = ''
    for i in l_a:
        hight += ord(i)
        ords += str(ord(i))

    #параметр, до которого будет рандомится цвет вашего изображения
    color_rand = sum(l_d)

    if color_rand < 256:
        color_rand = sum(l_d)
    else:
        while color_rand > 255:
            color_rand -= 31

    color_canvas = (randint(0,color_rand),randint(0,color_rand),randint(0,color_rand))

    ords_digits = ords + digits
    if len(ords_digits)%2 != 0:
        ords_digits = ords_digits[:-1:]
    else:
        ords_digits = ords_digits

    x = Image.new('RGB', (hight, hight), color=color_canvas)
    width_line = randint(0,25)
    color_line = (randint(0,len(ords_digits)),len(ords_digits),randint(len(ords_digits),255))

    draw = ImageDraw.Draw(x)
    for n in range(0,len(ords_digits)-2,4):
        draw.line((int(ords_digits[n]), int(ords_digits[n+1]) ,int(ords_digits[n+2]), int(ords_digits[n+3])), fill=color_line, width=width_line)

    #линий мне было мало, поэтому пусть будут еще элипсы
    for n in range(0,hight, 30):
        draw.ellipse((n, n , n + 20, n+20), fill=color_line, outline=color_line)


    path = r"C:\Users\eyadrenceva\PycharmProjects\python_belhard"
    name = "picture2.jpg"

    x.save(path + name)

f5('djf;iufnvxn.jjioi')
