import math

def ponto_fixo():
    x = float(input("Aproximação: " ))
    E = float(input("Erro em forma decimal: " ))
    n = int(input("Numéro máximo de iterações: " ))

    k = 1

    while k <= n:
        r = g(x)
        if abs(r-x) < E:
            print("A raiz pelo método do Ponto Fixo é: ",r)
            break
        k += 1
        r = x
        if k > n:
            print("O método falhou após", n,"iterações.")
            break

g = lambda x: 1 - math.cos(x)
dg = lambda x : math.sin(x)

ponto_fixo()