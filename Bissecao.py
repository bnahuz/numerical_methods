import math
def max_interacoes(a0,b0,E):
     """
        max_interacoes funciona de acordo com elementos previamente
        dados para retornar o valor mínimo de iterações necessárias
        para a aproximação da raiz de acordo com a fórmula:
            n >= log(a - b) - log (E) / log(2)
      Argumentos:
          a0: Início do intervalo
          b0: Final do intervalo
          E:  Erro considerado
      Retorna:
          Um n(número mínimo) de iterações necessárias.
    """
    conta = (math.log10(b0-a0)-math.log10(E))/math.log10(2)
    res = int(math.ceil(conta))
    return res

def bissecao():
    a = float(input("Extremo inicial: " ))
    b = float(input("Extremo final: " ))
    E = float(input("Erro em forma decimal: " ))
    max_i = max_interacoes(a,b,E)
    print('O número mínimo de iterações para esta função é de: ',max_i)
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
