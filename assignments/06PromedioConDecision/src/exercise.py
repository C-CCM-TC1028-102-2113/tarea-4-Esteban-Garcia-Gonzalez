def main():
    #escribe tu código abajo de esta línea
    p1=0
    p2=0
    prom=0
    c=0
    while p1>=0:
        p1=float(input())
        c=c+1
        p2=p1+p2
        if 0>p1:
            p2=p2-p1
            c=c-1
            prom=p2/c
    print(prom)
    pass
if __name__=='__main__':
    main()
