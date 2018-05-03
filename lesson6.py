# # try:
# #     12/0
# # except:
# #     print("Ничего не получилось")
# # ####################################
# # try:
# #     12/0
# # except ZeroDivisionError:
# #     print("Ничего не получилось")
# # ####################################
# # try:
# #     12 + 0
# # except ZeroDivisionError:
# #     print("Ничего не получилось")
# # else:
# #     print('no zero')
# #
# # finally:
# #     print('что странное')
# # ###################################
# x = 12
# y = 0
# # try:
# #     if y == 0:
# #         raise Exception("деление на ноль")
# #     print(x/y)
# #
# # except Exception:
# #     print("error")
# #######################################
# # try:
# #     assert (y != 0), 'Errrooorr!!'
# #     print(x/y)
# #
# # except EnvironmentError:
# #     print("rrrr")
# #######################################
# # numb1 = 3
# # numb2 = 0
# # try:
# #     numb1 = 3
# #     numb2 = 0
# #     assert numb1 == numb2, 'The number1 is not eq of number2'
# #     print("the result", numb1 + numb2)
# #
# # except ValueError:
# #     print("type thm wrong")
# # except Exception as e:
# #     print(e)
# #
# # print('final')
# #########################################################
#
# # f = open('pytest/text.txt', 'r')
# # #f.read()
# # print(f.read())
# # f.close()
# ########################################################
# # import hashlib
# # x = hashlib.sha256()
# # # x.update(b'helloo!')
# # x.update(bytes('helloo!', encoding='utf-8'))
# # print(x.hexdigest())
# #######################################################
# # import time
# # # time.time()
# # # print(time.time())
# ######################################################
# # def f(*args):
# #
# #     t1 = time.time()
# #     for e in args:
# #         print(e**2)
# #     t2 = time.time()
# #
# #     print(t2 - t1)
#
# # f(2,3,4,5,5)
# #####################################################
#
# import string
# import time
# import hashlib
# def f(path):
#     t1 = time.time()
#     alph = string.ascii_letters + string.digits
#     # digit = string.digits
#     f = open(path, 'r')
#     s_check = f.read()
#     f.close()
#     for i in range(len(alph)):
#         for j in range(i,len(alph)):
#             s = alph[i] + alph[j]
#             s_new = hashlib.sha256()
#             s_new.update(bytes(s, encoding='utf-8'))
#             s2 = s_new.hexdigest()
#             if s_check == s2:
#                 print(s)
#                 break
#     t2 = time.time()
#     f1 = open('test1.txt', 'a')
#     f1.write(str(t2 - t1)+'\r')
#     f1.close()
#     print(t2 - t1)
#
# # f('codefile_1.txt')
# # f('codefile_2.txt')
# # f('/home/red/PycharmProjects/python_belhard/codefile_1.txt')
#
# import random
# def f2(path):
#     t1 = time.time()
#     alph = string.ascii_letters + string.digits
#
#     f = open(path, 'r')
#     s_check = f.read()
#     f.close()
#     s2 = ''
#     s = ''
#     while s_check != s2:
#         s = random.choice(alph) + random.choice(alph)
#         s_new = hashlib.sha256()
#         s_new.update(bytes(s, encoding='utf-8'))
#         s2 = s_new.hexdigest()
#     print(s)
#     t2 = time.time()
#     f1 = open('test2.txt', 'a')
#     f1.write(str(t2 - t1)+'\r')
#     f1.close()
#     print(t2 - t1)
#
# # f2('codefile_1.txt')


def f3(path):
    t1 = time.time()
    alph = string.ascii_letters + string.digits

    f = open(path, 'r')
    s_check = f.read()
    f.close()
    s2 = ''
    s = ''
    while s_check != s2:
        s = random.choice(alph) + random.choice(alph) + random.choice(alph) + random.choice(alph)
        s_new = hashlib.sha256()
        s_new.update(bytes(s, encoding='utf-8'))
        s2 = s_new.hexdigest()
    print(s)
    t2 = time.time()
    f1 = open('test2.txt', 'a')
    f1.write(str(t2 - t1)+'\r')
    f1.close()
    print(t2 - t1)

f3('codefile_3.txt)
