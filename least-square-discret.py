def MinimosDiscretoLinear(Xi, Yi):
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

    print(soma)
    a0 = (soma[2]*soma[1]-soma[3]*soma[0])/(n*soma[2]-(soma[0])**2)
    a1 = (n*soma[3]-soma[0]*soma[1])/(n*soma[2]-(soma[0]**2))

    print("Alfas: ")
    print("a0: ", a0)
    print("a1: ", a1)
    if a0>0:
        print("f(x) = {}x + {}".format(a1, a0))
    else:
        print("f(x) = {}x{}".format(a1, a0))
      

x = [1,3,4,6,8,9,11,14]
y = [1,2,4,4,5,7,8,9]

MinimosDiscretoLinear(x,y)
