# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:16:21 2020

@author: beto_
"""


import networkx as nx
import matplotlib.pyplot as plt
import pydotplus
from networkx.drawing.nx_pydot import graphviz_layout
def drawGraph():
    global Connection_list
    
    graph_list = list(filter(lambda a: a != 'EoL' and a != 'SoL', Connection_list))
    print("my graph list is " + str(graph_list))
    G = nx.DiGraph()
    node_list = []
    for i in graph_list:
        node_list.append((str(i[0]),str(i[2])))
    cont = 0
    edge_labels={}
    G.add_edges_from(node_list, weight = '1')
    values = [0.25 for node in G.nodes()]
    for i in G.edges:
        edge_labels[i] = graph_list[cont][1]
        cont = cont +1
    print("My node list is now " + str(node_list))
    print("My edge list is now " + str(edge_labels))

    black_edges = [edge for edge in G.edges()]
    pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='fdp')
    print(pos)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G, pos, connectionstyle='arc3, rad=-0.2', label_pos = 0.1, fontsize=12)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels, connectionstyle='arc3, rad=0.2', label_pos = 0.8, clip_on = False, font_size=9, bbox=dict(facecolor='red', alpha=0.1), rotate=True)
    #nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True, connectionstyle='arc3, rad=0.2')
    #plt.show()

def handleOr():
    print("Received an |")
def handleAsterisk():
    global Node_count, Connection_list, Expression_count
    #print("fonud")
    #Paso1: validar el anterior. EoL?
    if (Connection_list[-1] == "SoL"): #Agarrar del SoL anterior a su EoL. 
         #print("pendiente")   
         #Siempre vamos a tener que agarrar del SoL anterior al EoL. el último nodo del SoL anterior siempre es connection_list[-3] (SoL, EoL, Nodo interesante)]
         final_node = Connection_list[-3][2]
         initial_node = ""
         debug_iter = 0
         Sol_count = 0 #The number of expressions to be gone through before taking a value will be kept tracked of with this
         #Innitial_node es el primero despues delSoL anterior.
         for i in range(len(Connection_list) - 2,-1,-1,):
#             if debug_iter == 0:
#                 print("debugging list " + str(Connection_list))
#                 debug_iter=1
#             print("I am in " + str(Connection_list[i]))
             if Connection_list[i] == "SoL":
                 initial_node = str(Connection_list[i+1][0])
                 #print("My initial node should be " + initial_node)
                 Sol_count = Sol_count +1
                 if Sol_count == Expression_count:
                     break
         Connection_list.append((final_node, "E", initial_node))
         Connection_list.append((initial_node, "E", Node_count + 1))
         Connection_list.append((final_node, "E", Node_count + 1))
         Node_count = Node_count +1
    else: #Agarrar el connection_list{-1}
        connector_letter = Connection_list[-1][1]
        initial_node = Connection_list[-1][0]
        final_node = Connection_list[-1][2]
        Connection_list.append((final_node, "E", initial_node))
        Connection_list.append((initial_node, "E", Node_count + 1))
        Connection_list.append((final_node, "E", Node_count + 1))
        Node_count = Node_count +1
def interpretSingleInstruct(string_to_interpret):
    global Node_count, Connection_list, Expression_count
    
    Connection_list.append("SoL")
    #print("I am interpretSimpleInstruct and I received a " + string_to_interpret)
    for i in string_to_interpret:
        #print("Node_count now is " + str(Node_count))
        if (i == '*'):
            handleAsterisk()
        elif (i == '|'):
            handleOr()
        else:
            Connection_list.append((Node_count, i, Node_count + 1))
            #print("Added" + str((Node_count, i, Node_count + 1)))
            Node_count = Node_count + 1
    #Node_count = Node_count +1 #Prepare for next instruction
    Connection_list.append("EoL")
    Expression_count = Expression_count + 1
        
def readRegex(regex):
    global Regex_stack, Connection_list
    print("My regex to interpret is: "  + regex)
    current_string = ""
    for i in regex:
        if(i != ")"):
            Regex_stack.append(i)
            #print(Regex_stack)
        else:
            #tenemos que sacar del stack hasta el próximo (
            while(Regex_stack[-1]!= '('):
                current_string = Regex_stack[-1] + current_string
                Regex_stack.pop()
                #print("Current string has " + current_string)
            #Send string to interpret:
            Regex_stack.pop() #Get rid of open parenthesis
            interpretSingleInstruct(current_string)
            current_string = ""
            #print(Connection_list)
    print(Connection_list)
        
    return 1

Regex_stack = []
Connection_list = []
Node_count = 0
Expression_count=0
regex = "(ab*a)"
readRegex(regex)
drawGraph()