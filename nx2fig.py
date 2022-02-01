def fig(G, color, highlight, filename):
    with open(filename, 'w') as target:
        print('\\begin{tikzpicture}', file = target)
        print('\\graph[spring layout, sibling distance=5.0cm,edges={nodes={sloped, inner sep=10pt}}, nodes={circle, draw}]{', file = target)
        for vertex in G:
            if vertex not in color:
                print(f'{vertex}[as={{{vertex}}}];', file = target)
            else:
                print(f'{vertex}[as={{{vertex}}},fill={color[vertex]}];', file = target)            
        for (s, t) in G.edges():
            if (s, t) in highlight or (t, s) in highlight:
                print(f'{s} -- [ultra thick]{t};', file = target)
            else:
                print(f'{s} -- {t};', file = target)            
        print('};', file = target)
        print('\\end{tikzpicture})', file = target)
