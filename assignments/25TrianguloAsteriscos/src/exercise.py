
def main():
    #Escribe tu código debajo de esta línea
    height = int(input("Enter triangle height: "))
    n=0
    ast=0
    for cont in range (0,height+1):
        if (cont!=0):
            n=height-cont
            ast=str(' '*n+'*'*cont)
            print(ast)
    pass


if __name__=='__main__':
    main()
