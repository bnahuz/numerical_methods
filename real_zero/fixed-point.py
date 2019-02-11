import math

def dg(x):
  h = 10**-10
  dg = (g(x + h) - g(x))/h
  return dg

def ponto_fixo():
  x = float(input("Aproximação: " ))
  Err = float(input("Erro em forma decimal: " ))
  max_int = int(input("Numéro máximo de iterações: " ))
  k = 1 #Contador

  p_novo = g(x) #Primeira iteração

  if abs(dg(x)) > 1 :
    print("A sequência irá divergir.")
  else:
    while k <= max_int:
      k += 1 # Aumento do contador
      x = p_novo # Atual iteração k 
      p_novo = g(x) #Cálculo da nova iteração k+1 
      if abs(p_novo - x) < Err or abs(f(p_novo)) < Err: #Critérios de parada
        print("A raiz pelo método do Ponto Fixo é aproximadamnete: ", p_novo)
        break

'''f = lambda x: 1 - math.cos(x) #1
g = lambda x : math.cos(x)
'''
'''f = lambda x: x**3 - x - 1 
g = lambda x: math.pow(x+1,1/3)
#x0 = 1  E = 0.001'''

f = lambda x: math.exp(-x**2) - math.cos(x) 
g = lambda x: x + math.cos(x) - math.exp(-x**2) #x0 = [1,2] E= 0.0001

ponto_fixo()
