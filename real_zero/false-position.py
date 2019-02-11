import math

def falsa_pos():
  a = float(input("Extremo inicial: " ))
  b = float(input("Extremo final: " ))
  E = float(input("Erro em forma decimal: " ))
  n = int(input("Numéro máximo de iterações: " ))

  k = 1 #Contador de iterações
    
  while k <= n:
    M = f(a) 
    N = f(b)
    t_raiz = (a*N - b*M)/(N-M) # t_raiz é a raiz de teste(possível resultado)
    A = f(t_raiz)

    if abs(b-a) < E or abs(A)<E: #Critérios de parada
        print("A raiz pelo método da Falsa Posição é: ",t_raiz)
        break
    k += 1
    if f(a) * f(t_raiz) < 0:
      b = t_raiz
    else:
      a = t_raiz
    if k > n:
      print("O método falhou após", n,"iterações.")
      break

#f = lambda x: math.log(x-1) + math.cos(x-1) #[1.3,2] E = 0.0001

#f = lambda x: math.sin(x) - math.exp(-x) #[3,4] e [6,7] E = 0.00001

#f = lambda x: x**3 + 3*x**2 - 1 #[-3,-2] E = 0.00001

f =  lambda x: math.exp(x) + math.pow(2,-x) + 2*math.cos(x) - 6 #[1,2] E= 0.0001
falsa_pos()
