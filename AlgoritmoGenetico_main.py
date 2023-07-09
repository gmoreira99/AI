# Guilherme Moreira de Carvalho, para Lab de IA 2023/1
# Algoritmos Genéticos

import math
import random
import numpy as np
import matplotlib.pyplot as plt

best = []   # melhor individuo da população
worst = []  # pior individuo
mean = []   # média dos individuos

# função alpine + 6 (f(X) > 0)
def alpine(X):
    res = 1
    for i in X:
        res *= math.sqrt(i)*math.sin(i)
    return res + 6

def fitness(pop):

    fit = []    # fitness de cada individuo (x1, x2)
    for i in range(len(pop)) :
        fit.append(alpine(pop[i]))

    fit.sort()  # ordenação do resultado
                # objetivo = max(alpine) + 6 = 7.88 + 6 = 13.88

    global best, worst, mean
    best.append(fit[-1])
    worst.append(fit[0])
    mean.append(np.mean(fit))

    # construção da roleta
    for i in range(1, len(pop)):
        fit[i] = fit[i] + fit[i-1]
    fit = np.divide(fit, fit[-1])

    # seleção dos pais
    parents = []
    for i in range(len(pop)):
        x = random.uniform(0, 1)
        for j in range(len(pop)):
            # qual a posição na roleta do valor aleatório gerado
            if x <= fit[j]:
                parents.append(j)
                break

    return parents

def crossover(p1, p2, tax_cross):
    a = random.uniform(0, 1)
    if a > tax_cross:
        return p1, p2

    else:
        x1 = a*p1[0] + (1-a)*p2[0]
        x2 = a*p1[1] + (1-a)*p2[1]
        o1 = [x1, x2]

        x1 = (1-a)*p1[0] + a*p2[0]
        x2 = (1-a)*p1[1] + a*p2[1]
        o2 = [x1, x2]

        return o1, o2

def mutation(pop, genes, tax_mutat):
    for i in range(len(pop)):
        for j in range(genes):
            if random.uniform(0, 1) < tax_mutat:
                x = random.uniform(pop[i][j]*(1-tax_mutat), pop[i][j]*(1+tax_mutat))
                if x >= 10.0: pop[i][j] = 10.0  # limites de xi da função alpine
                elif x <= 0.0: pop[i][j] = 0.0
                else: pop[i][j] = x

def plot(gen):
    global best, worst, mean
    x = np.linspace(1, gen, len(best))
    plt.plot(x, best, label='Melhor')
    plt.plot(x, mean, '--', label='Média')
    plt.plot(x, worst, label='Pior')
    plt.scatter(x[-1], best[-1], c='red', marker='D', label=best[-1])
    # melhor ponto encontrado

    plt.title('Evolução')
    plt.xlabel('Geração')
    plt.ylabel('Alpine')
    plt.legend()

    plt.show()

if __name__ == "__main__":

    pop_size = 150   # tamanho da população
    gen = 50    # quantidade de gerações
    genes = 2   # quantidade de genes em um individuo (x1, x2)

    tax_cross = 0.75    # taxa de crossover
    tax_mutat = 0.05    # taxa de mutação

    # população inicial
    pop = ([[random.uniform(0, 10) for j in range(genes)] for i in range(pop_size)])

    for i in range(gen):

        # seleção dos pais pelo método da roleta
        parents = fitness(pop)

        # criação da nova população por crossover aritmético
        new_pop = []
        for j in range(0, pop_size, 2):
            o1, o2 = crossover(pop[parents[j]], pop[parents[j+1]], tax_cross)
            new_pop.append(o1)
            new_pop.append(o2)

        # mutação
        mutation(new_pop, genes, tax_mutat)

        pop = new_pop

    plot(gen)