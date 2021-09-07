def main():
    #escribe tu código abajo de esta línea
    n=int(input('Entrada: ' ))
    c=0
    for cont in range(1,n+1):
        c=cont
        if (c%2==0):
            print(c,'-#')
        else:
            print(c,'-%')
    pass

if __name__=='__main__':   
    main()
