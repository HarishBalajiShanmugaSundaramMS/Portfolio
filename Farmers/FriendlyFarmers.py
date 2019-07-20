# Shows Friendly Farmers
import csv
import os
import os.path

import imageio
import imageio.plugins.pillow
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

dir = r'/Users/harishbalaji/documents/mycode/mycode/mypythoncode/Farmers'
if not os.path.exists(dir):
    os.mkdir(dir)

exists = os.path.isfile(
    '/Users/harishbalaji/documents/mycode/mycode/mypythoncode/Farmers/FriendlyFarmers.csv')
if exists:
    os.remove('/Users/harishbalaji/documents/mycode/mycode/mypythoncode/Farmers/FriendlyFarmers.csv')
else:
    print('File is created')

G = nx.Graph()
plt.figure(3, figsize=(20, 20))
for x in range(1, 51):
    G.add_node(x)
    for y in range(1, 51):
        z1 = x-y
        z2 = y-x
        if z1 <= 10 and x != y and x > y:
            G.add_edge(x, y, color='green', weight=1)
            #print('Friendly Farmers are ', x, ',', y)
            with open(os.path.join(dir, 'FriendlyFarmers.csv'), 'a+') as employee_file:
                employee_writer = csv.writer(
                    employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow([x, y])
pos = nx.circular_layout(G)
edges = G.edges()
colors = [G[u][v]['color'] for u, v in edges]
weights = [G[u][v]['weight'] for u, v in edges]
nx.draw_networkx(G, pos, edges=edges, edge_color=colors, width=weights,
                 with_labels=True, font_color='Black', node_color='Yellow', node_size=500)
plt.savefig('/Users/harishbalaji/documents/mycode/mycode/mypythoncode/Farmers/FriendlyFarmers.svg',format='svg',dpi=1200)