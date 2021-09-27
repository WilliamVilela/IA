import numpy as np

# Define o número de épocas (alterar caso não aprenda) e o número de amostras (q)
numEpocas = 20000 
q = 6


# Atributos utilizados peso e ph ficiticios
peso = np.array([113, 122, 107, 98, 115, 120])
ph = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

#Bias 
bias = 1

# Entrada do perceptron 
X = np.vstack((peso, ph))
Y = np.array([-1, 1, -1, -1, 1, 1])

# Taxa de aprendizado 
eta = 0.1

# Define o vetor de pesos
W = np.zeros([1, 3])                             # Duas entradas + baia

# Array para armazenarar os erros 
e = np.zeros(6)

def funcaoAtivacao(valor):
	# A função de ativação degrau bipolar
	if valor < 0.0:
		return(-1)
	else:
		return(1)

# Parte principal, repetição de treinamento com numEpocas e para cada um dos vetores 

for j in range(numEpocas):
    for k in range(q):
	# Insere o bias no vetor de entrada
        Xb = np.hstack((bias, X[:,k]))

	# Calcula o campo induzido com equação vetorial
        V = np.dot(W, Xb)
	# Calcular a saída do perceptron
        Yr = funcaoAtivacao(V)    
	#Calcula o erro: e = (Y - Yr)
        e[k] = Y[k] - Yr
	#Treinamento do perceptron
        W = W + eta*e[k]*Xb
print("Vetor de erros (e) = "+ str(e)) 

