import graph_functions

def co_tree(edges_graph,edges_tree):

	for i in range(len(edges_graph) -1, -1,-1):

		# verifies if the element on edges_graph also is on the edges_tree list.

		if str(edges_graph[i]) in edges_tree:

			# remove the repeated element of edges graph list.

			edges_graph.pop(i)



	return edges_graph

	

g = { "A" : ["B","C"],
	  "B" : ["A","E"],
	  "C" : ["A","F"],
	  "D" : ["E","F"],
	  "E" : ["B","D","G"],
	  "F" : ["C","D","G"],
	  "G" : ["E","F"]
}



t = [("A","B"),("A","C"),("C","F"),("F","G"),("B","E"),("E","D")]



new_t = []

for i in range(len(t)):

	new_t.append(str(set(t[i]))) 



assert co_tree(graph_functions.edges(g),new_t) == [set(['E', 'G']), set(['D', 'F'])]







g1 = { "A" : ["B","C"],

"B" : ["A","E"],

"C" : ["A","F"],

"D" : ["E","F"],

"E" : ["B","D","G"],

"F" : ["C","D","G"],

"G" : ["F","E"]

}



t1 = [("A","B"),("A","C"),("C","F"),("B","E"),("E","D"),("E","G")]



new_t1 = []

for i in range(len(t1)):

	new_t1.append(str(set(t1[i])))



assert co_tree(graph_functions.edges(g1),new_t1) == [set(['D', 'F']), set(['F', 'G'])]
