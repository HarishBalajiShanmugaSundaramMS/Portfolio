import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
plt.figure(1, figsize=(5, 5))
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,2)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_size=500, edge_color='Aqua', 
with_labels=True, font_color='Black', node_color='Red')
print(nx.shortest_path(G))

{1: {1: [1], 2: [1, 2], 3: [1, 2, 3], 5: [1, 2, 5], 4: [1, 2, 3, 4]}, 
 2: {2: [2], 1: [2, 1], 3: [2, 3], 5: [2, 5], 4: [2, 3, 4]}, 
 3: {3: [3], 2: [3, 2], 4: [3, 4], 1: [3, 2, 1], 5: [3, 2, 5]}, 
 4: {4: [4], 3: [4, 3], 5: [4, 5], 2: [4, 3, 2], 1: [4, 3, 2, 1]}, 
 5: {5: [5], 4: [5, 4], 2: [5, 2], 3: [5, 4, 3], 1: [5, 2, 1]}}
