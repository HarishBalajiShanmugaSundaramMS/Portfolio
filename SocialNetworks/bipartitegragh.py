import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite
G = nx.path_graph(4)
c = bipartite.color(G)
pos=nx.circular_layout(G)
nx.set_node_attributes(G, c, 'bipartite')
nx.draw_networkx(G, pos, width=3,edge_color='aqua')
print(c)