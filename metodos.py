import os
from sympy import *
#from main import Function

maxiter = 100

def metodoBiseccion(a,b,f, minerr):
    table= '\na\tb\tr\tcriterio\tError\n'
    select = ''
    os.system('cls')
    r=0 #Aproximación actual
    rant = 0 #Aproximación de la iteración anterior
    err = 100 #Error relativo
    fr = -1 # f(r)
    i=0
    try:
        while (err >= minerr and i < maxiter):
            r = (a+b)/2
            fr = float(f.eval_function(r))
            fa= float(f.eval_function(a))
            crt = True if fa*fr <0 else False  #Criterio
            err = 100*abs((r-rant)/r) if r != 0 else 100*abs((0.00001-rant)/0.00001) #Error relativo 
            rant = r #Guardar la r actual para la siguiente iteración       
            table += f'\n{a:.4f}\t{b:.4f}\t{r:.4f}\t{"f(a)f(r) < 0" if crt else "f(a)f(r) > 0"}\t{err:.2f}'  #Guardar información

            
            if (fr == 0): break

            if (crt):  #Si f(a)f(b) < 0
                b = r
            else:   #Si f(a)f(b) > 0
                a = r

            i+=1

        if (i < maxiter):
            print(table)
            print(f"\n\nIntersección encontrada en x={r}") if (fr == 0) else None
        else:
            print("El programa superó el número máximo de iteraciones permitido (100)")
            print(f"\n\nIntersección encontrada en x={r}") if (fr == 0) else None
            select = str(input("Deseas ver la tabla resultante? (y: sí)"))
            print(table) if (select.lower() == 'y') else None
    except Exception as err:
        print("\nSurgió un error al momento de ejecutar el algoritmo")
        select = str(input("Deseas ver la tabla resultante? (y: sí)"))
        print(table) if (select.lower() == 'y') else None



def metodoPosicionFalsa(a,b,f, minerr):
    table= '\na\tb\tr\tcriterio\tError\n'
    select = ''
    os.system('cls')
    r=0 #Aproximación actual
    rant = 0 #Aproximación de la iteración anterior
    err = 100 #Error relativo
    fr = -1 # f(r)
    i=0

    try:
        while (err >= minerr and i < maxiter):
            fb = float(f.eval_function(b))
            fa= float(f.eval_function(a))
            r = b - ((fb*(a-b))/(fa - fb)) if ((fb*(a-b)) != 0 and (fa - fb) != 0) else b- 0.1
            fr = float(f.eval_function(r))

            crt = True if fa*fr <0 else False  #Criterio
            err = 100*abs((r-rant)/r) if r != 0 else 100*abs((0.00001-rant)/0.00001) #Error relativo 
            rant = r #Guardar la r actual para la siguiente iteración      

            table += f'\n{a:.4f}\t{b:.4f}\t{r:.4f}\t{"f(a)f(r) < 0" if crt else "f(a)f(r) > 0"}\t{err:.2f}'  #Guardar información
            
            if (fr == 0): break

            if (crt):  #Si f(a)f(b) < 0
                b = r
            else:   #Si f(a)f(b) > 0
                a = r

            i+=1

        if (i < maxiter):
            print(table)
            print(f"\n\nIntersección encontrada en x={r}") if (fr == 0) else None
        else:
            print("El programa superó el número máximo de iteraciones permitido (100)")
            print(f"\n\nIntersección encontrada en x={r}") if (fr == 0) else None
            select = str(input("Deseas ver la tabla resultante? (y: sí)"))
            print(table) if (select.lower() == 'y') else None
    except Exception as err:
        print("\nSurgió un error al momento de ejecutar el algoritmo")
        select = str(input("Deseas ver la tabla resultante? (y: sí)"))
        print(table) if (select.lower() == 'y') else None


def metodoNR(xi,f, minerr):
    table= "\ni\txi\tf(x)\tf'(x)\txi+1\terror\n"
    select = ''
    os.system('cls')
    xant = 0 #Aproximación de la iteración anterior
    err = 100 #Error relativo
    i=0
    try:
        while (err >= minerr and i < maxiter):
            fx = float(f.eval_function(xi))
            if (fx == 0): break
            dfx = float(f.eval_dev_function(xi))
            dx = fx/dfx if (fx != 0 and dfx != 0) else .1
            xant = xi

            xi = xi - dx

            

            err = 100*abs((xi-xant)/xi) if xi != 0 else 100*abs((0.00001-xant)/0.00001) #Error relativo      

            table += f'\n{i}\t{xant:.4f}\t{fx:.4f}\t{dfx:.4f}\t{xi:.4f}\t{err:.2f}'  #Guardar información

            i+=1

        if (i < maxiter):
            print(table)
            print(f"\n\nIntersección encontrada en x={xi}") if (fx == 0) else None
        else:
            print("El programa superó el número máximo de iteraciones permitido (100)")
            print(f"\n\nIntersección encontrada en x={xi}") if (fx == 0) else None
            select = str(input("Deseas ver la tabla resultante? (y: sí)"))
            print(table) if (select.lower() == 'y') else None
    except Exception as err:
        print("\nSurgió un error al momento de ejecutar el algoritmo")
        select = str(input("Deseas ver la tabla resultante? (y: sí)"))
        print(table) if (select.lower() == 'y') else None

def metodoSecante(xi, xant,f, minerr):
    table= "\ni\txi-1\txi\txi+1\terror\n"
    select = ''
    os.system('cls')
    xant = 0 #Aproximación de la iteración anterior
    err = 100 #Error relativo
    i=0

    try:
        while (err >= minerr and i < maxiter):
            fx = float(f.eval_function(xi))
            if (fx == 0): break
            fxant = float(f.eval_function(xant))
            
            #print('a')
            xaft = xi -(fx*(xant - xi))/(fxant-fx) if (fx != fxant and xant != xi) else xi - 0.01
            


            err = 100*abs((xaft-xi)/xaft) if xaft != 0 else 100*abs((0.00001-xi)/0.00001) #Error relativo      

            #print(f'\n{i}\t{xant:.4f}\t{xi:.4f}\t{xaft:.4f}\t{err:.2f}')
            table += f'\n{i}\t{xant:.4f}\t{xi:.4f}\t{xaft:.4f}\t{err:.2f}'  #Guardar información

            xant = xi
            xi = xaft
            i+=1

        if (i < maxiter):
            print(table)
            print(f"\n\nIntersección encontrada en x={xi}") if (fx == 0) else None
        else:
            print("El programa superó el número máximo de iteraciones permitido (100)")
            print(f"\n\nIntersección encontrada en x={xi}") if (fx == 0) else None
            select = str(input("Deseas ver la tabla resultante? (y: sí)"))
            print(table) if (select.lower() == 'y') else None
    except Exception as err:
        print("\nSurgió un error al momento de ejecutar el algoritmo")
        select = str(input("Deseas ver la tabla resultante? (y: sí)"))
        print(table) if (select.lower() == 'y') else None



