import math

def new_rap():
  x = float(input("Aproximação: " ))
  Err = float(input("Erro em forma decimal: " ))
  max_int = int(input("Numéro máximo de iterações: " ))
  
  k = 1 #Contador

  if df(x) == 0:
    print("A sequência irá divergir.")
  else:
    while k <= max_int:
      k += 1
      A = f(x)
      D = df(x)
      p = x - A/D # Fórmula de Newton-Raphson(iteração atual)
      if abs(p - x) < Err: #and abs(A) < Err:
          print("A raiz pelo método de Newton-Raphson é: ", p)
          break
      x = p #Nova alocação para a próxima iteração
      if k > max_int:
        print("O método falhou após", max_int,"iterações.")

'''f = lambda x: math.exp(x) - 3*(x**2)
df = lambda x : math.exp(x) - 6*x #[0,1] e [3,5]'''

'''f = lambda x: (x-2)**2 - math.log(x)
df = lambda x: 2*(x-2) - 1/2 #[1,2] e [e,4]'''

f = lambda x: x**4 - 2*math.pow(x,3) + 4*x - 1.6
df = lambda x: 4*math.pow(x,3) - 6*math.pow(x,2) + 4 #[-2,-1] e [0,1]
new_rap()
