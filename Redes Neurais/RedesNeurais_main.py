# Guilherme Moreira de Carvalho, para Lab de IA 2023/1
# Redes Neurais: Implementação do algoritmo perceptron

import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt

def step(X):
    for i, x in enumerate(X):
        if (x < 0):
            X[i] = 0
        else:
            X[i] = 1

def sig(X):
    max_x = max(X)
    for i, x in enumerate(X):
        if x == max_x:
            X[i] = 1
        else:
            X[i] = 0

# treinamento do modelo
def perceptron_fit(X, D, max_it=100, tax_apr=0.1, func="sig"):

    # matriz e vetor, respectivamente, de pesos e bias aleatórios
    W = [[0]*len(X.columns) for i in range(len(D[0]))]
    for j in range(len(X.columns)):
        for i in range(len(D[0])):
            W[i][j] = round(random.uniform(-1, 1), 1)
    b = [ round(random.uniform(0, 1), 1) for _ in range(len(D[0])) ]

    t = 0    # época
    E = 1    # erro acumulado de uma época
    err = [] # erros de cada época

    while (t < max_it and E > 0):
        E = 0
        for i in range(len(X)):
            y = [0, 0, 0] # saída
            e = [0, 0, 0] # erro de uma instância

            # para cada instância (linha da matriz X)
            for j, x in enumerate(X.iloc[i]):
                for k in range(len(y)):
                    y[k] += W[k][j]*x
            for k in range(len(y)):
                y[k] = y[k]+b[k]

            if func == "sig":
                sig(y)
            else:
                step(y)

            for j in range(len(e)):
                e[j] = D[i][j] - y[j]

            for j, x in enumerate(X.iloc[i]):
                for k in range(len(b)):
                    W[k][j] += tax_apr*e[k]*x
                    b[k] += tax_apr*e[k]

            for j in range(len(e)):
                E += math.pow(e[j], 2)

        err.append(E)
        t += 1

    x = np.linspace(1, t, len(err))
    plt.plot(x, err)
    plt.title('Treinamento')
    plt.xlabel('Epoca')
    plt.ylabel('Erro')

    return W, b

# teste do modelo
def perceptron_test(X, D, W, b, func="sig"):
    tax_hit = 0 # taxa de acerto
    for i in range(len(X)):
        E = 0 # erro de uma instância
        y = [0, 0, 0]
        e = [0, 0, 0]

        for j, x in enumerate(X.iloc[i]):
            for k in range(len(y)):
                y[k] += W[k][j]*x
        for k in range(len(y)):
            y[k] = y[k]+b[k]

        if func == "sig":
            sig(y)
        else:
            step(y)

        for j in range(len(e)):
            e[j] = D[i][j] - y[j]
            E += math.pow(e[j], 2)
        if E == 0:
            tax_hit += 1

    tax_hit /= len(X)
    print("Taxa Acerto (Teste):", tax_hit)

if __name__ == "__main__":

    # preparo dos dados    
    dados = pd.read_csv("Iris_Data.csv")

    # 30% dos dados mantendo proporção de classes alvo (species)
    amostra = dados.groupby("species").sample(frac=0.3, random_state=1)
    amostra = amostra.sample(frac=1) # embaralha

    X_fit = amostra[amostra.columns[0:4]] # atributos
    D_fit = amostra["species"]  # alvo
    D_fit = D_fit.values.tolist()
    for i, d in enumerate(D_fit): # binarização das classes alvo
        if d == "Iris-setosa":
            D_fit[i] = [0, 0, 1]
        elif d == "Iris-versicolor":
            D_fit[i] = [0, 1, 0]
        else:
            D_fit[i] = [1, 0, 0]

    X_test = dados[dados.columns[0:4]]
    D_test = dados["species"]
    D_test = D_test.values.tolist()
    for i, d in enumerate(D_test):
        if d == "Iris-setosa":
            D_test[i] = [0, 0, 1]
        elif d == "Iris-versicolor":
            D_test[i] = [0, 1, 0]
        else:
            D_test[i] = [1, 0, 0]

    W, b = perceptron_fit(X_fit, D_fit)
    perceptron_test(X_test, D_test, W, b)

    plt.show()