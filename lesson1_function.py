def p(*args):
    d = dict()
    if len(args) < 2:
        d['hi'] = '=)'
    else:
        if len(args) % 2 == 0:
            ak = args[1::2]
            av = args[::2]
            for i in range(len(ak)):
                d[ak[i]] = av[i]
        else:
            ak = args[1:-1:2]
            av = args[::2]
            for i in range(len(ak)):
                d[ak[i]] = av[i]
            d[args[-1]] = None
    return d

#print(p(1,2,3,4,6))
#print(p(1,2,3,4))
#print(p(1))

def cake ( n = .5 ):

    n *= 1.25
    d = dict()
    d['cake'] = str(n) + ' kg'
    d['muka'] = str(n*.6) + ' kg'
    d['moloko'] = str(n *.15)  + ' kg'
    d['egg'] = str(n*.1) + ' kg'
    d['suger'] = str(n*.08)  + ' kg'
    d['salt'] = str(n*.01)  + ' kg'
    d['dr'] = str(n*.055)  + ' kg'
    d['vanil'] = str(n*.005) + ' kg'


    for i,j in d.items():
        print(i,j)

    #return d
#print(cake(.6))


def func_ye(*args):
    for el in args:
        yield el*2

#print(list(func_ye('abc')))



def  f(*args):
    for el in args:
        yield str(el) + ' hello'

print(list(f('abc',23, '%%$')))
