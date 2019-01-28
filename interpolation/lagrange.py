def lagrange(vec_x, vec_f, x=0):

    tam,res = len(vec_x),0
    L = [0]*tam

    for i in range(tam):
        L[i] = 1
        for j in range(tam):
            if j != i:
                L[i] = L[i] * (x - vec_x[j])/(vec_x[i] - vec_x[j])

    for k in range (tam):
        res = res + vec_f[k]*L[k]

    print(res)

x = [0.81,0.83,0.86] # x 
y = [16,9,0.24,2.94] # f(x)
x_bar = 0.84 # O que quer ser encontrado

lagrange(x, y, x_bar)
