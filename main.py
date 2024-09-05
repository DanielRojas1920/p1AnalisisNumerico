

"""
Antes de ejecutar el programa, hay que instalar la librería sympy ejecutando el 
siguiente comando en la consola o cmd:

pip install sympy

Hay que tener instalado pip, o descargar python desde la microsoft store

Para obtener la versión de python de la microsoft store, 
se puede ejecutar en la terminal el siguiente comando en el cmd:

python

Recomiendo correr el programa en la cmd ya que ahí sí se limpia la pantalla, 
en la terminal integrada de visual code, esto no sucede.

"""

import os
from sympy import * 
from metodos import *

x=symbols('x') #Inicializar la variable x


def menu():

    faux = exp(-x)-x/2 #Función por defecto
    a=0 #limite inferior
    b=0 #limite superior
    minerr=0 #Minimo error ingresado por el usuario
    xi=0 #xi
    xant=0 #xi-1

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

        try: #try except para validar el input
            select = int(input("\nIntroduzca la opción a realizar: "))
            if (select <= 0 or select >= 7):
                print("Opción inválida")
                os.system("pause")
        except Exception as err:
            if (err == KeyboardInterrupt): raise KeyboardInterrupt #Permite usar ctrl+c para terminar en seco el programa
            print("Opción inválida")
            os.system("pause")
            select = 0

        while (select == 1): #Cambiar función
            os.system("cls")
            print("Ejemplos de funciones fundamentales:")
            print("Input\tRepresentación matemática")
            print("exp(x):\te^x")
            print("x**2:\tx^2")
            print("cos(x):\tcos(x)")
            print("log(x):\tln(x)")
            print("Más información en https://people.duke.edu/~ccc14/sta-663-2016/10_SymbolicAlgebra.html#Basics")

            try: #Validar si la función ingresada es válida
                faux = eval(str(input("\nIntroduzca la nueva función: ")))
                select = 0 if (str(input("\nDeseas continuar? (y: sí): ")).lower() == 'y') else 1 #Si se introduce y, se guarda la función ingresada
                f.change_function(faux) if (select == 0) else None
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print("Función inválida")
                os.system("pause")
        
        while (select == 2): #Método de bisección
            os.system("cls")
            try:
                a = float(input("\nIngrese el límite inferior: "))
                b = float(input("Ingrese el límite superior: "))
                minerr = float(input("Ingrese el error mínimo en porcentaje: "))
                if (minerr <= 0): raise ValueError("Error mínimo negativo o igual a 0") #Checar que el mínimo error sea mayor a 0
                metodoBiseccion(a,b,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 2 #Si se introduce y, se vuelve al menú
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")

        while (select == 3): #Método Posición falsa
            os.system("cls")
            try:
                a = float(input("\nIngrese el límite inferior: "))
                b = float(input("Ingrese el límite superior: "))
                minerr = float(input("Ingrese el error mínimo en porcentaje: "))
                if (minerr <= 0): raise ValueError("Error mínimo negativo o igual a 0")
                metodoPosicionFalsa(a,b,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 3
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")

        while (select == 4): #Método Newton-Raphson
            os.system("cls")
            try:
                xi = float(input("\nIngrese el valor inicial: "))
                minerr = float(input("Ingrese el error mínimo en porcentaje: "))
                if (minerr <= 0): raise ValueError("Error mínimo negativo o igual a 0")
                metodoNR(xi,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 4
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")


        while (select == 5): #Método de la secante
            os.system("cls")
            try:
                xi = float(input("\nIngrese el valor inicial (i): "))
                xant = float(input("\nIngrese el valor anterior (i-1): "))
                minerr = float(input("\nIngrese el error mínimo en porcentaje: "))
                if (minerr <= 0): raise ValueError("Error mínimo negativo o igual a 0")
                metodoSecante(xi,xant,f,minerr)
                select = 0 if (str(input("\nDeseas volver al menú principal? (y: sí): ")).lower() == 'y') else 5
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                print("\nValor inválido")
                os.system("pause")




class Function():
    def __init__(self,f): #Inicializar función ingresada (en este caso la por defecto)
        self.f= f
        self.dfx = diff(self.f,x) #Obtiene la derivada de la función

    def eval_function(self,input):
        return self.f.subs(x,input) #Evaluar un punto en la función
    
    def eval_dev_function(self,input):
        return self.dfx.subs(x,input) #Evaluar un punto en la derivada de la función
    
    def change_function(self, f): #Cambiar función y derivada almacenadas en el objeto
        self.f = f
        self.dfx = diff(self.f)


menu() #Ejecuta el programa