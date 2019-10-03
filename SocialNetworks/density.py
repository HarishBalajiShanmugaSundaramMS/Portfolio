import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
plt.figure(3, figsize=(5, 5))
G.add_edge('Mike', 'Bob'); G.add_edge('Mike', 'Emma');
G.add_edge('Mike', 'Jill'); G.add_edge('Bob', 'Emma');
G.add_edge('Bob', 'Jill'); G.add_edge('Bob', 'John');
G.add_edge('John', 'Bob'); G.add_edge('John', 'Jill');
G.add_edge('John', 'Shane'); G.add_edge('Leah', 'John');
G.add_edge('Leah', 'Jill'); G.add_edge('Leah', 'Shane');
G.add_edge('Shane', 'John'); G.add_edge('Shane', 'Jill');
G.add_edge('Shane', 'Emma'); G.add_edge('Shane', 'Liz');
G.add_edge('Emma', 'Jill'); G.add_edge('Emma', 'Liz');
G.add_edge('Liz', 'Allen'); G.add_edge('Allen', 'Lisa');
pos = nx.spring_layout(G); edges = G.edges();
actualConnections=0; potentialConnections=0;
nx.draw_networkx(G, pos, node_size=500, edge_color='Aqua', 
with_labels=True, font_color='White', node_color='Gray')
noOfEdges=len(nx.degree(G)); actualConnections= len(nx.edges(G))
potentialConnections=(noOfEdges*(noOfEdges-1))/2
densityOfNetwork=actualConnections/potentialConnections
print('Density Calcualted Using In-Built Function = ', nx.density(G))
print('Number of Edges =', noOfEdges)
print('Number of Actual Connections =', actualConnections)
print('Number of Potential Connections =', potentialConnections)
print('Density Calcualted Using Formula = ', densityOfNetwork)
print(nx.diameter(G,e=None))
print(nx.eccentricity(G,'Lisa'))
#The diameter is the maximum eccentricity.

