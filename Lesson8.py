class Divider:
    def __init__(self):
        self.div = 1

    def devide(self, value):
        return value / self.div


d = Divider()
# print(d.devide(5))
d.div = 0


# print(d.devide(3))

class Divider:
    def __init__(self):
        self.__div = 1

    def devide(self, value):
        return value / self.__div

    def setDivide(self, numb):
        if numb != 0:
            self.__div = numb
        else:
            return 'nizya'


d = Divider()
d.setDivide(0)
d.setDivide(10)


# print(d.setDivide(10))
# print(d.devide(3))

class Human:
    def __init__(self, f_name, s_name):
        self.f_name = f_name
        self.s_name = s_name

    # @property
    def get_full_name(self):
        print("fuuul: {},{}".format(self.f_name, self.s_name))

    @staticmethod
    def meth(value):
        return 'hello ' + str(value)


x = Human("SSS", "uytiuy")


# print(x.get_full_name())
# print(x.get_full_name)


class Mother():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_param(self):
        return 'dfds {},{}'.format(self.name, self.age)


# m = Mother('Anns', 34)
# print(m.get_param())


class Son(Mother):
    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice

        # OR
        # self.name = name
        # self.age = age
        # self.voice = voice

        # OR
        # Mother.__init__(self,name,age)
        # self.voice = voice


# s = Son('HH', 12, 'lll')
# print(s.get_param())



class Metal:
    def __init__(self,massa,value):
        self.massa = massa
        self.value = value
        self.ro = None
        self.numb = None
        self.v = None

    def __repr__(self,ro):
        if self.ro != 0:
            return "fullness is: " + str(((self.massa / self.ro) / self.value) * 100) + '%; numb of table is: ' + str(self.numb)
        else:
            return 'massa Me is:' + str(self.massa) + 'value is: ' + str(self.value)

    def devis(self, ro):
        if self.ro != 0:
            return "fullness is: " + str(((self.massa / self.ro) / self.value) * 100)
        else:
            return 'massa Me is:' + str(self.massa)

    def __eq__(self, other):
        if self.v != 0:
            if (self.massa*self.v**2)/2 > (other.massa*other.v**2)/2:
                return 'the first object is faster =)'
            elif (self.massa*self.v**2)/2 < (other.massa*other.v**2)/2:
                return 'the second object is faster =)'
            elif  (self.massa*self.v**2)/2 == (other.massa*other.v**2)/2:
                return 'ooops! they are equal!!'
        else:
            return "nothing is to compare"

# > , < , =
class Al(Metal):
    def __init__(self,massa,value,ro,numb,v):
        super().__init__(massa,value)
        self.numb = numb
        self.ro =ro
        self.v = v

    # def __repr__(self):
    #     return "fullness is: " + str( ((self.massa/self.ro)/self.value)*100)   + '%; numb of table is: ' + str(self.numb)
#26
class Fe(Metal):
    def __init__(self,massa,value,ro,numb,v):
        super().__init__(massa,value)
        self.numb = numb
        self.ro =ro
        self.v = v

    # def __repr__(self):
    #     return "fullness is: " + str( ((self.massa/self.ro)/self.value)*100)   + '%; numb of table is: ' + str(self.numb)


class Hg(Metal):
    def __init__(self,massa,value,ro,numb,v):
        super().__init__(massa,value)
        self.numb = numb
        self.ro =ro
        self.v = v

    # def __repr__(self):
    #     return "fullness is: " + str( ((self.massa/self.ro)/self.value)*100)   + '%; numb of table is: ' + str(self.numb)

class Ti(Metal):
    def __init__(self,massa,value,ro,numb,v):
        super().__init__(massa,value)
        self.numb = numb
        self.ro =ro
        self.v = v

    # def __repr__(self):
    #     return "fullness is: " + str( ((self.massa/self.ro)/self.value)*100)   + '%; numb of table is: ' + str(self.numb)

class Ca(Metal):
    def __init__(self,massa,value,ro,numb,v):
        super().__init__(massa,value)
        self.numb = numb
        self.ro =ro
        self.v = v

    # def __repr__(self):
    #     return "fullness is: " + str( round(((self.massa/self.ro)/self.value)*100,5))   + '%; numb of table is: ' + str(self.numb)

# al = Al(5, 2000,2700,13)
# print(al.__repr__())
# fe = Fe(5,200,7870,26)
# print(fe.__repr__())
# hg = Hg(6,200,13540,80)
# print(hg.__repr__())
# ti = Ti(6000,2000,4520,22)
# print(ti.__repr__())
# ca = Ca(7000,2000,1550,20)
# print(ca.__repr__())

al = Al(5, 2000,2700,13,5)
fe = Fe(5,200,7870,26,10)
print(al.__eq__(fe))
