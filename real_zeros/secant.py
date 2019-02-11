def secant(a, b, E, n):
    k = 0
    while k < n:
        t_x = ((a * f(b)) - (b * f(a))) \
        / (f(b) - f(a))
        if abs(b-a) < E or abs(f(b)) < E:
            print ("Raiz =  {}".format(t_x))
            break
        a = b
        b = t_x
        
        k += 1
            

f = lambda x: x**3 - 3*x -1
Err = 0.01
secant(0,1,Err,20)
