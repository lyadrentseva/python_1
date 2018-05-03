class New:
    pass
x = New()
# print(x)

class Human:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def get_full_info(self):
        return '{},{}'.format(self.name, self.age)

m = Human('John', 35)
f = Human('Mila', 9)

# print(m.name)
# print(m.get_full_info())
# print(f.name)
# print(f.get_full_info())

class Squer():
    def __init__(self, a):
        self.a = a

    def get_sq(self):
        return self.a**2

    def __add__(self, other):
        return self.a**2 + other.a**2

    def __repr__(self):
        return 'square = {}'.format(self.a**2)

    def __str__(self):
        return 'd = {}'.format(self.a*2**0.5)

    def __eq__(self, other):
        if self.a**2 == other.a**2:
            return True
        else:
            return False



s1 = Squer(4)

# print(s1.get_sq())

x = Squer(8)
y = Squer(10)

x.diag = 27
y.perim = 8
# print(x.diag)
# print(y.perim)
# print(dir(x))

# print(x)
# print(str(x))
# print(x == y)

class Name:
    def __init__(self, f_n='Tome'):
        self.f_n = f_n

x = Name()
# print(x.f_n)
# f_n = 'Nnn'
# print(f_n)


class Glass:
    def __init__(self, curr_v=.5, max_v=200):
        self.curr_v = curr_v
        self.max_v = max_v

    def add_sth(self, add_sth):   # add sth
        if add_sth + self.curr_v <= self.max_v:
            return 'new_valume = {}'.format(self.curr_v + add_sth)
        else:
            return 'you can not do it(add)!'

    def sub_sth(self,sub_sth):   #sub  sth
        if self.curr_v - sub_sth >= 0:
            return 'new_valume = {}'.format(self.curr_v - sub_sth)
        else:
            return 'you can not do it(sub)!'

    def __add__(self, other):
        #add two glassed
        common_max_v = self.max_v + other.max_v
        common_curr_v = self.curr_v + other.curr_v
        return 'glasses is cool. common value and common fullnes = {};{}'.format(common_max_v, common_curr_v)

    def __sub__(self, other):
        common_diff_v = abs(self.curr_v - other.curr_v)
        return 'glasses difference is= {}'.format(common_diff_v)

    def __repr__(self):
        return 'glass is great.just take it. its valume = {}'.format(self.max_v)



gl = Glass()
gl2 = Glass(1,250)


print(gl)
print(gl2)
print(gl.add_sth(200))
print(gl.sub_sth(.3))
print(gl.__add__(gl2))
print(gl.__sub__(gl2))



class Figuer():

    d = {'bla-bla': }

    def __init__(self,type_f,a,b=0,c=0):
        self.type_f = type_f
        self.a = a
        self.b = b
        self.c = c

    def square(self):

        if self.type_f == 'tr':
            p = (self.a + self.b + self.c) / 2
            return (p * (p -self.a) * (p - self.b) * (p - self.c)) ** .5
        if self.type_f == 'r':
            return 3.14*self.a**2

        if self.type_f == 'sq':
            return self.a**2

        if self.type_f == 'nn':
            return self.a * self.b


r = Figuer('r', 2)
nn = Figuer('nn', 2, 3)
tr = Figuer('tr', 2, 5, 7)
sq = Figuer('sq', 5)

print(r.square())
print(nn.square())
print(tr.square())
print(sq.square())