import math
def max_interacoes(a0,b0,E): 
    conta = (math.log10(b0-a0)-math.log10(E))/math.log10(2)
    res = int(math.ceil(conta))
    return res

def bissecao():
    a = float(input("Extremo inicial: " ))
    b = float(input("Extremo final: " ))
    E = float(input("Erro em forma decimal: " ))
    maxi = max_interacoes(a,b,E)
    print('O número mínimo de iterações para esta função é de: ',maxi)
    n = int(input("Numéro máximo de iterações: " ))
    i = 1
    Kzao = f(a)

    while i <= n:
        x = (a+b)/2
        fx = f(x)
        if fx == 0 or (b-a) < E:
            print("A raiz pelo método da bisseção é: ",x)
            break
        i += 1
        if Kzao*fx < 0:
            b = x
        else:
            a = x
            Kzao = fx
            print("O método falhou após", n,"iterações.")
            break
f = lambda x: math.pow(x,3) + x - 4 
bissecao()