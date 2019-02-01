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

def extender(A,b):
    n = len(A)
    for i in range(n):
        A[i].append(b[i][0])
    return A

def solve(M):

    def retro_sub(matrix):
        n = len(matrix)
        xn_array = n*[0]
        for i in range (n-1,-1,-1):
            s = sum([matrix[i][j] * xn_array[j] for j in range(i + 1, n)])
            xn_array[i] = (matrix[i][n] - s) / matrix[i][i]
        
        return xn_array

    def gauss(matrix):

        n = len(matrix)
        for k in range (n):
            if matrix[k][k] == 0:
                print("Elemento nulo na posição do pivô")
                break
            else:
                for i in range(k + 1,n):
                    m = -matrix[i][k]/matrix[k][k] #Coeficiente para "zerar" os elementos abaixo do pivô e reorganizar os valores da linha. 
                    for j in range(k ,n+1): #Percorre a linha alterando os valores.
                        #print("Antes: ", matrix[i][j])
                        matrix[i][j] = matrix[i][j] + m * matrix[k][j]
                        #print("Depois: ",matrix[i][j])
                #print(m_array)
        return matrix

    triang_matrix = gauss(M)
    vec_sol = retro_sub(triang_matrix)

    print("\nSolução do sistema: \n",vec_sol)

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
 
    input("\n Aperte Enter para continuar: ")

    print("--------------------------------")

    print("\nAgora, unindo Ax(At*A) com b(At*b) \nformando uma matriz estendida.")

    A_ex = extender(Ax,At_b)

    print("\nMatriz A_ex : ")
    for x in A_ex:
        print(*x, sep=" ")

    print("\nTendo agora a forma Ax = b , resolveremos por \nEliminação de Gauss")

    input("\n Aperte Enter para continuar: ")

    solve(A_ex)

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

