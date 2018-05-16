# auto run script #email.py#

import os,sys,subprocess

path = "/home/red/PycharmProjects/python_belhard/email.py"

def open_f(p):
    if sys.platform == 'win32':
        os.startfile('email')
    else:
        opener = "execute" if sys.platform == 'darwin' else "xdg-open"
        subprocess.call([opener, p])
open_f(path)