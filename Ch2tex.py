import nx2tikz # obtain from https://github.com/johnyf/nx2tikz and install manually
import networkx as nx # install using pip on a local computer (colab has it)
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
with open('multiedge.tex', 'w') as target: 
    target.write(nx2tikz.dumps_tikz(G))
# the edge drawings need some manual work in order to not overlap
# edit multiedge.tex as follows for the effect shown in the book:
# v -- [edge label=b, bend left=10, thick]w;
# v -- [edge label=a, bend right=10]w;

