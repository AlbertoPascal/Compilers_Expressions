# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:16:21 2020

@author: beto_
"""


import networkx as nx
import matplotlib.pyplot as plt

def drawGraph():
    global Connection_list, regex
    
    graph_list = list(filter(lambda a: a != 'EoL' and a != 'SoL' and a != 'OR', Connection_list))
    print("my graph list is " + str(graph_list))
    G = nx.DiGraph()
    node_list = []
    cont = 0
    edge_labels={}
    for i in graph_list:
        node_list.append((str(i[0]),str(i[2])))
        edge_labels[(str(i[0]),str(i[2]))] = graph_list[cont][1]
        cont = cont +1
    
    G.add_edges_from(node_list, weight = '1')
    #values = [0.25 for node in G.nodes()]
    print(G.edges)
    
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
    plt.savefig('NFA.png')

def handleOr():
    global Connection_list, pending_connections, Node_count, pending_nodes, Expression_count
    print("Received an |")
#    #Agarrar el primer nodo de este paréntisis y conectarlo a uno nuevo con epsilon. Lo mismo para el último agregado.
#    #Prender bandera para conectar la derecha cuando cierre paréntisis.
#    pending_connections=True
#    #Find the nearest "SoL"
#    initial_node = ""
#    last_node = ""
#    Sol_count = 0
#    for i in range(len(Connection_list) - 2,-1,-1,):
##       if debug_iter == 0:
##                 print("debugging list " + str(Connection_list))
##                 debug_iter=1
##             print("I am in " + str(Connection_list[i]))
#        if Connection_list[i] == "SoL":
#            initial_node = str(Connection_list[i+1][0])
#             #print("My initial node should be " + initial_node)
#            Sol_count = Sol_count +1
#            if Sol_count == Expression_count:
#                break
#    
#    if(Expression_count == 0):
#        last_node = Connection_list[-1][2]
#    else:
#        for i in range(len(Connection_list) - 2,-1,-1,):
##             if debug_iter == 0:
##                 print("debugging list " + str(Connection_list))
##                 debug_iter=1
##             print("I am in " + str(Connection_list[i]))
#            if Connection_list[i] == "EoL":
#                last_node = str(Connection_list[i-1][2])
#                 #print("My initial node should be " + initial_node)
#                break
#    Node_count=Node_count +1 #Get to point to a new Node
#    pending_nodes.append((Node_count, "E", initial_node))
#    pending_nodes.append((last_node, "E", Node_count + 1))
#    Node_count = Node_count + 2 #Prepare the next expression. We added two nodes.
#    pending_connections = True
    
def OrConnectionHelper():
#    global pending_connections,Connection_list, pending_nodes
#    pending_connections=False
#    initial_node=""
#    final_node = ""
#    debug_iter=0
#    print("**********STARTING DEBUGGING****************")
#    for i in range(len(Connection_list) - 2,-1,-1,):
#        if debug_iter == 0:
#             print("debugging list " + str(Connection_list))
#             debug_iter=1
#             print("I am in " + str(Connection_list[i]))
#        if Connection_list[i] == "SoL":
#            initial_node = str(Connection_list[i+1][0])
#            final_node = str(Connection_list[i+1][2])
#            print("My nodes should be " + initial_node + " and " + final_node)
#            print("pending nodes currently has " + str(pending_nodes))
#            break
#    #Add the last two connections to pending_nodes. 
#    print("**********ENDING DEBUGGING****************")
#    pending_nodes.append((pending_nodes[0][0], "E", initial_node))
#    pending_nodes.append((final_node, "E", pending_nodes[1][2]))
#    print("My pending connections are: ")
#    print(pending_nodes)
#    print("End of pending connections")
#    Connection_list.append(pending_nodes[0])
#    Connection_list.append(pending_nodes[2])
#    Connection_list.append(pending_nodes[1])
#    Connection_list.append(pending_nodes[3])
#    
    return 0
def handleAsteriskPlus(invoker_char):
    global Node_count, Connection_list, Expression_count, last_node_arr
    #print("fonud")
    print("My invoker char was " + invoker_char)
    
    #Paso1: validar el anterior. EoL?
    if (Connection_list[-1] == "SoL"): #Agarrar del SoL anterior a su EoL. 
         #print("pendiente")   
         #Siempre vamos a tener que agarrar del SoL anterior al EoL. el último nodo del SoL anterior siempre es connection_list[-3] (SoL, EoL, Nodo interesante)]
         if ( invoker_char == "*"):
            print("Before removing " + str(Connection_list))
            Connection_list = Connection_list[:-2]
            print("Removed previous EoL *******************************")
            print(Connection_list)
            print("End of announcement")
            print("MY EXPRESSION COUNT IS " + str(Expression_count))
            print("***********I NOW HAVE AS CONNECTION_LIST ***********" + str(Connection_list))
         final_node = Connection_list[-1][2]
         print("I took as a final node value " + str(final_node) + " from " + str(Connection_list[-1]) )
         initial_node = ""
         debug_iter = 0
         Sol_count = 0 #The number of expressions to be gone through before taking a value will be kept tracked of with this
         #Innitial_node es el primero despues delSoL anterior.
         for i in range(len(Connection_list) - 2,-1,-1,):
             if debug_iter == 0:
                 print("debugging list " + str(Connection_list))
                 debug_iter=1
             print("I am in " + str(Connection_list[i]))
             if Connection_list[i] == "SoL":
                 initial_node = str(Connection_list[i+1][0])
                 #print("My initial node should be " + initial_node)
                 Sol_count = Sol_count +1
                 print("My sol count is now " + str(Sol_count))
                 if Sol_count == Expression_count:
                     break
         Connection_list.append((final_node, "E", initial_node))
         if(invoker_char == '*'):
            Connection_list.append((initial_node, "E", Node_count + 1))
            Connection_list.append((final_node, "E", Node_count + 1))
         Node_count = Node_count +1
    else: #Agarrar el connection_list{-1}
        #connector_letter = Connection_list[-1][1]
        initial_node = Connection_list[-1][0]
        final_node = Connection_list[-1][2]
        if(invoker_char == '*'):
            Connection_list.append((initial_node, "E", Node_count + 1))
            Connection_list.append((final_node, "E", Node_count + 1))
            last_node_arr = []
            last_node_arr.append((final_node, "E", Node_count + 1))
            Node_count = Node_count +1
        Connection_list.append((final_node, "E", initial_node))
    print("Resulting Connection List is :----------------------------------------------------")
    print(Connection_list)
def interpretSingleInstruct(string_to_interpret):
    global Node_count, Connection_list, Expression_count, last_node_arr, first_node_arr
    print( "I received a " + string_to_interpret + " as regex")
    Connection_list.append("SoL")
    #print("I am interpretSimpleInstruct and I received a " + string_to_interpret)
    for i in string_to_interpret:
        print("Node_count now is " + str(Node_count))
        if (i == '*' or i == '+'):
            print("fonud an " + i)
            handleAsteriskPlus(i)
        elif (i == '|'):
            handleOr()
        else:
            if (len(first_node_arr)==0):
                first_node_arr.append((Node_count, i, Node_count + 1))
            Connection_list.append((Node_count, i, Node_count + 1))
            last_node_arr = []
            last_node_arr.append((Node_count, i, Node_count + 1))
            print("Added" + str((Node_count, i, Node_count + 1)))
            Node_count = Node_count + 1
    #Node_count = Node_count +1 #Prepare for next instruction
    if (pending_connections):
        print("I have pending connections for I had an Or")
        OrConnectionHelper()
    Connection_list.append("EoL")
    print("My start node is now " + str(first_node_arr))
    print("My end node is now " + str(last_node_arr))
def preparePipe():
    global Node_count, Connection_list
    Node_count = Node_count + 1
    Connection_list.append("OR")
def readRegex(regex, iter_number, found_parenthesis_at):
    global Connection_list, Regex_stack, Expression_count
    print("starting iteration " + str(iter_number))
    print("My regex to interpret is: "  + regex)
    current_string = ""
    Regex_stack = list(regex)
    print(Regex_stack)
    print("I have " + str(regex.count("(") ) + " open parenthesis")
    valid = 1
    if (iter_number == 0):
        if(regex.count("(") != regex.count(")")):
            print("Invalid number of parenthesis. Regex is invalid.")
            valid = 0
        else:
            print("valid regex compelted")
            valid = 1
    else:
        print("I received" + regex +" ,"  + str(iter_number) + "***************************************")
    called_by_parenthesis=False   
    call_interpreter=False
    special_char = False
    special_char_pos = 0
    if (valid):
        while (len(Regex_stack)>0):
        #for x in range(0,4): 
            
            print("*********************************starting new cycle**************")
            print("Current Regex is "+ str(Regex_stack))
            inner_parenthesis_pos = 0
            for i in range(0,len(Regex_stack)):
                print("i is " + str(i))
                print("My Regex_stack in i has " + str(Regex_stack[i]))
              
                if(Regex_stack[i]=='('):
                    print("Updating inner parenthesis position")
                    print("most inner parenthesis found up to now is in " + str(inner_parenthesis_pos))
                    inner_parenthesis_pos +=i
                    #current_string = ""
                    
                    print("FOUND OPENNING PARENTHESIS AT " + str(i))
                    if current_string != "":
                        call_interpreter = True
                        called_by_parenthesis=True
                elif(Regex_stack[i]==")"):
                    Expression_count = Expression_count + 1
                    if(Regex_stack[i+1] == "*"):
                        special_char = True
                        special_char_pos = i+1
                        
                    #interpretSingleInstruct(string_to_interpret):
                    #print("calling interpreter with str: " + current_string)
                    call_interpreter=True
                    
            
                elif (Regex_stack[i]!='(' and Regex_stack[i] != ')' and i == len(Regex_stack)-1):
                    #no parenthesis but end of expression:
                    current_string += Regex_stack[i]
                    print("calling interpreter with str: " + current_string)
                    call_interpreter=True
                    
                    
                elif (Regex_stack[i]!='(' and Regex_stack[i] != ')'):
                    print("Adding to curr_string due to finding a regular letter")
                    current_string += Regex_stack[i]
                print(call_interpreter)
                if(call_interpreter):
                    if current_string != "":
                        print("Calling interpreter now")
                        call_interpreter = False
                        interpretSingleInstruct(current_string)
                    
                    print(Connection_list)
                    if(special_char == True):
                        special_char = False
                        current_string = Regex_stack[special_char_pos]
                        print("calling interpreter with str: " + current_string)
                        interpretSingleInstruct(current_string)
                        Regex_stack = Regex_stack[:inner_parenthesis_pos] + Regex_stack [special_char_pos+1:]
                    elif (called_by_parenthesis):
                        Regex_stack = Regex_stack[inner_parenthesis_pos:]
                        called_by_parenthesis=False
                    else:
                        Regex_stack = Regex_stack[:inner_parenthesis_pos] + Regex_stack [i+1:]
                    current_string=""
                    print("Erasing Regex_stack from " + str(inner_parenthesis_pos) + str(i))
                    print("Regex_stack now has " +str(Regex_stack))
                    print("New Regex_stack length is " +str(len(Regex_stack)) + "**************************" )
                    break;
                
            
  
first_node_arr = []
last_node_arr = []
pending_connections=False;
pending_nodes = []
Regex_stack = []
Connection_list = []
Node_count = 0
Expression_count=0
regex = "ab*(de)*"
readRegex(regex,0,0)
drawGraph()