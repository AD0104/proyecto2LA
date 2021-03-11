class Node:
    def __init__(self, alphabets):
        self.alphabets= alphabets
        self.right = None
        self.left = None

    def setRight(self, newRight):
        self.right = newRight
    def setLeft(self, newLeft):
        self.left = newLeft
    def setValue(self, newValue):
        self.values = newValue
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def getAlphabets(self):
        return self.alphabets
"""
import string
#This will merge the lists
leaf = Node(list(string.ascii_lowercase)+list(string.ascii_uppercase)+[x for x in range(0,10)])
root = Node(["Cadena","Entero","Real"])
root.setLeft(leaf)
cadena = input()

#print("root:",root)
#print("left leaf:",root.getLeft())

def preOrden(nodo, cad):
 #   print(nodo)
    if nodo == root:
        if cad[0] in nodo.getAlphabets():
            print("Tipo:",cad[0])
            cad.pop(0)
        else:
            print("Tipo invalido:",cad[0])
            return

    else:
        for letter in cad[0]:
            print(letter)
            if letter not in nodo.getAlphabets():
                print(nodo.getAlphabets())
                print("Caracter invalido:",letter)
                return
    if nodo.getLeft():
        preOrden(nodo.getLeft(),cad)
    if nodo.getRight():
        preOrden(nodo.getRight(), cad)

if ';' in cadena:
    if cadena[-1] == ';':
        cadena = cadena[:-1]
        preOrden(root, cadena.split(" "))
    else:
        print("Error ';' debería estar al final")
"""
