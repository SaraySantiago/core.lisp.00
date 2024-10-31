#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe
"""cons para core de lenguaje lisp 
    ver goo: lisp introduccion listas
        cons, car, cdr ...
   RSA oct 2024
"""
from atom import atom 
class cons:

    __car = None  #first object: lisp: NIL ~ ()
    __cdr = None  #remain objects: lisp: NIL ~ ()

    def __init__(self, o = None) -> None:
        if not isinstance(o, cons):
            self.__car = o

    def __str__(self) -> str:
        answ = "("
 
        if not self.__car:
            answ += "NIL"
        else: 
            answ += str(self.__car)
            
        answ += " "
 
        if not self.__cdr:
            answ += "NIL"
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
    a1 = atom(2)
    a2 = atom([2])    
    
    c0 = cons()
    print(c0)            
    
    c1 = cons (22)
    print(c1)
    c2 = cons (a1)
    print(c2)
    c3 = cons (a2)
    print(c3)