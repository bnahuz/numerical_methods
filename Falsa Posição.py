import math

def falsa_pos():
    a = float(input("Extremo inicial: " ))
    b = float(input("Extremo final: " ))
    E = float(input("Erro em forma decimal: " ))
    n = int(input("Numéro máximo de iterações: " ))

    k = 2
    
    while k <= n:
        M = f(a)
        N = f(b)
        t_raiz = (a*N - b*M)/(N-M)
        A = f(t_raiz)

        if abs(b-a) < E or abs(A)<E:
            print("A raiz pelo método da Falsa Posição é: ",t_raiz)
            break
        k = k + 1
        if A * N < 0:
            a = b
            M = N
        b = t_raiz
        N = A
        if k > n:
            print("O método falhou após", n,"iterações.")
            break

f = lambda x: math.log(x-1) + math.cos(x-1)

falsa_pos()
