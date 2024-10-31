#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe
"""lista recursiva con aspecto lisp y POO 
    ver goo: lisp introduccion listas
        cons, car, cdr ...
   RSA oct 2024
"""

class atom:
    
    _val = None
    
    def __init__(self, val = None) -> str:
        self._val = val

    def __str__(self) -> str:
        return str(self._val)

class cons:

    __car = None  #first object: lisp: NIL ~ ()
    __cdr = None  #remain objects: lisp: NIL ~ ()

    def __init__(self, o = None) -> None:
        if not isinstance(o, cons):
            self.__car = o

    def __str__(self) -> str:
        answ = "( "
 
        if not self.__car:
            answ += "()"
        else: 
            answ += str(self.__car)
 
        if not self.__cdr:
            answ += "()"
        else: 
            answ += str(self.__car)
 
        answ += ")"        

        return answ
        # if len(lista) == 0:
        #     print(")", end="")
        #     return
        # primero = lista[0]
        # listaRestantes = lista[1:]
        # print(primero, end=" ")
        # imprime(listaRestantes)
        # print(")", end="")    
 
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
    