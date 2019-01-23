def identidade(n):
    m = [[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m

def inversa(A):
    n = len(A)
    inversa = identidade(n)
    print("Matriz Inicial : ")
    for x in A:
        print(*x, sep=" ")

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

    print("Matriz Inversa : ")
    for x in inversa:
        print(*x, sep=" ")

    return A,inversa




A = [[12,3,1],[8,4,3],[1,1,1]]

inversa(A)
