def identity(n):
    m = [[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m

def LU_factor(U_array):
    n = len(U_array)
    m_array = []
    L_array = identity(n)

    for k in range (n):
        if U_array[k][k] == 0:
            print("Elemento nulo na posição do pivô")
            break
        else:
            for i in range(k + 1,n):
                m = -U_array[i][k]/U_array[k][k] #Coeficiente para "zerar" os elementos abaixo do pivô e reorganizar os valores da linha.
                m_array.append(m)
                L_array[i][k] = -m
                for j in range(k,n): #Percorre a linha alterando os valores.
                    U_array[i][j] = U_array[i][j] + m * U_array[k][j]


    print("Matriz U : ")
    for x in U_array:
        print(*x, sep=" ")

    #print(m_array)
    print("Matriz L : ")
    for x in L_array:
        print(*x, sep=" ")

    return U_array,L_array




A = [[1,1],[2,3]]

print("Matriz A : ")
for x in A:
    print(*x, sep=" ")

U_array,L_array = LU_factor(A)


