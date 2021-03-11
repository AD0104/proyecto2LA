from node import Node
import string
class Tree:
    def __init__(self):
        self.root = Node(["Cadena","Entero","Real"])
        self.leaf = Node(list(string.ascii_lowercase)+list(string.ascii_uppercase)+[str(x) for x in range(10)])

        self.root.setLeft(self.leaf)
        
        self.errorsRaised = [0,0,0,0,0]
        self.errors = ["Error 1: Cadena vacia","Eror 2: Tipo de dato invalido","Error 3: Variable no declarada","Error 4: Los nombres de variables no deben contener espacios","Error 5: Cadena con caracteres invalidos"]
    def getRoot(self):
        return self.root

    def printMessages(self):
        if 1 in self.errorsRaised:
            for index, value in enumerate(self.errorsRaised):
                if value == 1:
                    print(self.errors[index])
        else:
            print("Cadena correcta")

    def verificacion(self, actualNode, values):
        if actualNode == self.getRoot():
            if values:
                if values[0] not in actualNode.getAlphabets():
                    self.errorsRaised[1] = 1
                    values.pop(0)
                else:
                    values.pop(0)
            else:
                self.errorsRaised[0] = 1
                return
        else:
            if values:
                for idx,letter in enumerate(values[0]):
                    if letter not in actualNode.getAlphabets():
                        print("Caracter invalido",letter)
                        self.errorsRaised[4] = 1
                    else:
                        string = values[0]
                        string = string[idx+1:]
                        values[0] = string
                        if values[0] == '':
                            values.pop(0)
                            break
                if len(values) > 0:
                    self.errorsRaised[3] = 1
            else:
                self.errorsRaised[2] = 1
        if actualNode.getLeft():
            self.verificacion(actualNode.getLeft(), values)
        if actualNode.getRight():
            self.verificacion(actualNode.getRight(), values)
