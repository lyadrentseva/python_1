x = 1
def f1 (x):
    global y
    y = -x


# print(f1(5))
# print(y)

a = 0
def f2():
    a = 10
    print(a)

# f2()
# print(a)


a = 0
def f3():
    global a
    a = 10
    print(a)

# f3()
# print(a)


def fr1(x):
    if x == 1:
        return 1
    else:
        print(x)
        return x*fr1(x-1)
#print(fr1(10))


def fr2(x):
    if x < 10:
        print(x)
    else:
        print(x%10)
        x = x // 10
        fr2(x)

#fr2(12345)

def fr3(x):

    if len(x) == 1:
        print(x)
    else:
        print(x[0])
        x = x[1:]
        fr3(x)

# fr3('asddf')


def fr4(a,b):
    if b == 1:
        return a
    else:
        return a * fr4(a, b-1)

# print(fr4(2.2,9))


def fr5(x):
    from random import randrange as r
    xr = r(0,101,1)
    if x == xr:
        return xr
    else:
        print(xr)
        return xr + fr5(x)

#print(fr5(100))


def dnk(x):
    d = {'A':'T','G' : 'C','T' : 'A', 'C': 'G'}
    if len(x) != 0:
        x_new = ''
        for i in x:
            x_new += d.get(i)
        return ''.join(d.get(i))

# print(dnk('AGT'))

# l34 = lambda x : x*2, {'A':'T','G' : 'C','T' : 'A', 'C': 'G'}

''.join(filter(lambda x: x not in ['a','e','u','i','o'], 'adefwiupppp'))

tr = list(filter(lambda x: x**3 % 3 == 0, [2,3,6,8,9,10]))

#print(tr)

# def dec(fun):
#     def wrapper(x):
#         return list(str(fun(x)))
#     return wrapper
#
# @dec
# def n(a):
#     return a**2
#
# print(n(15))

def dec(fun):
    def wrapper(x):
        return fun(x)*2
    return wrapper

@dec
def n(a):
    return a**2
@dec
def k(i):
    return i+1



print(n(15))
print(k(15))