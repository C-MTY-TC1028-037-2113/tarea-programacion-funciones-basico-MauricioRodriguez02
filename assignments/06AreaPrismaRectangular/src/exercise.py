def area(base,altura):
    return 

def area_prisma(base,altura,profundidad):
    return area(base,altura)*2+area(altura,profundidad)*2+area(base,profundidad)*2

def main():
    
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = (b*a)*2+(a*p)*2+(b*p)*2

    print("El área total del prisma es:",r)

if __name__=='__main__':
    main()
