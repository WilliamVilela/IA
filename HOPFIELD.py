import numpy as np

# Definição das imagens conhecidas e desconhecida.

img1 = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
img2 = [1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1]
img3 = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1]
img4 = [-1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1]
img5 = [1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1]
img6 = [1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]
img7 = [-1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
img_desconhecida = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1]
imgEx = [img1, img2, img3, img4, img5, img6, img7]


# Numero de interações máximas realizadas
n_iteracoesmax = 10


#Função para inicializar a matriz
def inicializarMatriz():
    matriz = []

    for i in range(0,len(img_desconhecida)):

        linha = []

        for j in range(0,len(img_desconhecida)):
            linha.append(0)

        matriz.append(linha)

    return matriz

#Função para gerar os pesos da matriz, utilizando as imagens definidas no escopo, inicializa a matriz e realiza os calculos para gerar a matriz de peso.
def gerarPesosMatriz():
    padroes = [img1, img2, img3, img4, img5, img7]
    matrizPeso = inicializarMatriz()

    for i in range(0, len(matrizPeso[0])):
        for j in range(0, len(matrizPeso[i])):

            if j >= i:
                break

            soma = 0

            for k in range(0, len(padroes)):
                soma += (padroes[k][i] * padroes[k][j])

            matrizPeso[j][i] = matrizPeso[i][j] = soma

    return matrizPeso

#Função para treinamento utilizando a matriz de peso, temos como parametro pesos, imagem_desconhecida e contador, e verificando se converge ou não e mostrando na tela.
def treinar(pesos, img_desconhecida, contador):
    if contador == n_iteracoesmax:
        print("FALHOU")
        return

    contador += 1

    padraoY = [0 for i in range(len(img_desconhecida))]

    for i in range(0, len(pesos)):
        soma = 0

        for j in range(0, len(pesos[i])):
            soma += (img_desconhecida[j] * pesos[j][i])

        padraoY[i] = 1 if soma >= 0 else -1

    convergiu = False

    for i in range(0, len(imgEx)):
        convergiu = np.array_equal(padraoY, imgEx[i])

        if convergiu:
            break

    if not convergiu:
        treinar(pesos, padraoY, contador)
    else:
        print(f"\nCONVERGIU na {contador}ª vez")


if __name__ == '__main__':
    pesos = gerarPesosMatriz()
    contador = 0
    treinar(pesos, img_desconhecida, contador)
