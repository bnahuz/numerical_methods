import math

def new_rap():
    x = float(input("Aproximação: " ))
    Err = float(input("Erro em forma decimal: " ))
    max_int = int(input("Numéro máximo de iterações: " ))
    #Erel = 1 # Erro Relativo inicial
    k = 1 #Contador

    if df(x) == 0:
        print("A sequência irá divergir.")
    else:
        while k <= max_int:
            k += 1
            A = f(x)
            D = df(x)
            p = x - A/D # Fórmula de Newton-Raphson
            if abs(p - x) < Err: #and abs(A) < Err:
                print("A raiz pelo método de Newton-Raphson é: ", p)
                break
            x = p
        if k > max_int:
            print("O método falhou após", max_int,"iterações.")

f = lambda x: math.exp(x) - 3*(x**2)
df = lambda x : math.exp(x) - 6*x

new_rap()
