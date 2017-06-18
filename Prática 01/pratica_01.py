import graph_functions

'''
 Aplicacoes de Teoria dos Grafos - Turma 02
 @author Thiago Santos de Moura - 116210967
 @author Caio Sanches Batista de Lira - 116210403 
 @author Marcelo Gabriel dos Santos Queiroz Vitorino - 116211290
 @author Gabriel Almeida Azevedo - 116210009
'''

def is_complete(graph):
	
	'''prova que eh um grafo simples'''
	for vertex in graph: 
		'''verifica loop's'''
		if vertex in graph[vertex]:
			return False 

	'''adquire a quantidade de vertices adjacentes de todos os vertices'''
	total_vertex_neighbour = len(graph) - 1  
	
	'''prova que todos os vertices sao adjacentes a todos'''
	for vertex in graph:
		if graph_functions.vertex_degree(vertex,graph)!= total_vertex_neighbour: 
			return False
       
	return True
  
  
def is_subgraph(graph, sub_graph):
	
	'''guarda os vertices do grafo principal'''
	vertices_graph = graph_functions.vertices(graph) 
	
	'''guarda as arestas do grafo principal'''
	arestas_graph = graph_functions.edges(graph) 
  
	'''prova que todos os vertices do sub grafo testado existem no grafo principal'''
	for vertice in sub_graph:
		if vertice not in vertices_graph: 
			return False
			
	'''prova que todos as arestas do sub grafo testado existem no grafo principal'''       
	for edges in graph_functions.vertices(sub_graph):
		if set(sub_graph[edges]) not in arestas_graph:
			return False      
  
	return True
      

def edge_cut(graph, X):
	
	''' iniciando conjunto de arestas resultantes'''
	cut_result = [] 
	
	'''percorre os vertices de X'''
	for vertice in X:
		'''percorre todas as arestas do grafo''' 
		for edge in graph_functions.edges(graph):
			'''verifica se aresta contem o vertice cortado e nao eh loop'''
			if vertice in edge and len(edge) == 2:
				'''analisa os dois vertices da aresta da vez'''
				for possible in edge:
					'''caso o segundo vertice nao esteja no X, a aresta eh adicionada'''
					if possible != vertice and possible not in X: 
						cut_result.append(edge)
			
	return cut_result



grafo01 = { "1" : ["1","2","3"],
			"2" : ["1","4","5"],
			"3" : ["1"],
			"4" : ["2"],
			"5" : ["2"],
		  }

grafo02 = { "a" : ["b", "d", "e", "f"],
			"b" : ["a", "c", "e"],
			"c" : ["b", "d", "e"],
			"d" : ["a", "c"],
			"e" : ["c","a", "b"],
			"f" : ["a"]
		  }
		  
grafo03 = { "1" : ["4"],
			"2" : ["3"],
			"3" : ["2", "3", "4", "5"],
			"4" : ["1", "3"],
			"5" : ["3"],
			"6" : []
		  }

grafo04 = { "a" : ["b", "c", "d", "e", "f"],
			"b" : ["a", "c", "d", "e", "f"],
			"c" : ["b", "a", "d", "e", "f"],
			"d" : ["b", "c", "a", "e", "f"],
			"e" : ["b", "c", "d", "a", "f"],
			"f" : ["b", "c", "d", "e", "a"]
		  }

grafo05 = { "a" : ["b", "c"],
			"b" : ["a", "c"],
			"c" : ["b", "a"],
		  }

X = ["1","2"]
Y = ["c", "d", "e"]

'''Testando funcao edge_cut()'''
assert(edge_cut(grafo01, X) == [set(['1', '3']), set(['2', '4']), set(['2', '5'])])
assert(edge_cut(grafo02, Y) == [set(['c', 'b']), set(['a', 'd']), set(['a', 'e']), set(['b', 'e'])])

'''Testando funcao is_complete()'''
assert(is_complete(grafo01) == False)
assert(is_complete(grafo05) == True)
assert(is_complete(grafo03) == False)
assert(is_complete(grafo04) == True)

'''Testando funcao is_subgraph()'''
assert(is_subgraph(grafo04, grafo05) == True)
assert(is_subgraph(grafo04, grafo02) == False)
assert(is_subgraph(grafo03, grafo01) == False)
