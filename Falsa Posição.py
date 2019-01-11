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
        xi = (a*N - b*M)/(N-M)
        A = f(xi)

        if abs(A)<E or abs(b-a) < E:
            print("A raiz pelo método da Falsa Posição é: ",xi)
            break
        k = k + 1
        elif A * N < 0:
            a = b
            M = N
        b = xi
        N = A
        if k > n:
            print("O método falhou após", n,"iterações.")
            break

f = lambda x: math.pow(x,3) + x - 4 