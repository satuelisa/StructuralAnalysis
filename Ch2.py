import networkx as nx
# undirected graph, single edge
G = nx.Graph()
G.add_node('v')
G.add_node('w')
G.add_edge('v', 'w')
print('undirected', G.edges)
# directed graph, two edges between a pair of nodes
G = nx.DiGraph() # directed graph
G.add_edge('v', 'w') # this edge is from v to w
print('directed', G.edges)
# multigraph, a double undirected edge
G = nx.MultiGraph() # multigraph
G.add_edge('v', 'w', key = 'a', weight = 2) # this one weighs two units
G.add_edge('v', 'w', key = 'b', weight = 5) # this one weighs five units
print(G.edges)
print('multigraph', [ f"{a} {b} {c} {G[a][b][c]['weight']}" for (a, b, c) in G.edges ])

