'''
Adaptado de: 
    Numerical Methods for Mathematics, Science and Engineering, [Graphics:../Images/FixedPointProg_gr_1.gif] Ed, 1992
    John H. Mathews
    Prentice-Hall, Inc
    ISBN:  0-13-624990-6 
'''

import math

def ponto_fixo():
    x = float(input("Aproximação: " ))
    Err = float(input("Erro em forma decimal: " ))
    max_int = int(input("Numéro máximo de iterações: " ))
    Erel = 1 # Erro Relativo inicial
    k = 1 #Contador

    p_novo = g(x) #Primeira iteração

    if abs(dg(x)) > 1 :
        print("A sequência irá divergir.")
    else:
        while k <= max_int and Erel >= Err:
            k += 1 # Aumento do contador
            x = p_novo # Atual iteração k 
            p_novo = g(x) #Cálculo da nova iteração k+1 
            Delta = abs(p_novo - x) # Diferença em g(x) ~ Erro Absoluto
            Erel = (2*Delta)/abs(p_novo) + Err #Erro Relativo
        print("A raiz pelo método do Ponto Fixo é aproximadamnete: ", p_novo)

g = lambda x: math.cos(x)
dg = lambda x : -math.sin(x)

ponto_fixo()
