import numpy as np
from random import randint

duplas = [2, 4, 6, 8, 10, 12]

class Estado:
    def __init__(self, duplas, posicao, turnosCadeia):
        self.duplas = duplas
        self.posicao = posicao
        self.turnosCadeia = turnosCadeia

def jogarDados():
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    return (d1, d2)

def proximoEstado(estadoAtual:Estado, jogada:tuple):
    novoEstado = Estado(estadoAtual.duplas, estadoAtual.posicao, estadoAtual.turnosCadeia)

    if (estadoAtual.turnosCadeia == 0):
        if (novoEstado.duplas == 2):
            if (jogada[0] == jogada[1]):
                novoEstado.duplas = 0
                novoEstado.posicao = 20
                novoEstado.turnosCadeia += 1
            else:
                novoEstado.duplas = 0
                novoEstado.posicao += (jogada[0] + jogada[1])
        else:
            if (jogada[0] == jogada[1]):
                novoEstado.duplas += 1
            else:
                novoEstado.duplas = 0
                novoEstado.posicao += (jogada[0] + jogada[1])
    else:
        if (estadoAtual.turnosCadeia == 3):
            novoEstado.duplas = 0
            novoEstado.turnosCadeia = 0
            novoEstado.posicao += (jogada[0] + jogada[1])
        else:
            if (jogada[0] == jogada[1]):
                novoEstado.duplas = 0
                novoEstado.turnosCadeia = 0
            else:
                novoEstado.turnosCadeia += 1

    if (novoEstado.posicao > 39):
        novoEstado.posicao = novoEstado.posicao%40

    return novoEstado

def jogada(t):
    estadoInicial = Estado(0, 0, 0)

    dados = jogarDados()

    novoEstado = proximoEstado(estadoInicial, dados)
    print('Jogada 1:', dados, novoEstado.posicao+(novoEstado.duplas * 40))

    print('-----------------------------------------')

    contador = 1
    while (contador != t):
        dados = jogarDados()
        novoEstado = proximoEstado(novoEstado, dados)
        print('Jogada ' + str(contador+1) + ':', 'Dados: ' + str(dados), 'Posição: ' + str(novoEstado.posicao+(novoEstado.duplas * 40)), 'Quase preso!' if novoEstado.duplas == 2 else '', 'Preso!' if novoEstado.turnosCadeia != 0 else '')
        print('-----------------------------------------')
        contador += 1

jogada(1000)
