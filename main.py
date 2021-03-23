from tree import Tree
from node import Node
import string

treeVarDesc = Tree()
treeVarAss = Tree()

def setTree1():
    rootNode = Node(["Cadena","Entero","Real"])
    leaf = Node(list(string.ascii_lowercase)+list(string.ascii_uppercase)+[str(x) for x in range(10)])
    rootNode.setLeft(leaf)
    treeVarDesc.setRoot(rootNode)

def setTree2(var, dataType):
    rootNode = Node([var])
    leaf = Node(dataType)
    rootNode.setLeft(leaf)
    treeVarAss.setRoot(rootNode)

    pass

def stringVerification(string):
    if ';' in string:
        if string[-1] == ';':
            #New string without ';'
            string = string[:-1]
            #Convert string to list
            string = string.split(" ")
            lst = []
            for value in string:
                if value != "":
                    lst.append(value)
            setTree1()
            treeVarDesc.varVerificacion(treeVarDesc.getRoot(), lst)
            treeVarDesc.printMessages()
        else:
            idx = string.find(';')
            print("Error la cadena '{}' debería ser '{}'".format(string,string[:idx]+string[idx+1:]+";"))
    else:
        print("Error la cadena debe terminar en ';'")

def varVerification(string):
    #var=a;
    #;
    if ';' in string:
        if string[-1] == ';':
            #New string without ';'
            string = string[:-1]
            
            if "=" in string:
                string = string.split("=")
                lst = []
                for idx,value in enumerate(string):
                    if value != "":
                        lst.append(value.replace(' ',''))
                setTree2(treeVarDesc.getStatedVar(), treeVarDesc.getDataType())
                treeVarAss.varAssignation(treeVarAss.getRoot(), lst)
                treeVarAss.printMessages()
            else:
                print("Error la cadena debe contener un '='")
        else:
            idx = string.find(';')
            print("Error la cadena '{}' debería ser '{}'".format(string,string[:idx]+string[idx+1:]+";"))
    else:
        print("Error la cadena debe terminar en ';'")     
def operation(string):
    if ";" in string:
        if string[-1] == ';':
            pass
        else:
            idx = string.find(';')
            print("Error la cadena '{}' debería ser '{}'".format(string,string[:idx]+string[idx+1:]+";"))
    else:
        print("Error, la cadena debe terminar en ';'")
var_dec = input("Declara la variable: ") #variable declarada        
stringVerification(var_dec)

var_assig = input("Asigna valor: ") #asignacion de valores a una variable
varVerification(var_assig)