def solve(M):
    print(" Matriz inicial: ")
    for x in M:
        print(*x, sep=" ")

    n = len(matrix)
    def retro_sub(n,matrix):
        xn_array = n*[0]
        for i in range (n-1,-1,-1):
            s = sum([matrix[i][j] * xn_array[j] for j in range(i + 1, n)])
            xn_array[i] = (matrix[i][n] - s) / matrix[i][i]
        
        return xn_array

    def gauss(n,matrix):
        m_array = []
        for k in range (n):
            if matrix[k][k] == 0:
                print("Elemento nulo na posição do pivô")
                break
            else:
                #print("Pivô",matrix[k][k] )
                for i in range(k + 1,n):
                    m = -matrix[i][k]/matrix[k][k] #Coeficiente para "zerar" os elementos abaixo do pivô e reorganizar os valores da linha.
                    #print("Coeficiente", m) 
                    m_array.append(m)
                    for j in range(k ,n+1): #Percorre a linha alterando os valores.
                        #print("Antes: ", matrix[i][j])
                        matrix[i][j] = matrix[i][j] + m * matrix[k][j]
                        #print("Depois: ",matrix[i][j])
                #print(m_array)
        return matrix

    triang_matrix = gauss(n,M)
    vec_sol = retro_sub(n,triang_matrix)
     
    print("Matriz Triângular Superior: ")
    for x in triang_matrix:
        print(*x, sep=" ")
    print("Solução do sistema: \n",vec_sol)

matrix = [[2,2,1,1,7],[1,-1,2,-1,1],[3,2,-3,-2,4],[4,3,2,1,12]]

solve(matrix)
