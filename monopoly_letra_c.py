from monopoly_letra_b import *

@np_cache
def passosAtePrisao(simulacao):

    contador = 0
    preso = False

    for j in simulacao:
        if (j.turnosCadeia != 0):
            preso = True
            break
        elif (j.duplas == 0):
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

e = media(100, False)
print("E(Y): " + str(round(e)))
