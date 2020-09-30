def calc():
    print("Elige una Operación")
    a = input('Suma [s], Resta [r], Multiplicación [m], División [d]: ')
    num1= input("Ingresa el primer número: ")
    num2 = input("Ingresa el segundo número: ")

    if a=="s":
        print(su(num1,num2))
    elif a=="r":
        print(res(num1,num2))
    elif a=="m":
        print(mul(num1,num2))
    else:
        print(div(num1,num2))
