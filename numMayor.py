a=int(input("Digite 'a':"))
b=int(input("Digite 'b':"))
c=int(input("Digite 'c':"))
def mayor(a,b,c):
    if (a!='' and b!='' and c!=''):
        if(a>b):
            if(a>c):
                print("El mayor es:", a, "y pertenece a 'a'")
            else:
                print("El mayor es:", c, "y pertenece a 'c'")
        elif(b>c):
            print("El mayor es:", b, "y pertenece a 'b'")
        else:
            print("El mayor es:", c, "y pertenece a 'c'")
    else:
        print("Uno o más valores vacíos")
    return ''
print(mayor(a,b,c))
