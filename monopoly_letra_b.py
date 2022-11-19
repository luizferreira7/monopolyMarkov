from random import randint
from monopoly_letra_a import *

duplas = [2, 4, 6, 8, 10, 12]

class Estado:
    def __init__(self, duplas, posicao, turnosCadeia, dados):
        self.duplas = duplas
        self.posicao = posicao
        self.turnosCadeia = turnosCadeia
        self.dados = dados
        self.status = 'Livre'
        self.exibicao = 'Dados: ' + str(dados) + ' -> ' + str(posicao) + ' ' + self.status

        if (duplas > 0):
            self.status = 'Quase Preso'

        if (turnosCadeia > 0):
            self.status = 'Preso'

    def update(self):
        if (self.duplas > 0):
            self.status = 'Quase Preso'
        elif (self.turnosCadeia > 0):
            self.status = 'Preso'
        else:
            self.status = 'Livre'

        if (self.posicao > 119):
            self.exibicao = 'Dados: ' + str(self.dados) + ' -> ' + "20p" + ((self.turnosCadeia % 40) * "*" + ' ' + self.status) 
        else:
            self.exibicao = 'Dados: ' + str(self.dados) + ' -> ' + str(self.posicao) + ((self.duplas) * "*") + ' ' + self.status
        

def jogarDados():
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    return (d1, d2)

def proximoEstado(estadoAtual:Estado, jogada:tuple):
    novoEstado = Estado(estadoAtual.duplas, estadoAtual.posicao, estadoAtual.turnosCadeia, jogada)

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
        else:
            if (jogada[0] == jogada[1]):
                novoEstado.duplas = 0
                novoEstado.turnosCadeia = 0
            else:
                novoEstado.turnosCadeia += 1

    novoEstado.posicao %= 40
    novoEstado.update()

    return novoEstado

def simulacao(t:int, estadoInicial=0):
    estadoInicial = Estado(0, 0, 0, (0,0))
    jogadas = [estadoInicial]
    jogadasExibicao=[estadoInicial.exibicao]

    contador = 1
    while contador < t:
        dados = jogarDados()
        jogada = proximoEstado(jogadas[contador-1], dados)
        jogadasExibicao.append(jogada.exibicao)
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


s = simulacao(10)
print(s[1])
# c = jogadasAtePrisao(s[0])
# print(c)