# =============================================
# Title:  All Shortest Paths in a Network
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
if os.path.exists('/Users/harishbalaji/documents/mycode/mycode/mypythoncode/SocialNetworks/All_Shortest_Paths.csv'):
    os.remove(
        '/Users/harishbalaji/documents/mycode/mycode/mypythoncode/SocialNetworks/All_Shortest_Paths.csv')

# adds the header portion of the csv file
with open(os.path.join(dir, 'All_Shortest_Paths.csv'), 'a+') as farmers_file:
    farmers_writer = csv.writer(
        farmers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    farmers_writer.writerow(
        ['From', 'To',  'All Shortest Path(s)', 'Count of Shortest Path(s)'])

G = nx.Graph()
plt.figure(3, figsize=(5, 5))
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
    for y in range(1, 6):
        if(x != y) and (x < y):
            with open(os.path.join(dir, 'All_Shortest_Paths.csv'), 'a+') as farmers_file:
                farmers_writer = csv.writer(
                    farmers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                xxx = [p for p in nx.all_shortest_paths(G, source=x, target=y)]
                for p in xxx:
                    l = len(xxx)
                farmers_writer.writerow(
                    [x, y,  [p for p in nx.all_shortest_paths(G, source=x, target=y)], l])

pos = nx.spring_layout(G)
edges = G.edges()
nx.draw_networkx(G, pos, node_size=500, edge_color='Red',
                 with_labels=True, font_color='Black', node_color='Pink')
