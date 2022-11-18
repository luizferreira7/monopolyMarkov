from monopoly_letra_b_alt import *
from math import pow

y = []

#supondo 20 simulações de 10000 jogadas e seja Y a variável aleatória que representa o No de passos até a prisão:
#obter uma aproximação para o valor esperado de Y
# E(x) = somatorio(x*p_x), onde p_x(x=n) = p(1-p)ˆ(n-1), e agora, como escolher p? : 1/6
for i in range(0,20):
    s = simulacao(1000)
    c = jogadasAtePrisao(s)
    y.append(c)

print(y)

soma = sum(y)
media = soma/len(y)
print(media)

def distribuicaoGeometrica(y):
    p = 1/6
    return  pow((1-p),y-1)*p

def esperanca(y):
    esperanca = 0
    for i in range(len(y)):
        esperanca = distribuicaoGeometrica(y[i])*y[i]
        print(esperanca)
    return esperanca

def esperancaY(y):
  esperanca = 0
  for i in range(len(y)):
    esperanca += y[i]
  return esperanca/len(y)

print("Y=y  = " + str(y))
e = esperancaY(y)
print("Aproximação para E(Y): " + str(round(e,2)))

#supondo 1000 simulações de 100000 jogadas e seja Y a variável aleatória que representa o No de passos até a primeira prisão:
y = []
for i in range(0,1000):
    s = simulacao(100000)
    c = jogadasAtePrisao(s)
    y.append(c)
y.sort()
print(y)