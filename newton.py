'''
Initial:
   55.0000
  -12.5000
'''

import numpy

n = 1000
p = 21
initial = numpy.zeros(2)

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


def newton(X,tol):

    k = 0;

    while (k < n):
        k = k + 1
        delta = numpy.dot((-numpy.linalg.inv(JF(X))),F(X))

        if(numpy.isnan(numpy.sum(delta))):
            break

        X = X + delta

        if ((numpy.linalg.norm(delta,numpy.inf) < tol)):
            if(k==5):
                print "Initial:"
                print initial
                print "Delta"
                print delta
                print "X:"
                print X
                print "F(X) com p=" + str(p) + ":"
                print F(X)
            return X

    #raise NameError('num. max. iter. excedido.')
    X[0] = None
    X[1] = None
    return X

## PARA P = 9
#chute pra k=5 = 1 0
initial[0] = 0.16
initial[1] = 1.31
sol = newton(initial,0.00001)

#chute pra k=5 = 24 7
initial[0] = 0.7
initial[1] = 6.14
sol = newton(initial,0.00001)

#chute que divege: 0 700

## PARA P = 21
#chute que divege: 0 170
#chute pra k=5 = 0 1
#chute pra k=5 = 6 6

i = 0
j = 0
while (i < 1000):
    j = 0
    while (j < 1000):
        initial[0] = i
        initial[1] = j
        sol = newton(initial,0.00001)
        '''
        if(sol.all(None)):
            print "Deu ruim:"
            print initial
        '''
        j = j + 1
    i = i + 1
