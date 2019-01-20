def identity(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m

def gauss(matrix):
    n = len(matrix)
    m_array = []
    L_array = identity(n)

    for k in range (n):
        if matrix[k][k] == 0:
            print("Elemento nulo na posição do pivô")
            break
        else:
            for i in range(k + 1,n):
                m = -matrix[i][k]/matrix[k][k] #Coeficiente para "zerar" os elementos abaixo do pivô e reorganizar os valores da linha.
                m_array.append(m)
                L_array[i][k] = m
                for j in range(k-1 ,n): #Percorre a linha alterando os valores.
                    matrix[i][j] = matrix[i][j] + m * matrix[k][j]
    

    return matrix,L_array


A = [[1,1,1],[2,1,-1],[3,2,0]]

print("Matriz A : ")
for x in A:
    print(*x, sep=" ")

U_matrix,L_matrix = gauss(A)

print("Matriz L : ")
for x in L_matrix:
    print(*x, sep=" ")

print("Matriz U : ")
for x in U_matrix:
    print(*x, sep=" ")
