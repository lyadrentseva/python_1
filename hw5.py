# 1.	Создайте класс, описывающий бытовой прибор на ваш выбор (телевизор, ноутбук, микроволновка).
# У него должно быть хотя бы 3 атрибута, описывающих его,
# а также хотя бы один метод, делающий что-либо (например, издаёт звук).
class Pc:
    def __init__(self, color, cpu, orm):
        self.color = color
        self.cpu = cpu
        self.orm = orm

    def show_text(self):
        return 'Hello, bro! take it easy! beep. beep'


pc = Pc('red', 2.4, 16)
print(pc.show_text())

# 2.	Создайте класс «стул», у которого бы были входными
# аргументами цвет и количество ножек. Определите для него методы «сложение
# (т.е. знак +)» и вычитание (т.е. знак -). Сложение и вычитание стульев определено
# по количеству ножек стула. Также определите метод, с помощью которого
# с функцией print() выводилась бы информация о цвете стула и количестве ножек. *Магия

class Chair:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def __add__(self, other):
        print("Chairs have " + str(self.legs + other.legs) + ' legs')

    def __sub__(self, other):
        print("Chairs have a difference in " + str(abs(self.legs - other.legs)) + ' legs')

    def __repr__(self):
        print('Chair has ' + self.color + ' color and ' + str(self.legs) + ' legs')


ch1 = Chair('red', 22)
ch2 = Chair('black', 88)
ch1.__add__(ch2)
ch1.__sub__(ch2)
ch1.__repr__()

# 3. Создайте класс объектов «Еда». От данного класса сделайте
# классы-наследники соответствующих продуктов. Атрибуты класса – параметры из столбцов таблицы,
# а также масса продукта. Должна быть реализована возможность сравнения объектов
# с помощью знаков >, <, ==.
# Сравнение проводится по общей калорийности объекта (т.е. калорий с учётом массы продукта).
# Должен быть реализован метод, с помощью которого с функцией print() выводилась бы информация
# о каждом из атрибутов объекта в одной строке. Также реализовать сложение(знак +) объектов и
# вычитание (знак –), результатом которого бы был кортеж из суммы(разности) каждого из атрибутов
# объектов (т.е. X + Y = (115, 16, 2, 5.1, 30)).

class Food:
    def __init__(self, massa,kkal,fat,prot,carbo,water):
        self.massa = massa
        self.kkal = kkal
        self.fat = fat
        self.prot = prot
        self.carbo = carbo
        self.water = water

    def __eq__(self, other):
        if (self.massa * self.kkal/100) == (other.massa * other.kkal/100):
            return "продукты с одинаковой колорийностью"
        elif (self.massa * self.kkal/100) > (other.massa * other.kkal/100):
            return "первый продукт более колорийный"
        elif (self.massa * self.kkal/100) < (other.massa * other.kkal/100):
            return "первый продукт более колорийный"

    def __add__(self, other):
        return tuple((self.massa + other.massa, self.kkal + other.kkal, self.fat + other.fat, self.prot + other.prot, self.carbo + other.carbo, self.water + other.water),)

    def __sub__(self, other):
        return tuple((self.massa - other.massa, self.kkal - other.kkal, self.fat - other.fat, self.prot - other.prot, self.carbo - other.carbo, self.water - other.water),)

    def __repr__(self):
        return "продукт массой {} содержит в 100гр: {} ккал , {} жира, {} белков, {} углеводов, {} воды  ".format(self.massa,self.kkal,self.fat,self.prot,self.carbo,self.water)


class Avocado(Food):
    pass

class Potato(Food):
    pass

class Carrot(Food):
    pass

class Olive(Food):
    pass

class Spinach(Food):
    pass

avocado = Avocado(1000, 300,0.1,10,25,200)
carrot = Carrot(1000, 300,0.1,10,25,100)
spinach = Spinach(1000, 300,0.1,10,25,100)
potato = Potato(1000, 300,0.1,10,25,100)
olive = Olive(2200, 500,0.1,15,45,300)
print(potato.__repr__())
print(potato.__add__(olive))
print(potato.__sub__(olive))
print(potato.__eq__(carrot))
print(potato.__eq__(olive))

# 4.	Создать класс, принимающий всего один атрибут – градус (угловой градус).
# Реализовать методы, которые бы высчитывали синус, косинус, тангенс, арктангенс
# от этой градусной меры. С помощью специального декоратора, превращающего метод
# в атрибут сделать так, чтобы синус, косинус, тангенс, арктангенс вызывались у
# объекта как атрибуты. *Модуль math в помощь.

class Angle:

    def __init__(self, demention):
        self.demention = demention
    @property
    def cos_c(self):
        from math import cos, pi
        print(cos(self.demention*pi/180))
    @property
    def sin_c(self):
        from math import sin, pi
        print(sin(self.demention*pi/180))
    @property
    def tan_c(self):
        from math import tan, pi
        print(tan(self.demention*pi/180))
    @property
    def atan_c(self):
        from math import atan, pi
        print(atan(self.demention*pi/180))


an = Angle(60)
an.cos_c
an.sin_c
an.tan_c
an.atan_c
print(an.demention)

# 5.	Создать класс, который бы хранил в себе недоступный для изменения пароль = ‘123’.
# Данный пароль нельзя изменить или посмотреть напрямую. Сделайте методы с помощью которых:
# - можно посмотреть пароль;
# - можно изменить пароль. При этом новый пароль проверяется на то, чтобы
# он состоял только из цифр и был строкой. Также данный метод должен помимо нового
# пароля принимать старый (как если бы вы в соцсетях меняли пароль, вас бы сначала
# попросили ввести старый для сверки). В случае несовпадения параметров(проверка на
# старый пароль и строковое значение+цифры нового) – выдаётся надпись об отказе в изменении
# пароля. В случае ввода правильных параметров – меняется пароль на новый и выдаётся надпись об
# успешной смене пароля. *Инкапсуляция в помощь.

class Passwd:
    def __init__(self):
        self.__pswd = '123'

    def show(self):
        return "current password is {}".format(self.__pswd)

    def change(self,psw_new, psw_old):
        if str(type(psw_new)) == "<class 'str'>" and psw_new.isdigit() and psw_old == self.__pswd:
            self.__pswd = psw_new
            print("You 've just changed your password successfully!")

        else:
            print('Access denied. There are bad new password or incorrect old one. Check please!')


pswd = Passwd()
print(pswd.show())
pswd.change('789', '123')


