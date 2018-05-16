# 1.	Написать функцию, которая бы принимала один аргумент – путь к папке.
# В данной папке должна создаваться БД с двумя таблицами:
# - Customers (содержит поля: идентификатор, имя, фамилия, возраст, дата регистрации, первичный_пароль);
# - Contacts (содержит поля: идентификатор, email, телефон).
# В каждой из таблиц должна создаваться тестовая строка,
# причём первичный пароль должен автоматически генерироваться из 8 символов(буквы+цифры).


import sqlite3
from string import ascii_letters, digits
from random import choice

def cr_db(path):

    s_passw = ascii_letters + digits                #(буквы+цифры)
    passw_random = ''.join([choice(s_passw) for i in range(8)]) #рандомный пароль из 8 символов

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE Customers(id integer, first_name text, last_name text, age integer, reg_date text, passw text)")
    cursor.execute("""INSERT INTO Customers VALUES('{}','{}','{}','{}','{}','{}')""".format(1, 'name', 'lname','age','date', passw_random))

    cursor.execute("CREATE TABLE Contacts (id integer, mail text, phone text)")
    cursor.execute("""INSERT INTO Contacts VALUES('{}', '{}', '{}')""".format(1, 'mail@mail.com', 'phone'))

    conn.commit()
    conn.close()


path = r"/home/red/PycharmProjects/python_belhard/db1"
# cr_db(path)
#
# conn = sqlite3.connect(path)
# cursor = conn.cursor()
# print(cursor.execute("SELECT * FROM Customers").fetchall())
# print(cursor.execute("SELECT * FROM Contacts").fetchall())
# conn.close()

########################################################################################################################
# 2.
# 2.1) Написать функцию, которая бы принимала четыре аргумента: путь к папке, имя, фамилия, пароль.
# Должна создаваться БД по указанному пути с таблицей “Пользователи”. Если таблица уже существует,
#то просто должна вставляться в эту таблицу строка с указанными параметрами. В таблице должны быть поля: имя,
#фамилия, пароль (шифруется в 16-чное значение по алгоритму sha256 *для MacOS – по любому работающему*),
# дата регистрации (автоматически вставляется в формате день.месяц.год_часы:минуты:секунды).

from hashlib import sha256
from _datetime import datetime
from time import strftime

def cr_db2 (path,name,last_name,passwd):

    datecr_tuple = datetime.timetuple(datetime.today())
    datecr = strftime('%d.%m.%Y_%X', datecr_tuple)     #получаю дату в нужном форматке

    passwd_sha256 = sha256(bytes(passwd, encoding='utf-8')).hexdigest()  # шифрую пароль
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    id = 0
    try:
        id = (cursor.execute("SELECT max(id) FROM Users").fetchall()[0])[0] + 1
    except:
        id = 1

    try:
        cursor.execute("CREATE TABLE Users(id integer, first_name text, last_name text,datecr text, passw text)")
        cursor.execute("""INSERT INTO Users VALUES('{}','{}','{}','{}','{}')""".format(id, name, last_name, datecr, passwd_sha256))
    except sqlite3.OperationalError:
        cursor.execute("""INSERT INTO Users VALUES('{}','{}','{}','{}','{}')""".format(id, name, last_name, datecr, passwd_sha256))


    conn.commit()
    conn.close()


path = r"/home/red/PycharmProjects/python_belhard/db2"
# cr_db2(path,'Jack','Jonth','457890iT')
#
# conn = sqlite3.connect(path)
# cursor = conn.cursor()
# print(cursor.execute("SELECT * FROM Users").fetchall())
# conn.close()


########################################################################################################################
# 2.2) Написать функцию, обновляющую значение ячейки в таблице БД.
# Принимает как аргументы: путь к созданной БД,
# имя таблицы, выражение с условием для поиска обновляемых ячеек,
# имя столбца(в который будет вставляться новое знаечние),
# само новое значение ячейки.

def cr_db3 (path, table_name, conditions, coloumn_name, meaning):

    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute\
            ("UPDATE {t1} SET {c1}='{m1}' WHERE {c2}".format(t1=table_name, c1=coloumn_name, m1=meaning, c2=conditions))
        conn.commit()
        conn.close()

    except :
        print('table Users is not existed!')


path = r"/home/red/PycharmProjects/python_belhard/db2"
# cr_db3(path, 'Users', 'id = 1', 'first_name', 'Dima')
#
# conn = sqlite3.connect(path)
# cursor = conn.cursor()
# print(cursor.execute("SELECT * FROM Users").fetchall())
# conn.close()

