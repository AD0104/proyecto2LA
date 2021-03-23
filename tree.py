from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.leaf = None

        self.errorsRaised = [0,0,0,0,0,0,0,0]
        #                    0 1 2 3 4 5 6 7
        self.errors = ["Error 1: Cadena vacia", #0
                       "Eror 2: Tipo de dato invalido", #1
                       "Error 3: Variable no declarada", #2
                       "Error 4: Los nombres de variables no deben contener espacios", #3
                       "Error 5: Cadena con caracteres invalidos", #4
                       "Error 6: Asignacion invalida", #5
                       "Error 7: Operador invalido", #6
                       "Error 8: Operando incompatible" #7
                       ]
        self.dataType = ""
        self.statedVar = ""
    def setRoot(self, root):
        self.root = root
    def getRoot(self):
        return self.root
    def getDataType(self):
        return self.dataType
    def getStatedVar(self):
        return self.statedVar

    def printMessages(self):
        if 1 in self.errorsRaised:
            for index, value in enumerate(self.errorsRaised):
                if value == 1:
                    print(self.errors[index])
        else:
            print("Cadena correcta")
    #Recorrido en preorden
    def varVerificacion(self, actualNode, values):
        if actualNode == self.getRoot():
            if values:
                if values[0] not in actualNode.getAlphabets():
                    self.errorsRaised[1] = 1
                    values.pop(0)
                else:
                    self.dataType = values.pop(0)
            else:
                self.errorsRaised[0] = 1
                return
        else:
            if values:
                for letter in self.createList(values[0]):
                    if letter.isalpha() == False and letter.isdigit() == False:
                        print("Caracter invalido",letter)
                        self.errorsRaised[4] = 1
                    self.statedVar += letter
                    if len(values) > 1:
                        self.errorsRaised[3] = 1
            else:
                self.errorsRaised[2] = 1
        if actualNode.getLeft():
            self.varVerificacion(actualNode.getLeft(), values)
        if actualNode.getRight():
            self.varVerificacion(actualNode.getRight(), values)
    #Recorrido en preorden
    def varAssignation(self, actualNode=Node, values=[]):
        if actualNode == self.getRoot():
            if values:
                if values[0] not in actualNode.getAlphabets():
                    self.errorsRaised[2] = 1
                    values.pop(0)
                else:
                    values.pop(0)
            else:
                self.errorsRaised[0] = 1
                return
        else:
            if actualNode.getAlphabets() == "Cadena":
                string = values[0]
                if string[0] == '"' and string[-1] == '"':
                    pass
                else:
                    self.errorsRaised[5] = 1
                    return
                values.pop(0)

            elif actualNode.getAlphabets() == "Entero":
                string = values[0]
                numbers = [str(x) for x in range(10)]
                for letter in string:
                    if letter not in numbers:
                        self.errorsRaised[5] = 1
                        break
                values.pop(0)

            elif actualNode.getAlphabets() == "Real":
                string = values[0]
                numbers = [str(x) for x in range(10)]
                points = 0
                for letter in string:
                    if letter == ".":
                        points+=1
                    elif letter not in numbers:
                        self.errorsRaised[4] = 1
                        self.errorsRaised[5] = 1
                        break
                values.pop(0)
                if points > 1:
                    self.errorsRaised[5] = 1
            else:
                self.errorsRaised[1] = 1
        if actualNode.getLeft():
            self.varAssignation(actualNode.getLeft(), values)

    def operationVerif(self, actualNode, values):
        if actualNode == self.getRoot():
            if values:
                if values[0] not in actualNode.getAlphabets():
                    self.errorsRaised[2] = 1
                    values.pop(0)
                else:
                    values.pop(0)
            else:
                self.errorsRaised[0] = 1
                return
        #Verifica si estamos en el nodo izquierdo del nodo raiz
        elif actualNode == self.getRoot().getLeft():
            if "Cadena" in actualNode.getAlphabets(): 
                operator = ["+"]
                if values[0] in operator:
                    values.pop(0)
                else:
                    self.errorsRaised[6] = 1
                    values.pop(0)
            elif "Entero" in actualNode.getAlphabets():
                operator = list("+/*-")
                if values[0] in operator:
                    values.pop(0)
                else:
                    self.errorsRaised[6] = 1
                    values.pop(0)
            elif "Real" in actualNode.getAlphabets():
                operator = list("+/*-")
                if values[0] in operator:
                    values.pop(0)
                else:
                    self.errorsRaised[6] = 1
                    values.pop(0)                           
            else:
                self.errorsRaised[1] = 1
                values.pop(0)
        else:
            if "Cadena" in actualNode.getAlphabets() :
                string = values[0]
                if string in actualNode.getAlphabets():
                   return 
                else:
                    if string[0] == '"' and string[-1] == '"':
                        pass
                    else:
                        self.errorsRaised[7] = 1
                        return
                    values.pop(0)

            elif "Entero" in actualNode.getAlphabets() :
                string = values[0]
                if string in actualNode.getAlphabets():
                    return
                else:
                    numbers = [str(x) for x in range(10)]
                    for letter in string:
                        if letter not in numbers:
                            self.errorsRaised[7] = 1
                            break
                    values.pop(0)
            elif "Real" in actualNode.getAlphabets():
                string = values[0]
                if string in actualNode.getAlphabets():
                    return
                else:
                    numbers = [str(x) for x in range(10)]
                    points = 0
                    for letter in string:
                        if letter == ".":
                            points+=1
                        elif letter not in numbers:
                            self.errorsRaised[7] = 1
                            break
                    values.pop(0)
                    if points > 1:
                        self.errorsRaised[7] = 1
        if actualNode.getLeft():
            self.operationVerif(actualNode.getLeft(), values)
        if actualNode.getRight():
            self.operationVerif(actualNode.getRight(), values)

    def resetErrors(self):
        for idx in range(len(self.errorsRaised)):
            self.errorsRaised[idx]=0

    def createList(self, values):
        returnList = []
        for value in values:
            returnList.append(value)
        return returnList
