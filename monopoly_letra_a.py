import numpy as np
from fractions import Fraction

def linhaMatrizTransicao(linha):

    linhaMarkov = np.zeros([123])

    probsCasas = [0, 0, 1/18, 1/18, 1/9, 1/9, 1/6, 1/9, 1/9, 1/18, 1/18, 0]

    if (linha <= 119):
        linhaAux = linha % 40
        inicio = (linhaAux * 1)
        over = (12 + inicio) - 40
        for i in range(40):
            if (i > inicio) and (i <= (inicio + 12)):
                linhaMarkov[i] = probsCasas[i-linhaAux-1]
            if (over >= 0) and (i <= over):
                linhaMarkov[i] = probsCasas[len(probsCasas) - 1 - over + i]

        inicio = 40
        fim = 80
        if (linha >= 0 and linha <= 79):
            if (linha >= 40 and linha <= 79):
                inicio = 80
                fim = 120

            for j in range(inicio, fim):
                if (linha%40 == j%40):
                    linhaMarkov[j] = 1/6
                else:
                    linhaMarkov[j] = 0

        if (linha >= 80 and linha <= 119):
            linhaMarkov[120] = 1/6

    else:
        if (linha == 120):
            linhaMarkov[20] = 1/6
            linhaMarkov[121] = 5/6

        if (linha == 121):
            linhaMarkov[20] = 1/6
            linhaMarkov[122] = 5/6

        if (linha == 122):
            linhaMarkov[20] = 1
        
    return linhaMarkov

def imprimeLinhaMatriz(estado):
    linha = linhaMatrizTransicao(estado)

    linhaAux = []
    for j in range(len(linha)):
        linhaAux.append(str(Fraction(linha[j]).limit_denominator()))

    for i in range(5):
        print(''.join(['{:5}'.format(item) for item in linhaAux[i*40:(i+1)*40]]))

def imprimeMatriz(m):
  auxM = []
  for i in range(len(m)):
    aux = []
    for j in range(len(m[i])):
      s = str(Fraction(m[i][j]).limit_denominator())
      aux.append(s)
    auxM.append(aux)
  
  print(('\n\n').join([''.join(['{:5}'.format(item) for item in row]) for row in auxM]))

matrizTransicao = np.zeros([123, 123])

for i in range(123):
    matrizTransicao[i] = linhaMatrizTransicao(i)

for i in range(123):
    s = np.sum(matrizTransicao[i, :])
    if s != 1 and s < 0.99999:
        print(s)
        print(i)



