import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
G = nx.barbell_graph(5, 1)
plt.figure(1, figsize=(5, 5))
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
sorted(map(sorted, next_level_communities))
pos=nx.spring_layout(G)
nx.draw_networkx(G, pos, node_size=500, edge_color='Aqua', with_labels=True, font_color='Black', node_color='Red')
