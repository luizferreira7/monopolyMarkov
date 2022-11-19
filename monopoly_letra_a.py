import numpy as np
from fractions import Fraction
from functools import lru_cache, wraps

def cache(f):

    def g(*args):
        if args not in g.cache:
            g.cache[args] = f(*args)
        return g.cache[args]
    g.cache = {}
    g.__doc__  = f.__doc__
    g.__name__ = f.__name__
    return g

def np_cache(function):
    @lru_cache()
    def cached_wrapper(hashable_array):
        array = np.array(hashable_array)
        return function(array)

    @wraps(function)
    def wrapper(array):
        return cached_wrapper(tuple(array))

    wrapper.cache_info = cached_wrapper.cache_info
    wrapper.cache_clear = cached_wrapper.cache_clear

    return wrapper

@cache
def linhaMatrizTransicao(linha):

    linhaMarkov = np.zeros([123])

    probsCasas = [0, 0, 0, 1/18, 1/18, 1/9, 1/9, 1/6, 1/9, 1/9, 1/18, 1/18, 0]

    if (linha <= 119):
        linhaAux = linha % 40

        for i, p in enumerate(probsCasas):
            if (i + linhaAux > 39):
                linhaMarkov[(linhaAux+i)%40] = p
            else:
                linhaMarkov[linhaAux+i] = p

        if (linha < 80):
            linhaMarkov[linha + 40] = 1/6

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

    print('Linha do estado ' + str(estado))
    print(''.join(['{:6}'.format('' + str(item) + '  ') for item in range(0, 123)]))
    print(''.join(['{:6}'.format(item) for item in linhaAux]))

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


imprimeLinhaMatriz(0)
