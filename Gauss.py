def solve(M):
    print(" Matriz inicial: ", M, '\n')
    n = len(matrix)
    def retro_sub(n,matrix):
        xn_array = n*[0]

        for k in range (n-1,1,-1):
            s = sum([matrix[k][j] * xn_array[j] for j in range(k + 1, n)])
            xn_array[k] = (matrix[k][n] - s) / matrix[k][k]
            
        return matrix

    def gauss(n,matrix):
        
        for k in range (n):
            if matrix[k][k] == 0:
                print("Elemento nulo na posição do pivô")
                break
            for i in range(k + 1,n):
                m = -matrix[i][k]/matrix[k][k]
                for j in range(k ,n+1):
                    matrix[i][j] = matrix[i][j] + m * matrix[k][j]
        return matrix

    gauss_matrix = gauss(n,M)
    triang_matrix = retro_sub(n,gauss_matrix)
     
    print("Matriz de Gauss: ", gauss_matrix, '\n' )
    print("Matriz Retrosubstituição: ", triang_matrix, '\n')



matrix = [[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]]

solve(matrix)
