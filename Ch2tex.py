# this controls whether the manually adjusted figures will be
# overwritten or not
redo = False 

# import libraries

# obtain from https://github.com/johnyf/nx2tikz and install manually (with some changes to match the present version of NetworkX)

import nx2tikz 

# install using pip on a local computer (colab has it preinstalled)
import networkx as nx 

# edge drawings

G = nx.Graph() # create an undirected graph
G.add_edge('v', 'w') # create a single edge
with open('undirected_edge.tex', 'w') as target:
    target.write(nx2tikz.dumps_tikz(G))
G = nx.DiGraph() # directed graph
G.add_edge('v', 'w') # this edge is from v to w
with open('directed_edges.tex', 'w') as target:
    target.write(nx2tikz.dumps_tikz(G))
G = nx.MultiGraph() # multigraph
G.add_edge('v', 'w', key = 'a', weight = 2) # this one weighs two units
G.add_edge('v', 'w', key = 'b', weight = 5) # this one weighs five units
if redo:
    with open('multiedge.tex', 'w') as target: 
        target.write(nx2tikz.dumps_tikz(G))
# the edge drawings need some manual work in order to not overlap
# edit multiedge.tex as follows for the effect shown in the book:
# v -- [edge label=b, bend left=10, thick]w;
# v -- [edge label=a, bend right=10]w;

# complete graphs

from networkx.generators.classic import complete_graph
for n in range(3, 8, 2):
    with open(f'k{n}.tex', 'w') as target: 
        target.write(nx2tikz.dumps_tikz(complete_graph(n)))    

# the component-diameter experiment

n = 23 # graph order
p = 0.07 # edge probability
from networkx.generators.random_graphs import erdos_renyi_graph
Gnp = erdos_renyi_graph(n, p)
cc = [ Gnp.subgraph(c) for c in nx.connected_components(Gnp) ]
from networkx.algorithms.shortest_paths.generic import shortest_path
sp = shortest_path(Gnp, method='dijkstra')
color = None
options = [ 'cyan', 'orange', 'teal', 'olive', 'pink', 'yellow', 'lime', 'violet', 'lightgray' ]
palette = dict()
diams = set()
if len (cc) > len(options):
    print('% Colors may run out')
count = 0
for subgraph in cc:
    if len(subgraph) > 2: # if it has more than two vertices
        count += 1
        if len(options) > 0:
            color = options.pop(0) 
        diameter = None # we do not know this yet
        storage = None # this is where we will store the path that gives the diameter
        for v in subgraph: # iterate over its vertices
             palette[v] = color
             for w in subgraph: # match them with all the others
                 if v > w: # do not check the pairs twice nor a vertex to itself
                     path = sp[v][w] # check the shortest path
                     l = len(path) - 1 
                     if diameter is None or l > diameter: 
                         diameter = l # update the longest seen thus far
                         storage = path # store it
        v = storage.pop(0)
        while len(storage) > 0:
            w = storage.pop(0)
            diams.add((v, w)) # this edge lies along a diameter
            v = w
from nx2fig import fig
# draw the components using colors, make the diameter edges thicker
if redo:
    fig(Gnp, palette, diams, 'comp.tex') 
print(count, 'component(s) of order above two')
