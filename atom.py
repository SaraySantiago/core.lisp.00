#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe
"""atomos para un core del leng.
    ver goo: lisp introduccion listas
        cons, car, cdr ...
   RSA oct 2024
"""
from cons import cons 

class atom:
    
    _val = None
    
    def __init__(self, val = None) -> str:
        self._val = val

    def __str__(self) -> str:
        return str(self._val)

if __name__ == "__main__":

    a0 = atom()    
    print(a0)
    
    a1 = atom(2)    
    print(a1)
    
    a2 = atom("22")    
    print(a2)
    
    a3 = atom(["ajo", 33])    
    print(a3)

    c = cons()
    print(c)
    