########################################################################################################################
# 3.
# 3.1)Написать функцию, которая бы принимала аргументы: путь к папке, массу в кг.
# В папке по укзанному пути должна создаваться БД с таблицей. В таблицу должно заноситься
# значение массы в кг, а также эта маса, конвертированная в:
# -	Фунты
# -	Стоуны
# -	Драхмы
# -	Пуды
# -	Хандредвейты
# Если таблица с укзанным именем существует в БД, то просто должна вставляться в эту
# таблицу строка с указанными параметрами.
# Занести в данную таблицу не менее 10-ти значений.

def cr_db4(path, m_kg):

    # конвертируем в разные метрические единицы
    m_kg_str = str(m_kg)
    m1 = str(2.2 * m_kg)           # -	Фунты - lb
    m2 = str(0.157 * m_kg)         # -	Стоуны - st
    m3 = str(564.382* m_kg)        # -	Драхмы - dh
    m4 = str(1/16 * m_kg)          # -	Пуды -pud
    m5 = str(0.01968 * m_kg)       # -	Хандредвейты - cwt

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    id = 0
    try:
        id = (cursor.execute("SELECT max(id) FROM Weights").fetchall()[0])[0] + 1
    except:
        id = 1

    try:
        cursor.execute("CREATE TABLE Weights(id integer, m_kg text, lb text,st text,dh text, pud text, cwt text)")
        cursor.execute("INSERT INTO Weights VALUES({},'{}','{}','{}','{}','{}','{}')".format(id, m_kg_str, m1, m2, m3, m4, m5))
    except sqlite3.OperationalError:
        cursor.execute("INSERT INTO Weights VALUES({},'{}','{}','{}','{}','{}','{}')".format(id, m_kg_str, m1, m2, m3, m4, m5))

    conn.commit()
    conn.close()

path = r"/home/red/PycharmProjects/python_belhard/db4"
# cr_db4(path, 10011)
#
# conn = sqlite3.connect(path)
# cursor = conn.cursor()
# print(cursor.execute("SELECT * FROM Weights").fetchall())
# conn.close()

########################################################################################################################

# 3.2) Написать функцию, которая бы принимала аргументы: полный путь к БД, название таблицы, путь к папке.
# Функция должна прочитать в БД таблицу с массами и на её основе сформировать таблицу Excel в формате .xls
# по пути к папке(аргумент 3).
# При невозможности использовать библиотеку xlwt (может проблема возникнуть у пользователей MacOs) –
# функция должна будет сформировать и вернуть словарь, где ключ – значение массы в кг + слово «кг»,
# а значение – список из масс в других единицах + их названия.
# {’10 кг’: [’22.05 фунта’,’1.57 стоуна’… и т.д.]}

import xlwt
def cr_db5(path_db, table_name, path_xls):

    try:
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        curselect = (cursor.execute("""SELECT * FROM '{}'""".format(table_name))).fetchall()
        conn.commit()
        conn.close()

    except:
        print('Samething is wrong!')

    if curselect:
        book = xlwt.Workbook('utf-8')
        font = xlwt.easyxf('font: height 240,name Times New Roman,colour_index black, bold 1,\
            italic off; align: wrap on, vert center, horiz center; border: top thin, right thin, bottom thin, left thin;\
            pattern: pattern solid, fore_colour white;')
        sheet = book.add_sheet('New_sheet')

        for i in range(len(curselect)):
            for j in range(len(curselect[i])):
                sheet.col(j).width = 8250
                sheet.write(i, j, curselect[i][j], font)

        sheet.portrait = False
        book.save(path_xls + table_name + '.xls')


path_db = r"/home/red/PycharmProjects/python_belhard/db4"
path_xls = r"/home/red/PycharmProjects/python_belhard/ "
cr_db5(path_db, 'Weights', path_xls)

########################################################################################################################
# 4.	Регулярные выражения.
# Написать функцию, которая бы принимала один аргумент: строку.
# Функция должна посчитать с помощью регулярных выражений:
# - количество пробельных символов;
# - количество слов, начинающихся и заканчивающихся только на гласные буквы;
# - количество переносов строки;
# - количество слов, состоящих только из цифр.
# Возвращать значение красивым словарём.
# Использовать регулярные выражения.
# Можете тестить на английской статье в википедии о Минске
# (предварительно скопированной в файл) https://en.wikipedia.org/wiki/Minsk

