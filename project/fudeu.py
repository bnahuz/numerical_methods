def MinimosDiscretoLinear(Xi, Yi, pr = True, t = None):
    '''Entrada: Xi, Yi, é montado uma tabela com os seguintes valores
       Xi, Yi, Xi², Xi*Yi e seus somatórios para encontrar o alfa da equação
       Saída:  os Alfas e a expressão'''
    n = len(Xi)
    tabela = [[0 for i in range(n+1)] for i in range(4)]
    soma = [0]*4 
    
    for i in range(n):
         tabela[0][i] = Xi[i]
         tabela[1][i] = Yi[i]
         tabela[2][i] = Xi[i]**2
         tabela[3][i] = Xi[i]*Yi[i]

    for i in range(4): #Lista com a somatória de todos os elementos
        soma[i] = sum(tabela[i])

    a0 = (soma[2]*soma[1]-soma[3]*soma[0])/(n*soma[2]-(soma[0])**2)
    a1 = (n*soma[3]-soma[0]*soma[1])/(n*soma[2]-(soma[0]**2))

    if pr == True:
        print("\nAlfas: ")
        print("a0: ", a0)
        print("a1: ", a1)
        
        if a0>0:
            print("f(x) = {}x + {}".format(a1, a0))
        else:
            print("f(x) = {}x{}".format(a1, a0))

    if t != None:
        print("\nValor selecionado {}".format(t))
        print("f({}) = {}".format(t, a0*t+a1))

def produto(A,B):

    numLinhasA, numColsA = len(A), len(A[0])
    numLinhasB, numColsB = len(B), len(B[0])

    C = []

    for linha in range(numLinhasA):
        C.append([])
        for coluna in range (numColsB):
            C[linha].append(0)
            for k in range(numColsA):
                C[linha][coluna] += A[linha][k] * B[k][coluna]

    return C

def transposta(mA):
    n = len(mA)
    tam = len(mA[0])
    mT = [[mA[j][i] for j in range(n)] for i in range(tam)]

    return mT

def matrizCoef(A):
    n = len(A)
    mC = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(A[i][j])
        mC.append(l)
    return(mC)

def retroSuperior(a, y):
    n = len(a)
    x = [0 for i in range(n)]
    for i in range(n-1,-1,-1):
        soma = y[i]
        for k in range(i+1,n):
            soma = soma - a[i][k]*x[k]
        x[i] = soma/a[i][i]
    return x

def retroInferior(a, b):
    #Recebe como entrada uma matriz triangular inferior e um vetor B , retorna um vetor y
    n = len(a)
    y = [0 for i in range(n)]
    for i in range(0,n,1):
        y[i] = b[i]
        for k in range(0,i,1):
            y[i] -= y[k]*a[i][k]
        y[i] = y[i]/a[i][i]
    return y
    
def choleskyX(a,b):
    #Função que recebe uma matriz aumentada, faz a fatoração de cholesky e retorna o vetor solução X

    #Calcula matriz dos coeficientes
    mC = matrizCoef(a)

    n = len(mC)
    g = [[0 for i in range(n)] for i in range(n)]
    for k in range(0,n):
        soma = 0
        #Calcula gkk ou elemento da diagonal
        for j in range(0, k):
            soma = soma + (g[k][j])**2
        r = mC[k][k] - soma
        g[k][k] = (r)**(1/2)
        #Calcula elementos abaixo da diagonal ou gik
        for i in range(k+1, n):
            soma = 0
            for j in range (0, k):
                soma = soma + g[i][j]*g[k][j]
            g[i][k] = (mC[i][k] - soma)/g[k][k]

    print("Matriz G")
    for i in range(n):
        print(g[i])
    #Descobre o vetor Y através de G*Y = b
    y = retroInferior(g,b)
    #Descobre o vetor X atravé de gT*X = y
    gT = transposta(g)
    x = retroSuperior(gT,y)
    print("Vetor solução X:")
    print(x)

def sobreDet(x,y):
    A = [[1,i] for i in x]
    b = [[i] for i in y]
    
    print("\nMatriz A : ")
    for x in A:
        print(*x, sep=" ")

    print("\nMatriz b : ")
    for x in b:
        print(*x, sep=" ")
    
    At = transposta(A)

    print("--------------------------------")

    print("\nMatriz At : ")
    for x in At:
        print(*x, sep=" ")

    At_b = produto(At,b) # valor de x

    print("\nMatriz At * b : ")
    for x in At_b:
        print(*x, sep=" ")

    Ax = produto(At,A)

    print("\nMatriz At * A : ")
    for x in Ax:
        print(*x, sep=" ")

    print("\nTendo como Ax = b , resolveremos por Cholesky")

    input("\n Aperte Enter para continuar: ")

    choleskyX(Ax, At_b)

x = [1,3,4,6,8,9,11,14]
y = [1,2,4,4,5,7,8,9]

print("Tabela: ")
print("  x  ", x)
print(" f(x)", y)

input("\n Aperte Enter para continuar: ")

print("\n Vejamos o polinômio gerado pelo \n Método dos Mínimos Quadrados: ")
MinimosDiscretoLinear(x,y)

input("\n Aperte Enter para continuar: ")

print("\n Sistema Linear Sobredeterminado: ")
print("Solução: A(Transposta) * Ax = A(transposta)*b")

input("\n Aperte Enter para continuar: ")

sobreDet(x,y)

