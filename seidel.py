def showMatrix(M):
    for i in M:
        print(i, sep=' ')
    print()

def gaussS(A,b):

    xo = [0,0,0] # Chutes
    N = 500 # Limitador de Iterações
    e = 0.001 # Erro
    n = len(A)
    k = 1
    x = [0 for i in range(n)]

    while k <= N:
        for i in range (n):
            soma1,soma2 = 0,0
            for j in range(i):
                soma1 += A[i][j] * x[j]
            for j in range(i+1,n):
                soma2 += A[i][j] * xo[j]

            x[i] = (b[i] - soma1 - soma2)/A[i][i]

            X = []

            for a in range(n):
                X.append(abs(x[a] - xo[a]))

            if max(X) < e:
                return x
        k+=1
        for i in range(n):
            xo[i] = x[i]

    return ("Rodou, rodou e não chegou em lugar nenhum.")

A = [[5,1,1],[3,4,1],[3,3,6]]
b = [5,6,0]

print("# Matriz A: ")
showMatrix(A)

print("# Vetor b: ")
print(b)
print()

print("# Matriz de Coeficientes xi's: ")
print(gaussS(A,b))
