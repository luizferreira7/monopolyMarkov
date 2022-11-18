from monopoly_letra_b_alt import *

#supondo 1000 simulações de 100000 jogadas e seja Y a variável aleatória que representa o No de passos até a primeira prisão:
y = []
for i in range(0,1000):
    s = simulacao(10000, False)
    p = passosAtePrisao(s)
    y.append(p)

def esperanca(y:list):
  return sum(y)/len(y)

print("Y=y  = " + str(y))
e = esperanca(y)
print("Aproximação para E(Y): " + str(round(e,2)))
