# Escribe aquí tus funciones...

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    area=b*a

    volumen=area*p

    print("El volumen del prisma es:",volumen)

if __name__=='__main__':
    main()
