
def main():
    #escribe tu código abajo de esta línea
    index = int(input("Enter the index: "))
    n1=0
    n2=1
    s=0
    i=0
    while i<=index:
        i=i+1
        n1=n2
        n2=s
        s=n1+n2
    print(n2)
    pass

if __name__=='__main__':
    main()
