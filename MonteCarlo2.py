import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

import numpy
#print(numpy.random.__doc__)
#print(numpy.random.uniform.__doc__)

a = -1
b = 1
h = 3
N = 1000

#(pseido)gadījumu skaitļu ģeneratora "grauds"
#numpy.random.seed(1)

x = numpy.random.uniform(a,b,N)
#x = numpy.random.normal(a,b,N)
'''
k = [0, 0, 0, 0, 0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] <2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1

print(k)
print(sum(k))
'''
y = numpy.random.uniform(a,b,N)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $asin(x)$')
#plt.plot(x, y, 'ko')
N1 = -1
for i in range(N):
    if y[i] < x[i]:
        #print(x[i], y[i], 'go')
        plt.plot(x[i], y[i], 'go')
        N1 = N1 + 1
    elif y[i] > x[i]:
        N2 = N2 + 1
    else:
        #print(x[i], y[i], 'ro')
        plt.plot(x[i], y[i], 'ro')

#print(N1)
S_zinaamais = (N1 - N2)/N
S_nezinaamais = 1. * S_zinaamais * N1 / N2
print(S_nezinaamais)

plt.show()

