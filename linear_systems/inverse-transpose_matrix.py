def identidade(n):
    I = [[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        I[i][i] = 1
    return I

 
def transposta(mA): #transposta
    n = len(mA)
    mT = identidade(n)
    for i in range(n):
        for j in range(n):
            mT[i][j] = mA[j][i]

    print("Matriz Transposta : ")
    for x in mT:
        print(*x, sep=" ")

    return mT


def inversa(A, arred = 0):
    n = len(A)
    inversa = identidade(n)
    
    indices = list(range(n)) # Auxiliar no loop "for"
    #print(indices)
    for fd in range(n): # fd serve para focar na diagonal
        fdScaler = 1.0 / A[fd][fd]
        # 1º: Reduz a matriz A aplicando as operações na inversa
        for j in range(n): # j analisa as colunas
            A[fd][j] *= fdScaler
            inversa[fd][j] *= fdScaler
        # 2º: Operando todas as linhas exceto alinha fd
        for i in indices[0:fd] + indices[fd+1:]: # Pular a linha fd
            crScaler = A[i][fd] # crScaler = Índice para escalonar as linhas atuais
            for j in range(n): # cr - crScaler * fdRow
                A[i][j] = A[i][j] - crScaler * A[fd][j]
                inversa[i][j] = inversa[i][j] - crScaler * inversa[fd][j]

    if arred == 1:            
        for i in range (n):
            for j in range(n):
                inversa[i][j] = int(inversa[i][j])   

    print("Matriz Inversa : ")
    for x in inversa:
        print(*x, sep=" ")

    return inversa



M = [[12,3,1],[8,4,3],[1,1,1]]
t = transposta(M)
inv = inversa(M, 1)
