import numpy

# Altere o p aqui conforme desejado. Gabriela: p = 9, Luiz: p = 21
p = 9
chute = numpy.zeros(2)

def chutesQueDivergem():
    i = 0
    while (i < 25):
        j = 0
        while (j < 25):
            chute[0] = i
            chute[1] = j
            if (newton(chute,0.00001,1000) is None):
                print "Diverge: " + str(chute)
            j = j + 0.25
        i = i + 0.25

def chutesParaSol1():

    sol1 = numpy.zeros(2)
    if(p == 9):
        sol1[0] = 0.16
        sol1[1] = 1.31
    elif(p == 21):
        sol1[0] = 0.15
        sol1[1] = 1.32

    i = 0
    while (i < 25):
        j = 0
        while (j < 25):
            chute[0] = i
            chute[1] = j
            resultado = newton(chute,0.00001,5,nFixo=True)
            if(resultado is not None and (numpy.linalg.norm(resultado - sol1,numpy.inf) < 0.01)):
                print "Converge para a solucao " + str(sol1) + ": " + str(chute)
            j = j + 0.25
        i = i + 0.25

def chutesParaSol2():

    sol2 = numpy.zeros(2)
    if(p == 9):
        sol2[0] = 0.7
        sol2[1] = 6.14
    elif(p == 21):
        sol2[0] = 0.38
        sol2[1] = 6.13

    i = 0
    while (i < 25):
        j = 0
        while (j < 25):
            chute[0] = i
            chute[1] = j
            resultado = newton(chute,0.00001,5,nFixo=True)
            if(resultado is not None and (numpy.linalg.norm(resultado - sol2,numpy.inf) < 0.01)):
                print "Converge para a solucao " + str(sol2) + ": " + str(chute)
            j = j + 0.25
        i = i + 0.25

def F(X):
    ret = numpy.zeros(2)

    ret[0] = numpy.exp(-X[0]) + numpy.exp(X[1]) - pow(X[0],2) - 2*pow(X[1],3)
    ret[1] = numpy.cos(X[0] + p*X[1]) + p*X[0] - X[1] - 1

    return ret


def JF(X):
    ret = numpy.zeros((2,2))

    ret[0,0] = -2*X[0] - numpy.exp(-X[0])
    ret[0,1] = numpy.exp(X[1]) - 6*pow(X[1],2)
    ret[1,0] = p - numpy.sin(X[0] + p*X[1])
    ret[1,1] = -p * numpy.sin(X[0] + p*X[1]) - 1

    return ret


def newton(X,tol,n,verboso=False,nFixo=False):

    k = 0;

    while (k < n):
        k = k + 1
        delta = numpy.dot((-numpy.linalg.inv(JF(X))),F(X))

        if(numpy.isnan(numpy.sum(delta))):
            break

        X = X + delta

        if ((numpy.linalg.norm(delta,numpy.inf) < tol)):
            if(verboso):
                print "chute:"
                print chute
                print "Delta"
                print delta
                print "X:"
                print X
                print "F(X) com p=" + str(p) + ":"
                print F(X)

            if(k==n):
                return X
            if not (nFixo):
                return X

    return None

chutesParaSol1()
print "--------------------------------------------"
chutesParaSol2()
print "--------------------------------------------"
chutesQueDivergem()
