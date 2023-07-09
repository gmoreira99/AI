"""Guilherme Moreira de Carvalho 13/04/2023 - Para Laboratório de Inteligência Artificial, 2023/1"""
"""A* search - Romanian Map (Arad -> Bucareste)"""

class No:
		nome = None
		pai = None

		def __init__ (self, nome, pai):
			self.nome = nome
			self.pai = pai

def busca (origem, destino, heuristica, grafo):
	folhas = {}		# nós abertos
	visitados = {}	# nós visitados
	custo = 0		# custo acumulado do percurso
	caminho = []	# percurso

	pos = No(origem, None)	# posição atual
	pai = None				# posição anterior

	folhas[pos] = heuristica[pos.nome]	# abre primeiro nó (raíz/origem)

	"""
	enquanto houver nós abertos
		seleciona o nó de menor f(n) = g(n) + h(n)
		calcula o custo de alcançar o nó
		- exhib
		visita/processa o nó
		se alcançar o destino -> fim
		senão, abre nós adjacentes ao atual
	"""
	while len(folhas) > 0:
		pos = min(folhas, key=folhas.get)
		custo = folhas[pos] - heuristica[pos.nome]

		for no in folhas:	# exibição do passo a passo
			print("[", no.nome, ":", folhas[no], "]", end=" ")
		print("\nGO TO >", pos.nome, "\n")

		visitados[pos] = folhas[pos]
		folhas.pop(pos)
		pai = pos

		if pos.nome == destino:	# construção do resultado final
			caminho.append(pos.nome)
			while (pos.nome != origem):
				pos = pos.pai
				caminho.insert(0, pos.nome)
			break

		for adj in grafo[pos.nome]:	# para cada adjacência da posição atual
			skip = False
			for vis in visitados:
				if (adj[0] == vis.nome):
					skip = True
					break
			if (not skip):	# se já não tiver sido visitado
				aux = No(adj[0], pai)
				folhas[aux] = heuristica[adj[0]] + adj[1] + custo	# abre adjacência
							# heuristica + custo [A->B] + custo acumulado

	return caminho

if __name__ == "__main__":
	# leitura do arquivo de heuristicas
	heuristica = {}
	f = open("Heuristica.txt","r")
	for linha in f:
		valores = linha.split(";")
		heuristica[valores[0]] = int(valores[1])
	f.close()
	
	# leitura do arquivo de conexões
	grafo = {}
	f = open("Grafo.txt", "r")
	for linha in f:
		valores = linha.split(";")
		valores[2] = int(valores[2])
		# Se origem e destino são conhecidos, atualiza as conexões de ambos
		if valores[0] in grafo and valores[1] in grafo:
			aux = grafo[valores[0]]
			aux.append([valores[1], valores[2]])
			grafo[valores[0]] = aux
			aux = grafo[valores[1]]
			aux.append([valores[0], valores[2]])
			grafo[valores[1]] = aux
		# Se origem/destino é conhecido, atualiza suas conexões e adiciona destino/origem 	
		elif valores[0] in grafo:
			aux = grafo[valores[0]]
			aux.append([valores[1], valores[2]])
			grafo[valores[0]] = aux
			grafo[valores[1]] = [[valores[0], valores[2]]]
		elif valores[1] in grafo:
			aux = grafo[valores[1]]
			aux.append([valores[0], valores[2]])
			grafo[valores[1]] = aux
			grafo[valores[0]] = [[valores[1], valores[2]]]
		# Adiciona origem e destino
		else:
			grafo[valores[0]] = [[valores[1], valores[2]]]
			grafo[valores[1]] = [[valores[0], valores[2]]]
	f.close()

	"""for cidade in grafo:
		print("Cidade :", cidade)
		print("Vizinhos :", grafo[cidade])
		print("Heuristica :", heuristica[cidade])"""
		
	caminho = busca("Arad", "Bucareste", heuristica, grafo)
	print("Caminho > ", caminho)