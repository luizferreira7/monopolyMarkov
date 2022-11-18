from monopoly_letra_b_alt import *

def matrizTransicao():

    matriz = np.zeros([123, 123])
    for i in range(0, 123):
        linha = linhaMatrizTransicao(i)
        matriz[i] = linha

    return matriz

def probablidadesAposTempo(t:int):
    m = matrizTransicao()

    posInicial = np.zeros([123])
    posInicial[0] = 1

    contador = 0
    while contador < t:
        posInicial = posInicial.dot(m)
        contador += 1

    r = []

    for i in range(0, 40):
        z1 = posInicial[i]
        z2 = posInicial[i+40]
        z3 = posInicial[i+80]

        z = z1 + z2 + z3

        if (i == 20):
            z += posInicial[120]
            z += posInicial[121]
            z += posInicial[122]

        r.append(z)

    return r


def posicaoZ(z, n=1000000):
    probs = probablidadesAposTempo(n)

    p = probs[z]

    return p

z = posicaoZ(39)

print(z)