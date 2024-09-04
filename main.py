import os
from sympy import *
from metodos import *

x=symbols('x')


def menu():

    faux = exp(-x)-x/2
    a=0
    b=0
    minerr=0

    f = Function(faux)

    select = 0

    while select != 6:
        os.system('cls')
        print("\nCalculadora de raíces\n\n")
        print(f"1. Cambiar función\tFunción actual: {faux}")
        print("2. Método de bisección")
        print("3. Método de posición falsa")
        print("4. Método de Newton-Raphson")
        print("5. Método de la secante")
        print("6. Salir")

        try:
            select = int(input("\nIntroduzca la opción a realizar: "))
            if (select <= 0 or select >= 7):
                print("Opción inválida")
                os.system("pause")
        except Exception as err:
            if (err == KeyboardInterrupt): raise KeyboardInterrupt
            print("Opción inválida")
            os.system("pause")
            select = 0

        while (select == 1):
            os.system("cls")
            print("Ejemplos de funciones fundamentales:")
            print("Input\tRepresentación matemática")
            print("exp(x):\te^x")
            print("x**2:\tx^2")
            print("cos(x):\tcos(x)")
            print("log(x):\tln(x)")
            print("Más información en https://people.duke.edu/~ccc14/sta-663-2016/10_SymbolicAlgebra.html#Basics")

            try:
                faux = eval(str(input("\nIntroduzca la nueva función: ")))
                select = 0 if (str(input("\nDeseas continuar? (y: sí): ")).lower() == 'y') else 1
                f.change_function(faux) if (select == 0) else None
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print("Función inválida")
                os.system("pause")
        
        while (select == 2):
            os.system("cls")
            try:
                a = float(input("\nIngrese el límite inferior: "))
                b = float(input("Ingrese el límite superior: "))
                minerr = float(input("Ingrese el error mínimo en porcentaje: "))
                metodoBiseccion(a,b,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 2
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")

        while (select == 3):
            os.system("cls")
            try:
                a = float(input("\nIngrese el límite inferior: "))
                b = float(input("Ingrese el límite superior: "))
                minerr = float(input("Ingrese el error mínimo en porcentaje: "))
                metodoPosicionFalsa(a,b,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 3
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")

        while (select == 4):
            os.system("cls")
            try:
                xi = float(input("\nIngrese el valor inicial: "))
                minerr = float(input("Ingrese el error mínimo en porcentaje: "))
                metodoNR(xi,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 4
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")


        while (select == 5):
            os.system("cls")
            try:
                xi = float(input("\nIngrese el valor inicial (i): "))
                xant = float(input("\nIngrese el valor anterior (i-1): "))
                minerr = float(input("\nIngrese el error mínimo en porcentaje: "))
                metodoSecante(xi,xant,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 5
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")




class Function():
    def __init__(self,f):
        self.f= f
        self.dfx = diff(self.f,x)

    def eval_function(self,input):
        return self.f.subs(x,input)
    
    def eval_dev_function(self,input):
        return self.dfx.subs(x,input)
    
    def change_function(self, f):
        self.f = f
        self.dfx = diff(self.f)


menu()