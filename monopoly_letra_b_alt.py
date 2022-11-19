from monopoly_letra_a import *
from random import randint

@cache
def probablidades(estado:int):

    linhaMatriz = linhaMatrizTransicao(estado)

    estadosPossiveis = dict()

    for i, p in enumerate(linhaMatriz):
        if (p != 0):
            estadosPossiveis[i] = p

    array = []

    for chave in estadosPossiveis:
        probabilidade = Fraction(estadosPossiveis.get(chave)).limit_denominator()
        k = probabilidade.numerator
        if (probabilidade.denominator != 36):
            k = (36//probabilidade.denominator) * probabilidade.numerator
        
        array.extend([chave]*k)

    return array

def proximoEstado(estado:int):
    
    probs = probablidades(estado)

    novoEstado = probs[randint(0, 35)]

    return novoEstado

def simulacao(t:int, imprimir=True, estadoInicial=0):
    jogadas = [estadoInicial]
    jogadasExibicao=[str(estadoInicial)]

    contador = 1
    while contador < t:
        jogada = proximoEstado(jogadas[contador-1])
        if (imprimir == True):
            if (jogada > 119):
                jogadasExibicao.append("20p" + ((jogada % 40) * "*") )
            else:
                jogadasExibicao.append(str(jogada%40) + ((jogada // 40) * "*") )
        jogadas.append(jogada)
        contador += 1

    if (imprimir == True):
        print(jogadasExibicao)

    return jogadas

s = simulacao(1000000, False)