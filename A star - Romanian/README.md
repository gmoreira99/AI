Busca com Informação: A*

Guilherme Moreira de Carvalho;
Laboratório de Inteligência Artificial - T02 (2023.1);
Prof. Rogerio Martins Gomes, DECOM - CEFET MG.

Representa a operação da busca A* aplicada ao problema de ir
de Arad a Bucareste usando a heurística de distância em linha reta;
Exibe a sequência de nós com menor custo que o algoritmo encontra e
a pontuação de f, g e h para cada nó.
 
Heuristicas:
	Arad;366
	Bucareste;0
	Craiova;160
	Drobeta;242
	Eforie;161
	Fagaras;176
	Giurgiu;77
	Hirsova;151
	Iasi;226
	Lugoj;244
	Mehadia;241
	Neamt;234
	Oradea;380
	Pitesti;100
	Rimnicu Vilcea;193
	Sibiu;253
	Timisoara;329
	Urziceni;80
	Vaslui;199
	Zerind;374
	
Grafo:
	Oradea;Zerind;71
	Oradea;Sibiu;151
	Zerind;Arad;75
	Arad;Sibiu;140
	Arad;Timisoara;118
	Timisoara;Lugoj;111
	Lugoj;Mehadia;70
	Mehadia;Drobeta;75
	Drobeta;Craiova;120
	Craiova;Rimnicu Vilcea;146
	Craiova;Pitesti;138
	Rimnicu Vilcea;Pitesti;97
	Rimnicu Vilcea;Sibiu;80
	Sibiu;Fagaras;99
	Fagaras;Bucareste;211
	Pitesti;Bucareste;101
	Bucareste;Giurgiu;90
	Bucareste;Urziceni;85
	Urziceni;Hirsova;98
	Hirsova;Eforie;86
	Urziceni;Vaslui;142
	Vaslui;Iasi;92
	Iasi;Neamt;87
