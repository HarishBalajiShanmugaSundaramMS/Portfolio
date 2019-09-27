import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community
import community as cm
def initialize_sbm(list_of_community_sizes,matrix_probabilities):
    G = nx.stochastic_block_model(list_of_community_sizes,matrix_probabilities)
    positions = nx.spring_layout(G)
    nx.set_node_attributes(G,positions,'positions')
    return G

G=initialize_sbm([100,100,100,100,100],[
    [0.05,0.001,0,0,0.001],
    [0.001,0.05,0.001,0,0],
    [0,0.001,0.05,0.001,0],
    [0,0,0.001,0.05,0.001],
    [0.001,0,0,0.001,0.05]])
G = max(nx.connected_component_subgraphs(G), key=len)

nx.draw(G,node_size=100,node_color='green')
plt.show()