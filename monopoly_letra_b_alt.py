from monopoly_letra_a import *
from random import randint

def proximoEstado(estado:int):
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
        
        for i in range(k):
            array.append(chave)

    novoEstado = array[randint(0, 35)]

    return novoEstado
    
def simulacao(t:int, estadoInicial=0):
    jogadas = [estadoInicial]
    jogadasExibicao=[str(estadoInicial)]

    contador = 0
    while contador < t:
        jogada = proximoEstado(jogadas[contador])
        if (jogada > 119):
            jogadasExibicao.append("20p" + ((jogada % 40) * "'") )
        else:
            jogadasExibicao.append(str(jogada%40) + ((jogada // 40) * "'") )
        jogadas.append(jogada)
        contador += 1
    return jogadasExibicao


def jogadasAtePrisao(simulacao):

    contador = 0
    preso = False

    for j in simulacao:
        if (str(j).find('p') != -1):
            preso = True
            break
        else:
            contador += 1

    return contador if preso == True else 0

