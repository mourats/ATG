# coding: utf-8
import graph_functions

'''
 Aplicacoes de Teoria dos Grafos - Turma 02
 @author Thiago Santos de Moura - 116210967
 @author Caio Sanches Batista de Lira - 116210403 
 @author Marcelo Gabriel dos Santos Queiroz Vitorino - 116211290
 @author Gabriel Almeida Azevedo - 116210009
'''

# Código da função 1:
'''Função responsável por verficar se o passeio válido é uma trilha do grafo.'''
def is_trail(graph, valid_ride):
     
    '''Percorre a lista de arestas recebida.'''
    for edge in valid_ride:
		
        if type(edge) == tuple:
            inverse_edge = (edge[1] , edge[0])
       
        if type(edge) == str:
            inverse_edge = (edge[1] + edge[0])
            
		            
	'''Verifica se existe apenas uma aresta com o mesmo conjunto de vértices. Caso contrário, o passeio não é uma trilha.'''
        if (valid_ride.count(edge) + valid_ride.count(inverse_edge)) > 1:
            return False
           
    return True
    
# Código da função 2:
'''Função responsável por verficar se o passeio válido é uma trilha de Euler do grafo'''
def is_trail_euler (grafo,valid_ride):
 
	'''Armazena a lista de arestas do grafo'''
	temp_edges = graph_functions.edges(grafo)
 
	for edge in valid_ride:
		a,b = edge
		if set([a,b]) in temp_edges :
			temp_edges.remove(set([a,b]))
   
	ran_all_edges = temp_edges == []
	trail = is_trail(grafo,valid_ride)
   
	''' Se o passeio for uma trilha e passar por todos os vertices do grafo, então é uma trilha de Euler.'''
	return ran_all_edges and trail


# Código da função 3:
'''Função responsável por retornar a co-árvore da árvore em relação ao grafo recebido'''
def co_tree(graph,edges_tree):
	
	'''Armazena a lista de arestas do grafo'''
	graph_edges = graph_functions.edges(graph)

	for edge in edges_tree:
		
		if type(edge) == str:
			edge = (edge[0],edge[1])
			
		graph_edges.remove(set(edge))

	'''Retorna o conjunto de arestas restantes que representa a co-árvore.'''
	return graph_edges
 
 
graph = {"a" : ['b', 'c'],
         "b" : ['a', 'e'],
         "c" : ['a', 'f'],
         "d" : ['e', 'f' ],
         "e" : ['b', 'd', 'g'],
         "f" : ['c', 'd', 'g'],
         "g" : ['e', 'f']
        }
 
   
''' Realizando testes com as duas formas de representação de passeios válidos. '''
valid_ride1 = ['ac','cf','fd']
valid_ride2 = ['ed','df','fg','ge','ed']
valid_ride3 = ['ed','df','fg','ge','eb','ba']
valid_ride4 = ['ed','df','fg','ge','eb','ba','ac','cf']
valid_ride5 = []
 
valid_ride6 = [('a','c'),('c','f'),('f','d')]
valid_ride7 = [('e','d'),('d','f'),('f','g'),('g','e'),('e','d')]
valid_ride8 = [('e','d'),('d','f'),('f','g'),('g','e'),('e','b'),('b','a')]
valid_ride9 = [('e','d'),('d','f'),('f','g'),('g','e'),('e','b'),('b','a'),('a','c'),('c','f')]
valid_ride10 = []

arvore1 = [("a","b"),("a","c"),("c","f"),("f","g"),("b","e"),("e","d")]
arvore2 = [("a","b"),("a","c"),("c","f"),("b","e"),("e","d"),("e","g")]

arvore3 = ["ab","ac","cf","fg","be","ed"]
arvore4 = ["ab","ac","cf","be","ed","eg"]


   
# Testes função 01:            
assert(is_trail(graph, valid_ride1) == True)
assert(is_trail(graph, valid_ride2) == False)
assert(is_trail(graph, valid_ride3) == True)
assert(is_trail(graph, valid_ride4) == True)
assert(is_trail(graph, valid_ride5) == True)

assert(is_trail(graph, valid_ride6) == True)
assert(is_trail(graph, valid_ride7) == False)
assert(is_trail(graph, valid_ride8) == True)
assert(is_trail(graph, valid_ride9) == True)
assert(is_trail(graph, valid_ride10) == True)


# Testes função 02: 
assert(is_trail_euler(graph, valid_ride1) == False)
assert(is_trail_euler(graph, valid_ride2) == False)
assert(is_trail_euler(graph, valid_ride3) == False)
assert(is_trail_euler(graph, valid_ride4) == True)
assert(is_trail_euler(graph, valid_ride5) == False)

assert(is_trail_euler(graph, valid_ride6) == False)
assert(is_trail_euler(graph, valid_ride7) == False)
assert(is_trail_euler(graph, valid_ride8) == False)
assert(is_trail_euler(graph, valid_ride9) == True)
assert(is_trail_euler(graph, valid_ride10) == False)


# Testes função 03:
assert co_tree(graph, arvore1) == [set(['e','g']), set(['d','f'])]
assert co_tree(graph, arvore2) == [set(['d','f']), set(['f','g'])]

assert co_tree(graph, arvore3) == [set(['e','g']), set(['d','f'])]
assert co_tree(graph, arvore4) == [set(['d','f']), set(['f','g'])]
