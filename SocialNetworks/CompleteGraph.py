import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
plt.figure(figsize=(5, 5))
plt.axis('off')
pos = nx.circular_layout(G)

nx.draw_networkx(G, pos, edge_color='Aqua')
plt.show()
