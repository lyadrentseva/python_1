# ***************************************    ДЗ №1   *****************************************

# 1. Создайте переменную со строчным значением ‘12345’, преобразуйте переменную в другие типы:
# - целое число;
# - вещественное число;
# - логическое значение;
# - список;
# - кортеж;
# - множество;
# - словарь (используйте метод словаря fromkeys())

s = '12345'                     # создали переменную со строчным значением

s_new = int(s)                  # - преобразовали в целое число;
s_new = float(s)                # - вещественное число;
s_new = bool(s)                 # - логическое значение;
s_new = list(s)                 # - список;
s_new = tuple(s)                # - кортеж;
s_new = set(s)                  # - множество;
s_new = dict().fromkeys(s)      # - словарь


# 2. Дана произвольная строка.
# Разрежьте ее на две равные части (если длина строки — четная,
# а если длина строки нечетная, то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите с помощью функции print().
# При решении нельзя использовать конструкцию if,
# примените срезы, целочисленное деление и функцию длины строки.

s = 'The real war does not resemble the legendary war in its process'    # произвольная строка
part2 = len(s) // 2                # вторая часть строки, для нечетного количества символов - это меньшая часть
s_new = s[part2:] + s[:part2]      # поменяли местами части строк, новая строка
print(s_new)


# 3. Дан текст – “The real war does not resemble the legendary war in its process
#  or its conclusion. If it had inspired or directed the development of the legend,
# then certainly the Ring would have been seized and used against Sauron; he would not
# have been annihilated but enslaved, and Barad-dûr would not have been destroyed but
#  occupied. Saruman, failing to get possession of the Ring, would in the confusion
# and treacheries of the time have found in Mordor the missing links in his own researches
# into Ring-lore, and before long he would have made a Great Ring of his own with which to
#  challenge the self-styled Ruler of Middle-earth. In that conflict both sides would have
# held hobbits in hatred and contempt: they would not long have survived even as slaves.”
# посчитайте и выведите количество букв (‘a’) в тексте (независимо от регистра)(смотрите методы строк);
# посчитайте количество слов в тексте (вспомните, каким методом можно превратить строку в список);
# создайте на основе данной строки новую, в которой все строчные буквы (‘a’)
# будут заменены символом ‘@’ (смотрите методы строк);

s = 'The real war does not resemble the legendary war in its process or its conclusion. \
If it had inspired or directed the development of the legend, then certainly the Ring would \
have been seized and used against Sauron; he would not have been annihilated but enslaved, \
and Barad-dûr would not have been destroyed but occupied. Saruman, failing to get possession \
of the Ring, would in the confusion and treacheries of the time have found in Mordor the missing \
links in his own researches into Ring-lore, and before long he would have made a Great Ring of \
his own with which to challenge the self-styled Ruler of Middle-earth. \
In that conflict both sides would have held hobbits in hatred and contempt: they would not \
long have survived even as slaves.'

print(s.lower().count('a'))              # подсчет количествa букв (‘a’);
print(len(s.split(' ')))                 # посчитайте количество слов в тексте
s_new = s.replace('a', '@')              # новая строка, все строчные буквы (‘a’) заменены символом ‘@’


# 4. Дан список – [2, 1, 4, 3, 5, 6, 7, 10, 8, 9].
# отсортируйте список по возрастанию значений (смотрите методы списка);
# отсортируйте список по убыванию значений (reverse=True);
# выведите с помощью функции print() элементы списка [2, 1, 4, 3, 5, 6, 7, 10, 8, 9]
# с чётными индексами(вспомните срез и шаг среза);
# разверните список в обратную сторону с помощью шага среза;
# найдите максимальное значение в списке (поищите нужную встроенную функцию);
# найдите минимальное значение в списке;
# удалить все элементы списка, индекс которых кратен 3.


l = [2, 1, 4, 3, 5, 6, 7, 10, 8, 9]         # список
l.sort(reverse=False)                       # список отсортирован по возрастанию значений
l.sort(reverse=True)                        # список отсортирован по убыванию значений

l = [2, 1, 4, 3, 5, 6, 7, 10, 8, 9]         # список несортированный
print(l[::2])                               # элементы списка с чётными индексами

l = [2, 1, 4, 3, 5, 6, 7, 10, 8, 9]
l_new = l[::-1]                             # разверните список в обратную сторону с помощью шага среза
print(l_new)

el_max = max(l)                             # максимальное значение в списке ;
el_min = min(l)                             # минимальное значение в списке;

l = [2, 1, 4, 3, 5, 6, 7, 10, 8, 9]         # список несортированный
del l[::3]                                  # удалить все элементы, индекс которых кратен 3.


# 5. Дан список - [5,4,3,2,1,2,3,4,5,1,1,11,35,4,3,5,7,8,10,15,2,99].
# - посчитайте, сколько в данном списке уникальных значений (примените множество, задача в одну строчку);
# - получите из данного списка множество, затем найдите элементы, которые будут
# общими у него и у множества {4,3,5,1,2} (смотрите методы множеств);

l_2 = [5,4,3,2,1,2,3,4,5,1,1,11,35,4,3,5,7,8,10,15,2,99]  # список
print(len(set(l_2)))                         #сколько в данном списке уникальных значений

set_test = set(l_2)
set_compare = {4,3,5,1,2}
print(set_test.intersection(set_compare))    #элементы, общие у set_test и у множества set_compare


# 6. Дан словарь - {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}.
# - выведите списком все ключи данного словаря (смотрите методы словарей, а также вспомните строенную функцию list());
# - выведите списком все значения данного словаря;
# - добавьте значения {‘f’ : 6, ‘g’: 7, ‘h’ : 8} в словарь с помощью метода update

d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
print(list(d.keys()))                                   # все ключи данного словаря списком
print(list(d.values()))                                 # все значения данного словаря списком
d.update({'f' : 6, 'g': 7, 'h' : 8})                    # добавьте значения {‘f’ : 6, ‘g’: 7, ‘h’ : 8} в словарь update
