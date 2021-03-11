from tree import Tree
tree = Tree()
cadena = input()
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
            tree.verificacion(tree.getRoot(), lst)
            tree.printMessages()
        else:
            idx = string.find(';')
            print("Error la cadena '{}' debería ser '{}'".format(string,string[:idx]+string[idx+1:]+";"))
    else:
        print("Error la cadena debe terminar en ';'")

stringVerification(cadena)
