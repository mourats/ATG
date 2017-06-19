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
def is_trail(graph, valid_ride):
           
    for edge in valid_ride:
        if type(edge) == tuple:
            inverse_edge = (edge[1] , edge[0])
       
        if type(edge) == str:
            inverse_edge = (edge[1] + edge[0]) 
   
        if (valid_ride.count(edge) + valid_ride.count(inverse_edge)) > 1:
            return False
           
    return True
    
# Código da função 2:
def is_trail_euler (grafo,valid_ride):
 
    temp_edges = graph_functions.edges(grafo)
 
    for edge in valid_ride:
        a,b = edge
        if set([a,b]) in temp_edges :
            temp_edges.remove(set([a,b]))
   
    ran_all_edges = temp_edges == []
    trail = is_trail(grafo,valid_ride)
   
    return ran_all_edges and trail
    
 
 
graph = {"a" : ['b', 'c'],
         "b" : ['a', 'e'],
         "c" : ['a', 'f'],
         "d" : ['e', 'f' ],
         "e" : ['b', 'd', 'g'],
         "f" : ['c', 'd', 'g'],
         "g" : ['e', 'f']
        }

'''Falta testar com esse grafo.'''       
graph2 = {"1" : ['2'],
          "2" : ['1', '3'],
          "3" : ['2', '4'],
          "4" : ['3']
         }
 
   
''' Realizando testes com as duas formas de representação de passeios válidos '''
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

