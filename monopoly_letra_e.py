from monopoly_letra_b_alt import *

def matrizTransicao():

    matriz = np.zeros([123, 123])
    for i in range(0, 123):
        linha = linhaMatrizTransicao(i)
        matriz[i] = linha

    return matriz

def probablidadesAposTempo(t:int):
    m = matrizTransicao()

    posicao = np.zeros([123])
    posicao[0] = 1

    contador = 0
    while contador < t:
        posicao = posicao.dot(m)
        contador += 1

    probablidades = []

    for i in range(0, 123):
        z = posicao[i]

        if (i >= 40 and i < 120):
            probablidades[i%40] += z
        elif (i >= 120):
            probablidades[20] += z
        else:
            probablidades.append(z)

    return probablidades

def posicaoZ(z, n=1000000):
    probs = probablidadesAposTempo(n)

    p = probs[z]

    return p

z = posicaoZ(20, 100000)

print(z)