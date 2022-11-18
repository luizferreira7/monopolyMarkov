from random import randint
from monopoly_letra_a import *

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

@cache
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

    return novoEstado

def simulacao(t:int, estadoInicial=0):
    estadoInicial = Estado(0, 0, 0)
    jogadas = [estadoInicial]
    jogadasExibicao=[estadoInicial.posicao]

    contador = 1
    while contador < t:
        dados = jogarDados()
        jogada = proximoEstado(jogadas[contador-1], dados)
        if (jogada.posicao > 119):
            jogadasExibicao.append("20p" + ((jogada.posicao % 40) * "'") )
        else:
            jogadasExibicao.append(str(jogada.posicao%40) + ((jogada.posicao // 40) * "'") )
        jogadas.append(jogada)
        contador += 1

    return (jogadas, jogadasExibicao)

@np_cache
def jogadasAtePrisao(simulacao):

    contador = 0
    preso = False

    for j in simulacao:
        if (j.posicao == 120):
            preso = True
            break
        elif (j.posicao < 40):
            contador += 1

    return contador if preso == True else 0


# s = simulacao(10000)
# c = jogadasAtePrisao(s[0])
# print(c)