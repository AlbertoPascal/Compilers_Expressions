# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 17:18:12 2020

@author: beto_
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')], weight = '1')

val_map = {'A': 1.0,
           'D': 0.5,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]
print(values)
# Specify the edges you want here
red_edges = [('A', 'C'), ('E', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

#edge_labels=dict([((u,v,),d['weight'])
#                 for u,v,d in G.edges(data=True)])
print(len(G.edges))
alph = [chr(i) for i in range(97, 97 + len(G.edges))]
cont = 0
for i in G.edges:
    edge_labels[i] = alph[cont]
    cont = cont +1
#edge_labels={i: str(i) for i in G.edges}
print(edge_labels)
# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
print(pos)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
#plt.show()
plt.savefig('Graphs.png')