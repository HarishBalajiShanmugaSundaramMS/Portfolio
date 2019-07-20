# =============================================
# Title:  Degree Centrality in a Network
# Author: HarishBalaji ShanmugaSundaram
# Date:   19 July 2019
# =============================================

import csv
import os
import os.path

import matplotlib.pyplot as plt
import networkx as nx

# creates the directory if not existing
dir = r'/Users/harishbalaji/documents/mycode/mycode/mypythoncode/SocialNetworks'
if not os.path.exists(dir):
    os.mkdir(dir)

# deletes the file to avoid row appends on every execution of the program
if os.path.exists('/Users/harishbalaji/documents/mycode/mycode/mypythoncode/SocialNetworks/Degree_Centrality.csv'):
    os.remove(
        '/Users/harishbalaji/documents/mycode/mycode/mypythoncode/SocialNetworks/Degree_Centrality.csv')

# adds the header portion of the csv file
with open(os.path.join(dir, 'Degree_Centrality.csv'), 'a+') as farmers_file:
    farmers_writer = csv.writer(
        farmers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    farmers_writer.writerow(
        ['Node', 'Degree',  'N-1', 'Degree Centrality'])

G = nx.Graph()
plt.figure(3, figsize=(3, 3))
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

n = len(G)

for x in range(1, 6):  # specify the number of nodes you want to add, Here 6-1 = 5 nodes are added
    G.add_node(x)
    deg = nx.degree(G, x)
    dc = deg/(n-1)
    with open(os.path.join(dir, 'Degree_Centrality.csv'), 'a+') as farmers_file:
        farmers_writer = csv.writer(
            farmers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        farmers_writer.writerow([x, deg, n-1, dc])

pos = nx.spring_layout(G)
edges = G.edges()
nx.draw_networkx(G, pos, node_size=500, edge_color='Red',
                 with_labels=True, font_color='Black', node_color='Pink')