import re
def f_reg(s):
    d = {'количество пробельных символов': 0,
         'количество слов начинающихся и заканчивающихся только на гласные буквы': 0,
         'количество переносов строки': 0,
         'количество слов, состоящих только из цифр': 0}
    count_space = len(re.findall('[ ]+', s))           # - количество пробельных символов;
    count_cons = len(re.findall(r'\b[aeiouAEIOU]\w+[aeiouAEIOU]\b', s))  # - количество слов, начинающихся и заканчивающихся только на гласные буквы;
    count_newstr = len(re.findall('[\n]',s))           # - количество переносов строки;
    count_numb = len(re.findall('\d+', s))             # - количество слов, состоящих только из цифр.

    d['количество пробельных символов'] = count_space
    d['количество слов начинающихся и заканчивающихся только на гласные буквы'] = count_cons
    d['количество переносов строки'] = count_newstr
    d['количество слов, состоящих только из цифр'] = count_numb

    for i in d:
        print(i +': ' + str(d.get(i)))


path_to_read = r"/home/red/PycharmProjects/python_belhard/Minsk - Wikipedia.html"

s = ''
with open(path_to_read, 'r', encoding='utf-8') as g:
    for line in g:
        s += line

# f_reg(s)

########################################################################################################################

# 5.
# 5.1) Напишите функцию, которая бы создавала БД с таблицей «Телефонная_книга».
# В таблице должны быть поля: имя, фамилия, телефон, год рождения.
def cr_db6(path = r"/home/red/PycharmProjects/python_belhard/db6"):

    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Phone_book(id integer, first_name text, last_name text, phone text, year_bith integer)")
    conn.commit()
    conn.close()


path = r"/home/red/PycharmProjects/python_belhard/db6"
# cr_db6(path)

# conn = sqlite3.connect(path)
# cursor = conn.cursor()
# print(cursor.execute("SELECT * FROM Phone_book").fetchall())
# conn.close()

########################################################################################################################
# 5.2) Напишите функцию, которая бы просила пользователя последовательно ввести:
# - имя
# - фамилию
# - возраст
# - номер телефона.
# Номер телефона соответствует Республике Беларусь и может быть введён в одном из следующих форматов:
# - +375297776655
# - 8(029)7776655
# - (029)7776655
# - 7776655
# - 777-66-55
# - 297776655
# Введённые данные должны быть занесены данной функцией в таблицу в созданной БД с условиями:
# 1)	Имя и фамилия должны состоять только из букв и знака апострофа
# 2)	Год рождения должен высчитываться автоматически с помощью модуля time или datetime, исходя из возраста товарища.
# 3)	Номер телефона должен быть записан в БД в виде: +375-код_с_нулём-телефон_в_формате_3_2_2 (+375-29-777-66-55)
# Конечно же, использовать регулярные выражения.

# from _datetime import datetime   # already imported
# from time import strftime

def ins_db6 (path = r"/home/red/PycharmProjects/python_belhard/db6"):

    f_name = ''
    s_name = ""
    age = 0
    phone_str = ''

    while True:
        f_name = input("Введите имя: ")
        if len(re.findall('[A-z\']+', f_name)) != 0:
            f_name = f_name
            break
        else:
            print('недопустимые символы для имени')
            f_name = ''

    while True:
        s_name = input("Введите имя: ")
        if len(re.findall('[A-z\']+', s_name)) != 0:
            s_name = s_name
            break
        else:
            print('недопустимые символы для фамилии')
            s_name = ''

    age = input("Введите возраст: ")

    datecr_tuple = datetime.timetuple(datetime.today())
    datecr = strftime('%Y', datecr_tuple)
    year_birth = int(datecr) - age

    while True:

        phone_numb = input("Введите номер телефона: ")

        phone_numb = phone_numb.replace('-', '')
        phone_numb = phone_numb.replace('(', '')
        phone_numb = phone_numb.replace(')', '')

        if re.match(r'[+375]|[8029]|[029]|[]|[29][0-9]{7}', phone_numb) and len(phone_numb) > 6:
            phone_numb = phone_numb
            break
        else:
            print('некорректный номер телефона')


    if len(phone_numb) > 0:
        phone_str = '+37529' + phone_numb[-7:]
    else:
        phone_str = ''


    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    id = 0
    try:
        id = (cursor.execute("SELECT max(id) FROM Phone_book").fetchall()[0])[0] + 1
    except:
        id = 1

    cursor.execute("""INSERT INTO Phone_book VALUES({},"{}","{}",'{}',{})""".format(id, f_name, s_name, phone_str ,year_birth))
    conn.commit()
    conn.close()


path = r"/home/red/PycharmProjects/python_belhard/db6"
# ins_db6(path)
#
# conn = sqlite3.connect(path)
# cursor = conn.cursor()
# print(cursor.execute("SELECT * FROM Phone_book").fetchall())
# conn.close()