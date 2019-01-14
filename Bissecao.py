import math
def min_interacoes(a0,b0,E):
  """
  min_interacoes funciona de acordo com elementos previamente
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
  min_i = min_interacoes(a,b,E)
  print('O número mínimo de iterações para esta função é de: ',min_i)
  n = int(input("Numéro máximo de iterações: " ))
  i = 1 # Contador de iterações
  Kzao = f(a) # Variável alocada para receber o valor de f(a) 

  while i <= n:
    x = (a+b)/2 #Média do intervalo
    fx = f(x) #Média em função de x
    if fx == 0 or (b-a) < E: #Critério de parada
      print("A raiz pelo método da bisseção é: ",x)
      break
    i += 1 #Incremento do contador
    if Kzao*fx < 0:
      b = x 
    else:
      a = x 
      Kzao = fx
    if i > n:
      print("O método falhou após", n,"iterações.")
      break
f = lambda x: x**2 - 5*math.sin(x) #[1,3] E = 0.01
#f = lambda x: math.pox(2,x) - 3*x # [0,1] e [3,4] E= 0.1
#f = lambda x: (x+2)*(x+1)*x*math.pow(x-1,3) * (x-2) # [-3,2.5] e [-2.5,1]
bissecao()
