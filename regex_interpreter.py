# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:16:21 2020

@author: beto_
"""

import sys

def interpretSingleInstruct(string_to_interpret):
    global Node_count, Connection_list, Expression_count
    
    Connection_list.append("SoL")
    print("I am interpretSimpleInstruct and I received a " + string_to_interpret)
    for i in string_to_interpret:
        print("Node_count now is " + str(Node_count))
        if (i == '*'):
            print("fonud")
            #Paso1: validar el anterior. EoL?
            if (Connection_list[-1] == "SoL"): #Agarrar del SoL anterior a su EoL. 
                 print("pendiente")   
                 #Siempre vamos a tener que agarrar del SoL anterior al EoL. el último nodo del SoL anterior siempre es connection_list[-3] (SoL, EoL, Nodo interesante)]
                 final_node = Connection_list[-3][2]
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
                         print("My initial node should be " + initial_node)
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
        else:
            Connection_list.append((Node_count, i, Node_count + 1))
            print("Added" + str((Node_count, i, Node_count + 1)))
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
            print(Regex_stack)
        else:
            #tenemos que sacar del stack hasta el próximo (
            while(Regex_stack[-1]!= '('):
                current_string = Regex_stack[-1] + current_string
                Regex_stack.pop()
                print("Current string has " + current_string)
            #Send string to interpret:
            Regex_stack.pop() #Get rid of open parenthesis
            interpretSingleInstruct(current_string)
            current_string = ""
            print(Connection_list)
    
        
    return 1

Regex_stack = []
Connection_list = []
Node_count = 0
Expression_count=0
regex = "(aE)"
readRegex(regex)