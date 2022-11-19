from monopoly_letra_b_alt import *

@np_cache
def passosAtePrisao(simulacao):

    contador = 0
    preso = False

    for j in simulacao:
        if (j == 120):
            preso = True
            break
        elif (j < 40):
            contador += 1

    return contador if preso == True else 0

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
