# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:16:21 2020

@author: beto_, Manu, Roy
"""


import networkx as nx
import matplotlib.pyplot as plt

def drawGraph():
    global Connection_list, regex, DFA
    
    graph_list = list(filter(lambda a: a != 'EoL' and a != 'SoL' and a != 'OR', Connection_list))
    #print("my graph list is " + str(graph_list))
    plt.figure(1)
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
    #print(G.edges)
    
    print("My node list is now " + str(node_list))
    print("My edge list is now " + str(edge_labels))

    black_edges = [edge for edge in G.edges()]
    pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='fdp')
    #print(pos)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G, pos, connectionstyle='arc3, rad=-0.2', label_pos = 0.1, fontsize=12)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels, connectionstyle='arc3, rad=0.2', label_pos = 0.8, clip_on = False, font_size=9, bbox=dict(facecolor='red', alpha=0.1), rotate=True)
    #nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True, connectionstyle='arc3, rad=0.2')
    #plt.show()
    plt.savefig('NFA.png')
    
    #Now ##printing and creating the DFA
    plt.figure(2)
    G2 = nx.DiGraph()
    node_list2 = []
    cont2 = 0
    edge_labels2={}
    for item in DFA:
        ##print("I have the dict " + str(item))
        cont2+=1
    added_nodes = []
    #clean DFA list
    print(DFA)
    for node in DFA:
        for key in node:
            if key != 'Node' and node[key]!= '':
                edge_labels2[ (str(node["Node"]), str(node[key])) ] = key
                node_list2.append( (str(node["Node"]), str(node[key])) )

    print("Node_label: ")
    print(node_list2)
    print("Node_label2: ")
    #print(type(node_list2[0][0]))
    
    print("Edge_label: ")
    print(edge_labels2)
    print("Edge_label2: ")
    #print(edge_labels2[0])
    
    #print(node_list2)
    #print("This is my new graph_list for DFA: ")
    #print(node_list2)
    G2.add_edges_from(edge_labels2, weight = '1')
    G2.add_edges_from(node_list2, weight = '1')
    pos2 = nx.spring_layout(G2)
    #pos2 = nx.drawing.nx_pydot.graphviz_layout(G2, prog='fdp')
    ##print(pos)
    black_edges = [edge for edge in G2.edges()]
    nx.draw_networkx_nodes(G2, pos2, cmap=plt.get_cmap('jet'), node_size = 500)
    nx.draw_networkx_labels(G2, pos2, connectionstyle='arc3, rad=-0.5', label_pos = 0.1, font_size=8)
    nx.draw_networkx_edge_labels(G2,pos2,edge_labels=edge_labels2, connectionstyle='arc3, rad=0.2', label_pos = 0.8, clip_on = False, font_size=7, bbox=dict(facecolor='red', alpha=0.1), rotate=True)
    #nx.draw_networkx_edges(G2, pos2, edgelist=edge_, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G2, pos2, edgelist=black_edges, arrows=True, connectionstyle='arc3, rad=0.3', arrowsize=3,arrowstyle='fancy')
    plt.savefig('DFA.png')
def handleOr():
    global Connection_list, pending_connections, Node_count, pending_nodes, Expression_count, last_node_arr, first_node_arr
    ##print("Received an |")
    #Adding the new first and last nodes
    Node_count+=1
    Expression_count=0
    Connection_list.append((Node_count, "E", first_node_arr[0][0]))
    ##print("Appending new connection: " + str((Node_count, "E", first_node_arr[0][0])))
    Node_count+=1
    first_node_arr = []
    first_node_arr.append((Node_count -1, "E", Connection_list[-1][2])) #podría estar actualizandose mal.
    ##print("Appending new connection: " + str((last_node_arr[0][2], "E", Node_count)))
    Connection_list.append((last_node_arr[0][2], "E", Node_count))
    
    last_node_arr = []
    last_node_arr.append((Connection_list[-1][0], "E", Node_count)) #podría estar afectando el conenction list
    
    
    ##print("****************Newest Inicial node*******************")
    ##print(first_node_arr[0][0])
    ##print("****************Newest final node*******************")
    ##print(last_node_arr[0][2])
    Node_count+=1 #prepare to create right part of pipe
    
    pending_connections = True
#    
    
def OrConnectionHelper():
#    global pending_connections,Connection_list, pending_nodes
#    pending_connections=False
#    initial_node=""
#    final_node = ""
#    debug_iter=0
#    ##print("**********STARTING DEBUGGING****************")
#    for i in range(len(Connection_list) - 2,-1,-1,):
#        if debug_iter == 0:
#             ##print("debugging list " + str(Connection_list))
#             debug_iter=1
#             ##print("I am in " + str(Connection_list[i]))
#        if Connection_list[i] == "SoL":
#            initial_node = str(Connection_list[i+1][0])
#            final_node = str(Connection_list[i+1][2])
#            ##print("My nodes should be " + initial_node + " and " + final_node)
#            ##print("pending nodes currently has " + str(pending_nodes))
#            break
#    #Add the last two connections to pending_nodes. 
#    ##print("**********ENDING DEBUGGING****************")
#    pending_nodes.append((pending_nodes[0][0], "E", initial_node))
#    pending_nodes.append((final_node, "E", pending_nodes[1][2]))
#    ##print("My pending connections are: ")
#    ##print(pending_nodes)
#    ##print("End of pending connections")
#    Connection_list.append(pending_nodes[0])
#    Connection_list.append(pending_nodes[2])
#    Connection_list.append(pending_nodes[1])
#    Connection_list.append(pending_nodes[3])
#    
    return 0
def handleAsteriskPlus(invoker_char):
    global Node_count, Connection_list, Expression_count, last_node_arr, first_node_arr, pending_connections
    ###print("fonud")
    ##print("My invoker char was " + invoker_char)
    
    #Paso1: validar el anterior. EoL?
    if (Connection_list[-1] == "SoL"): #Agarrar del SoL anterior a su EoL. 
         ###print("pendiente")   
         #Siempre vamos a tener que agarrar del SoL anterior al EoL. el último nodo del SoL anterior siempre es connection_list[-3] (SoL, EoL, Nodo interesante)]
         if ( invoker_char == "*" or invoker_char == "+"):
            ##print("Before removing " + str(Connection_list))
            Connection_list = Connection_list[:-2]
            ##print("Removed previous EoL *******************************")
            ##print(Connection_list)
            ##print("End of announcement")
            ##print("MY EXPRESSION COUNT IS " + str(Expression_count))
            ##print("***********I NOW HAVE AS CONNECTION_LIST ***********" + str(Connection_list))
         final_node = Connection_list[-1][2]
         ##print("I took as a final node value " + str(final_node) + " from " + str(Connection_list[-1]) )
         initial_node = ""
         debug_iter = 0
        # Sol_count = 1 #The number of expressions to be gone through before taking a value will be kept tracked of with this
         #Innitial_node es el primero despues delSoL anterior.
         for i in range(len(Connection_list) - 2,-1,-1,):
             if debug_iter == 0:
                 ##print("debugging list " + str(Connection_list))
                 debug_iter=1
             ##print("I am in " + str(Connection_list[i]))
             if Connection_list[i] == "SoL":
                 initial_node = str(Connection_list[i+1][0])
                 ###print("My initial node should be " + initial_node)
                 #Sol_count = Sol_count +1
                # ##print("My sol count is now " + str(Sol_count))
                 #if Sol_count >= Expression_count:
                 break
         Connection_list.append((final_node, "E", initial_node))
         if(invoker_char == '*'):
            Connection_list.append((initial_node, "E", Node_count + 1))
            Connection_list.append((final_node, "E", Node_count + 1))
            if not pending_connections:
                last_node_arr = []
                last_node_arr.append((final_node, "E", Node_count + 1))
            ##print("My start node is now " + str(first_node_arr))
            ##print("My end node is now " + str(last_node_arr))
         Node_count = Node_count +1
    else: #Agarrar el connection_list{-1}
        #connector_letter = Connection_list[-1][1]
        initial_node = Connection_list[-1][0]
        final_node = Connection_list[-1][2]
        if(invoker_char == '*'):
            Connection_list.append((initial_node, "E", Node_count + 1))
            Connection_list.append((final_node, "E", Node_count + 1))
            if not pending_connections:
                last_node_arr = []
                last_node_arr.append((final_node, "E", Node_count + 1))
            Node_count = Node_count +1
        Connection_list.append((final_node, "E", initial_node))
    ##print("Resulting Connection List is :----------------------------------------------------")
    ##print(Connection_list)
def check_new_initial(string_to_interpret):
    global interpretation_called, first_node_arr
    if string_to_interpret != "*":
        interpretation_called+=1
        current_sol_count=0
        for i in Connection_list:
            if i == "SoL":
                current_sol_count+=1
                if current_sol_count == interpretation_called:
                    first_node_arr = Connection_list[Connection_list.index(i+1)]
                    ##print("Updated my starter due to obligatory nodes. New starter is ")
def interpretSingleInstruct(string_to_interpret):
    global interpretation_called, Node_count, Connection_list, Expression_count, last_node_arr, first_node_arr, pending_connections, handled_pipe
    #update first node for each time
    #check_new_initial(string_to_interpret)
    ##print( "I received a " + string_to_interpret + " as regex")
    Connection_list.append("SoL")
    ###print("I am interpretSimpleInstruct and I received a " + string_to_interpret)
    for i in string_to_interpret:
        ##print("Node_count now is " + str(Node_count))
        if (i == '*' or i == '+'):
            ##print("fonud an " + i)
            handleAsteriskPlus(i)
        elif (i == '|'):
            if (pending_connections):
                ##print("I have pending connections for I had an Or") #iterate to previous OR before adding.
                for i in range(len(Connection_list)-1,-1,-1):
                    if Connection_list[i] == "OR":
                        t_list=[]
                        t_list.append((Node_count, "E", last_node_arr[0][2]))
                        C2= Connection_list[:i]
                        c3 = Connection_list[i:]
                        Connection_list = Connection_list[:i] + t_list + Connection_list[i:]
                        break
                #Connection_list.append((Node_count, "E", last_node_arr[0][2]))
                ##print("Added pipe final connection_ inside for: " + str(last_node_arr[0][2]))
                pending_connections=False
            handleOr()
            handled_pipe = True
        else:
            if (len(first_node_arr)==0):
                first_node_arr.append((Node_count, i, Node_count + 1))
            if not pending_connections:
                ###print("Need to update my last_node_arr due to my string being" + string_to_interpret[string_to_interpret.index(i) +1])
                last_node_arr = []
                last_node_arr.append((Node_count, i, Node_count + 1))
            if(handled_pipe): #might need to add here a EoL SoL removal to add this and then readd them after connection
                for x in range(len(Connection_list)-1,-1,-1):
                    if Connection_list[x]=="SoL" and Connection_list[x-1] == "EoL":
                        #Remove previous two values. 
                        last_val = []
                        last_val.append(Connection_list[x-2])
                        Connection_list = Connection_list[:x-2] + Connection_list[x+1:] + last_val
                        break
                #Connection_list = Connection_list[:-2] #removes EoL SoL
                Connection_list.append("OR") #append identifier
                Connection_list.append((first_node_arr[0][0], "E", Node_count)) #append initial or connection
                Connection_list.append("EoL")
                Connection_list.append("SoL") #returns list to normal behaviour
                ##print("Added pipe initial connection: " + str(Connection_list[-1]))
                handled_pipe=False
            Connection_list.append((Node_count, i, Node_count + 1))
            ##print("Added" + str((Node_count, i, Node_count + 1)))
            Node_count = Node_count + 1
            
    #Node_count = Node_count +1 #Prepare for next instruction
#    if (pending_connections):
#        ##print("I have pending connections for I had an Or")
#        Connection_list.append((Node_count, "E", last_node_arr[0][2]))
#        ##print("Added pipe final connection outside for: " + str((Node_count, "E", last_node_arr[0][2])))
#        pending_connections=False
    Connection_list.append("EoL")
    ##print("My start node is now " + str(first_node_arr))
    ##print("My end node is now " + str(last_node_arr))
def preparePipe():
    global Node_count, Connection_list

    Connection_list.append("OR")
def generateTable():
    global Connection_list, Node_count, transitionTable, edges
    
    
    for i in range (len(Connection_list)):
        if (Connection_list[i] != "SoL"):
            if (Connection_list[i] != "EoL"):
                if (Connection_list[i] != "OR"):
                    if (Connection_list[i][1] not in edges):
                        edges.append(Connection_list[i][1])    
    
    for j in range (0, Node_count+1):
        transitionTable.append(dict())
        transitionTable[j]["Node"] = str(j)
        for i in edges:           
            transitionTable[j][i] = ""

    ##print(Connection_list)
    for i in range (len(Connection_list)):
        if (Connection_list[i] != "SoL"):
            if (Connection_list[i] != "EoL"):
                if (Connection_list[i] != "OR"):
                    transitionTable[int(Connection_list[i][0])][Connection_list[i][1]] += str(Connection_list[i][2]) + ","

    ###print("TT" + str(transitionTable))
    
    for node in transitionTable:
        ###print(node.keys())
        if "E" not in node.keys():
            ##print("YES")
            return False

    for nodes in transitionTable:
        if (nodes["E"] != ""):
            if (nodes["E"][-1] == ","):
                nodes["E"] = nodes["E"][:-1]

    return True

def getEclose(currentRead):
    global transitionTable, Node_count, DFA, edges, edgesDFA
    ##print(transitionTable)
    nodeForE = currentRead
    #print(nodeForE)
    if(transitionTable[int(nodeForE)]["E"] != ""):
        newNode = nodeForE + "," + transitionTable[int(nodeForE)]["E"]
    else:
        newNode = nodeForE + transitionTable[int(nodeForE)]["E"]
    return newNode
        
def checkDestinations(nodeArr):
    global transitionTable, Node_count, DFA, edges, edgesDFA

    if (nodeArr[0] == ""):
        nodeArr = nodeArr[1:]

    for node in nodeArr:
        DFA.append(dict())
        for edges in edgesDFA:
            DFA[-1]["Node"] = node
            DFA[-1][edges] = ""

    it = 0

    #print(transitionTable)
    #print(nodeArr)
    for nodes in nodeArr:        
        #print(nodes)
        checkConn = [x.strip() for x in nodes.split(',')]
        #print(checkConn)
        for nodes_separated in checkConn:
            for edges in edgesDFA:
                #print(nodes_separated + "    " +str(edges) + "----"+ str(transitionTable[int(nodes_separated)][edges]))
                #print(nodes_separated + " -  " +str(edges))
                path = str(transitionTable[int(nodes_separated)][edges])
                
                DFA[it][str(edges)] += str(path)
            
                if (path != ""):
                    if (path[-1] == ","):
                        path = path[:-1]
                        
                    DFA[it][str(edges)] += transitionTable[int(path)]["E"]
                    
        it += 1
                
def NFAtoDFA():
    global transitionTable, Node_count, DFA, edges, edgesDFA, first_node_arr
    currentRead = ""
    if (transitionTable[first_node_arr[0][0]]["E"] != ""):
        nodeArr = [transitionTable[first_node_arr[0][0]]["E"]]
    else:
        nodeArr = [str(first_node_arr[0][0])]
    #nodeArr = [transitionTable[first_node_arr[0][0]]["E"]]
    edgesDFA = list(filter(lambda a: a != 'E', edges))

    for nodes in range(0, Node_count+1):        
        for inp in edgesDFA:
            currentRead = transitionTable[nodes][inp]
            if (currentRead != ""):
                if (currentRead[-1] == ","):
                    currentRead = currentRead[:-1]
                
                nodeArr.append(getEclose(currentRead))  
    
    checkDestinations(nodeArr)

def readRegex(regex, iter_number, found_parenthesis_at):
    global Connection_list, Regex_stack, Expression_count, pending_connections, last_node_arr, first_node_arr
    ##print("starting iteration " + str(iter_number))
    ##print("My regex to interpret is: "  + regex)
    current_string = ""
    Regex_stack = list(regex)
    ##print(Regex_stack)
    ##print("I have " + str(regex.count("(") ) + " open parenthesis")
    valid = 1
    if (iter_number == 0):
        if(regex.count("(") != regex.count(")")):
            ##print("Invalid number of parenthesis. Regex is invalid.")
            valid = 0
        else:
            ##print("valid regex compelted")
            valid = 1

    called_by_parenthesis=False   
    call_interpreter=False
    special_char = False
    special_char_pos = 0
    if (valid):
        while (len(Regex_stack)>0):
        #for x in range(0,4): 
            
            ##print("*********************************starting new cycle**************")
            ##print("Current Regex is "+ str(Regex_stack))
            inner_parenthesis_pos = 0
            for i in range(0,len(Regex_stack)):
                ##print("i is " + str(i))
                ##print("My Regex_stack in i has " + str(Regex_stack[i]))
              
                if(Regex_stack[i]=='('):
                    ##print("Updating inner parenthesis position")
                    ##print("most inner parenthesis found up to now is in " + str(inner_parenthesis_pos))
                    inner_parenthesis_pos +=i
                    update_initial=True
                    #current_string = ""
                    if (pending_connections):
                        ##print("I have pending connections for I had an Or") #iterate to previous OR before adding.
                        for i in range(len(Connection_list)-1,-1,-1):
                            if Connection_list[i] == "OR":
                                t_list=[]
                                t_list.append((Node_count, "E", last_node_arr[0][2]))
                                C2= Connection_list[:i]
                                c3 = Connection_list[i:]
                                Connection_list = Connection_list[:i] + t_list + Connection_list[i:]
                                break
                        pending_connections=False
                    ##print("FOUND OPENNING PARENTHESIS AT " + str(i))
                    if current_string != "":
                        call_interpreter = True
                        called_by_parenthesis=True
                elif(Regex_stack[i]==")"):
                    
                    Expression_count = Expression_count + 1
                    if(i + 1 < len(Regex_stack) and (Regex_stack[i+1] == "*" or Regex_stack[i+1] == "+")):
                        special_char = True
                        special_char_pos = i+1
                        
                    #interpretSingleInstruct(string_to_interpret):
                    ###print("calling interpreter with str: " + current_string)
                    call_interpreter=True
                    
            
                elif (Regex_stack[i]!='(' and Regex_stack[i] != ')' and i == len(Regex_stack)-1):
                    #no parenthesis but end of expression:
                    current_string += Regex_stack[i]
                    ##print("calling interpreter with str: " + current_string)
                    call_interpreter=True
                    
                    
                elif (Regex_stack[i]!='(' and Regex_stack[i] != ')'):
                    ##print("Adding to curr_string due to finding a regular letter")
                    current_string += Regex_stack[i]
                ##print(call_interpreter)
                if(call_interpreter):
                    if current_string != "":
                        ##print("Calling interpreter now")
                        call_interpreter = False
                        interpretSingleInstruct(current_string)
                    
                    ##print(Connection_list)
                    if(special_char == True):
                        special_char = False
                        current_string = Regex_stack[special_char_pos]
                        if (pending_connections):
                        ##print("I have pending connections for I had an Or") #iterate to previous OR before adding.
                            
                            for i in range(len(Connection_list)-1,-1,-1):
                                if Connection_list[i] == "OR":
                                    t_list=[]
                                    t_list.append((Node_count, "E", last_node_arr[0][2]))
                                    C2= Connection_list[:i]
                                    c3 = Connection_list[i:]
                                    Connection_list = Connection_list[:i] + t_list + Connection_list[i:]
                                    break
                            pending_connections=False
                        ##print("calling interpreter with str: " + current_string)
                        interpretSingleInstruct(current_string)
                        Regex_stack = Regex_stack[:inner_parenthesis_pos] + Regex_stack [special_char_pos+1:]
                    elif (called_by_parenthesis):
                        Regex_stack = Regex_stack[inner_parenthesis_pos:]
                        called_by_parenthesis=False
                    else:
                        Regex_stack = Regex_stack[:inner_parenthesis_pos] + Regex_stack [i+1:]
                    current_string=""
                    ##print("Erasing Regex_stack from " + str(inner_parenthesis_pos) + str(i))
                    ##print("Regex_stack now has " +str(Regex_stack))
                    ##print("New Regex_stack length is " +str(len(Regex_stack)) + "**************************" )
                    break;
        if (pending_connections):
            ##print("I have pending connections for I had an Or") #iterate to previous OR before adding.
            for i in range(len(Connection_list)-1,-1,-1):
                if Connection_list[i] == "OR":
                    t_list=[]
                    t_list.append((Node_count, "E", last_node_arr[0][2]))
                    C2= Connection_list[:i]
                    c3 = Connection_list[i:]
                    Connection_list = Connection_list[:i] + t_list + Connection_list[i:]
                    break
            pending_connections=False
        ##print("Resulting Connection List after everything" + str(Connection_list))

def cleanDFA():
    global DFA

    visited = []
    for node in DFA:
        for key in node:
            if (node[key] != ""):
                if node[key][-1] == ",":
                    node[key] = node[key][:-1]
                if (key != "Node"):
                    if (node[key] not in visited):
                        visited.append(node[key])
    
    for node in DFA:
        if (node["Node"] not in visited):
            DFA.remove(node)
                    
                    
        
def getFinalNodes():
    global DFA, last_node_arr, DFA_final_nodes

    for node in DFA:
        nodes_separated = list(filter(lambda a: a != ',', node["Node"]))
        for nodes_sep in nodes_separated:
            if (nodes_sep == str(last_node_arr[0][-1])):
                if node not in DFA_final_nodes:
                    DFA_final_nodes.append(node["Node"])

transitionTable = []
edges = []
edgesDFA = None
DFA = []
DFA_final_nodes = []
handled_pipe=False
interpretation_called = 0
first_node_arr = []
last_node_arr = []
pending_connections=False;
pending_nodes = []
Regex_stack = []
Connection_list = []
Node_count = 0
Expression_count=0
regex = "a|b"
update_initial=False
readRegex(regex,0,0)
Connection_list = list(dict.fromkeys(Connection_list))
if (generateTable() == True):
    NFAtoDFA()
else:
    DFA = transitionTable;

cleanDFA()
getFinalNodes()
print(DFA)
drawGraph()

