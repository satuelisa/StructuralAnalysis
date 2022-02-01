import networkx as nx

# EDGE CREATION

# undirected graph, single edge
G = nx.Graph()
G.add_node('v')
G.add_node('w')
G.add_edge('v', 'w')
print('undirected', G.edges) # let us see the edge
# directed graph, two edges between a pair of nodes
G = nx.DiGraph() # directed graph
G.add_edge('v', 'w') # this edge is from v to w
print('directed', G.edges) # the printout looks the same, but this HAS an orientation
# multigraph, a double undirected edge
G = nx.MultiGraph() # multigraph
G.add_edge('v', 'w', key = 'a', weight = 2) # this one weighs two units
G.add_edge('v', 'w', key = 'b', weight = 5) # this one weighs five units
# these are a bit trickier to print in order to see the key and the weight
# G.edges() returns us triplets (x, y, z) where x and y are the vertices and z is the key
# using those triples, we can then query the graph to get the associated weight
print('multigraph', [ f"{x} {y} {z} {G[x][y][z]['weight']}" for (x, y, z) in G.edges ])

# COMPLETE GRAPH

Gm = nx.Graph() # build a complete graph manually, first
n = 7 # the desired graph order
for v in range(n): # vertices 0, 1, ..., 6
    for w in range(v + 1, n): # connected to all the others
         Gm.add_edge(v, w) # create the edge
m = Gm.size() # check the size of the resulting graph
print('Manual:', Gm)
assert 2 * m == n * (n - 1) # this invariant must hold
from networkx.generators.classic import complete_graph
Gl = complete_graph(n) # using a ready-made library routine
assert n == len(Gl) # number of vertices must match
assert m == Gl.size() # number of edges must also match
print('Library:', Gl)

# SMALL EXPERIMENT REGARDING COMPONENTS, PATHS, AND DIAMETERS

n = 23 # graph order
p = 0.07 # edge probability
from networkx.generators.random_graphs import erdos_renyi_graph
G = erdos_renyi_graph(n, p)
print(G)
# iterate over the connected components and make a list of the subgraphs
cc = [ G.subgraph(c) for c in nx.connected_components(G) ]
print(len(cc), 'components') # check how many there are
from networkx.algorithms.shortest_paths.generic import shortest_path

# this is a dictionary that gives for each vertex and each other vertex the sequence of vertex visits
sp = shortest_path(G, method='dijkstra')  
for subgraph in cc:
    if len(subgraph) > 2: # if it has more than two vertices
        diameter = None # we do not know this yet
        storage = None # this is where we will store the path that gives the diameter
        for v in subgraph: # iterate over its vertices
             for w in subgraph: # match them with all the others
                 if v > w: # do not check the pairs twice nor a vertex to itself
                     path = sp[v][w] # check the shortest path
                     l = len(path) - 1 # how many edges does it traverse? (vertices visited minus one)
                     if diameter is None or l > diameter: # if it is longer than what we have seen
                         diameter = l # update the longest seen thus far
                         storage = path # store it
        print(path) # let's see the path that defines the diameter of the component
