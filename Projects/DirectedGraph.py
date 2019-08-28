# =======================================
# Title:  Networkx Directed Graph
# Author: HarishBalaji ShanmugaSundaram
# Date:   24 August 2019
# =======================================

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('A', 'D')])

plt.figure(figsize=(5, 5))
plt.axis('off')
pos = nx.circular_layout(G)

directedEdges = [('A', 'B'), ('C', 'D')]
undirectedEdges = [('B', 'C'), ('D', 'A')]

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_size=500, edgelist=directedEdges,
                 edge_color='aqua', arrows=True, withLabels=True, width=3)
nx.draw_networkx_edges(G, pos, edgelist=undirectedEdges,
                       arrows=False, edge_color='aqua', width=2)
plt.show()
