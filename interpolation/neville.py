def lagrange_nev(data_x, data_y, x):

    tam = len(data_x)
    Q = [0]*tam

    for k in range(tam):
        for j in range(tam-k):
            if k == 0:
                Q[j] = data_y[j]
            else:
                Q[j] = ((x - data_x[j+k] ) * Q[j]+ \
                        (data_x[j] - x) * Q[j+1]) / \
                        (data_x[j] - data_x[j+k])


    print(Q[0])

x = [0.81,0.83,0.86] # x 
y = [16.94410,17.5692,18.50515] # f(x)
x_bar = 0.84 # O que quer ser encontrado

lagrange_nev(x, y, x_bar)
