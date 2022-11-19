from monopoly_letra_b_alt import *

def media(t, imprimir=True):
  y = []

  contador = 0
  while contador < t:
      s = simulacao(10000, False)
      p = passosAtePrisao(s)

      y.append(p)

      contador += 1

  if (imprimir):
    print(y)

  return sum(y)/len(y)

e = media(1000, False)
print("E(Y): " + str(round(e)))
