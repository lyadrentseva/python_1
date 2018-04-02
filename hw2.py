#*********************************   ДЗ №2  *********************************************
# #********************************** IF    ********************************************
# 1. Запросить у пользователя два числа с помощью функции input().
# - Если первое больше второго, то вычислить их разницу и вывести данные на печать.
# - Если второе число больше первого, то вычислить их сумму и вывести на печать
# - Если оба числа равны, то вывести это значение на печать.

a, b = int(input('Введите первое число:')), int(input('Введите второе число:'))
if a > b:
    print(a - b)
elif a < b:
    print(a + b)
else:
    print(a)

# 2. Запросить у пользователя ввести любое значение (input()).
# Если введённая строка состоит только из цифр, то вывести сообщение (‘Вы ввели цифры’);
# Если введённая строка состоит только из букв, то вывести сообщение (‘Вы ввели буквы’);
# Если присутствуют другие символы, то вывести текст данной строки.

s = input('Введите любое значение:')
if s.isdigit():
    print('Вы ввели цифры')
elif s.isalpha():
    print('Вы ввели буквы')
else:
    print(s)


# 3. Требуется определить, является ли данный год високосным (вводить через input()).
# Високосными годами считаются те годы, порядковый номер которых либо кратен 4, но при этом не кратен 100,
# либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
# Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае.

v_year = int(input('Введите год:'))
if (v_year % 4 == 0 and v_year % 100 != 0) or (v_year % 400 == 0):
    print(v_year, ' - високосный')
else:
    print(v_year, ' - невисокосный')


# 4. Получить на ввод количество рублей и копеек и вывести в правильной форме, например,
# 3 рубля, 1 рубль 25 копеек, 3 копейки.

rub, coin = input('Введите рубли: '),input('Введите копейки: ')
rub_s, coin_s = '', ''
if (rub[-1] in ['0','5','6','7','8','9']) and ((int(rub) > 19) or (int(rub) < 11)):
    rub_s = 'рублей'
elif (int(rub) > 10) and (int(rub) < 20):
    rub_s = 'рублей'
elif rub[-1] == '1' and ((int(rub) > 19) or (int(rub) < 11)):
    rub_s = 'рубль'
elif (rub[-1] in ['2','3','4']) and ((int(rub) > 19) or (int(rub) < 11)):
    rub_s = 'рубля'

if (coin[-1] in ['0','5','6','7','8','9']) and ((int(coin) > 19) or (int(coin) < 11)):
    coin_s = 'копеек'
elif (int(coin) > 10) and (int(coin) < 20):
    coin_s = 'копеек'
elif coin[-1] == '1' and ((int(coin) > 19) or (int(coin) < 11)):
    coin_s = 'копейка'
elif (coin[-1] in ['2','3','4']) and ((int(coin) > 19) or (int(coin) < 11)):
    coin_s = 'копейки'

print(rub + ' ' + rub_s + ' ' + coin + ' ' + coin_s)

# ####************************************FOR*******************************************************###
# For
# 1. На вход подаётся целое число. Найти факториал до этого числа включительно.

numb = int(input('Введите число: '))
fact = 1
if numb == 0:
    fact = 1
else:
    for i in range(1,numb+1):
        fact *=  i
print(fact)

# 2. Ввести строку, состоящую из нескольких слов, разделенных пробелами.
# Нарезать строку в список по словам и вывести ее поэлементно – по одному слову в строке.

s = input('Введите строку, состоящую из нескольких слов, разделенных пробелами: ')
l = s.split(' ')
for el in l:
    print(el)

# 3. Получить сумму кубов первых n натуральных чисел.

n = int(input('Введите число: '))
sum_q = 0
for i in range(0,n+1):
        sum_q += i**3
print(sum_q)

# 4. Даны 2 списка: [1,2,3,4,5] и [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]. С помощью цикла for создайте на их основе словарь.

l1 = [1,2,3,4,5]
l2 = ['a', 'b', 'c', 'd', 'e']
d = dict()
for i in range(len(l1)):
    d[l2[i]] = l1[i]
print(d)


# 5. Дана строка – ‘abcdefghijklmnopqrstuvwxyz’. Необходимо вывести по 1 символу данной строки на экран,
# при условии, что выводятся только согласные буквы. Гласные пропускаются.

s = 'abcdefghijklmnopqrstuvwxyz'
for elem in s:
    if elem not in ['a','e','o','i','u']:
        print(elem)

# ####*********************************WHILE*******************************************************###
# While

# 1. Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введет слово «стоп».

sum_n = 0
while True:
    s = input('Введите хоть что-нибудь: ')
    if s.isdigit():
        sum_n +=  int(s)
    elif s == 'стоп':
        break
    else:
        break
print(sum_n)

# 2. Генерировать случайные числа от 0 до 10 до тех пор, пока не выпадет 0 или 10.
#  Выводить на каждой итерации получаемое число, сумму чисел с момента старта программы и количество итераций.
# (поможет random.randint())

from random import randint as r
count_i = 0
n_sum = 0
n = 1
while (n != 0) and (n != 10):
    n = r(0,10)
    print('Число: ',n)
    n_sum += n
    print('Сумма: ',n_sum)
    count_i += 1
    print('Итерация: ',count_i)

# 3. Создадим электронный замОк с тремя попытками ввода пароля.
# Если все 3 попытки были неудачными – выдаётся сообщение ‘замок заблокирован’.

count_i = 0
password = 'sdsdsd'
s = ''
while (count_i < 4) and (s != password):
    s = input('Введите пароль: ')
    count_i += 1

    if (s == password):
        print('Ok!')

    if count_i == 3:
        print('замок заблокирован')
        break

# 4. Дан список - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
# Написать программу, которая бы выдавала случайное значение из этого списка и выдавала сумму
# чисел каждую итерацию. Если сумма превысила 100, программа должна прерваться. Если попадаются
# значения, кратные 5, то они должны пропускаться. (поможет random.choice())

from random import choice as c
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum_n = 0
count_i = 0
while sum_n < 100:
    n = c(l)
    count_i += 1
    if n % 5 != 0:
        print('Число: ', n)
        sum_n += n
        print('Сумма: ',sum_n)