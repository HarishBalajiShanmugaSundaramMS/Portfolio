import matplotlib.pyplot as plt
import networkx as nx
G = nx.house_graph()
# explicitly set positions
pos = {0: (0, 0),
       1: (1, 0),
       2: (0, 1),
       3: (1, 1),
       4: (0.5, 2.0)}
nx.draw_networkx_nodes(G, pos, node_size=200, nodelist=[4])
nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=[0, 1, 2, 3], node_color='b')
nx.draw_networkx_edges(G, pos, width=3, edge_color='aqua')
plt.axis('off')
plt.show()