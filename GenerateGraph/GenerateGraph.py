#Milorad Markovic RA162-2015
#FTN - RT-RK
#Projektovanje Algoritama

import pprint
import json
import os

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None, name = "NoName"):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d
        self.name = name

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class Graph:
    def __init__(self, connections, prices):
        self.connections = connections
        self.prices = prices

def UserDefineGraphUndirectional():
    gr = []
    pr = []
    node_names = []
    print("Enter Node Names :\n(Just Press ENTER to go Enter Connections)")
    x = "filler"
    counter = 0
    while x!="":
        x = input("- ")

        gr.append([])
        pr.append([])
        node_names.append(x)
        gr[counter].append(Node(name = x))
        pr[counter].append(0)
        counter+=1
    
    gr = gr[:-1]
    pr = pr[:-1]
    node_names = node_names[:-1]

    print("Enter Connections :\n(Just Press ENTER to go Enter Connections)\n(format \"NodeName1-ConnectionWeight-Nodename2\")")
    x = "filler"
    while x!="":
        x = input("- ")
        if x == "":
            break
        connection = x.split("-")
        gr[node_names.index(connection[0])].append(gr[node_names.index(connection[2])][0])
        pr[node_names.index(connection[0])].append(int(connection[1]))

    pprint.pprint(gr)
    input("\n")
    input(pr)
    
    graph = Graph(gr, pr)

    #for i in range(len(gr)):
    #    print("-"*20 + "\nEnter Outgoing Connections for Node \"" + gr[i][0].name + "\" :\n(Just Press ENTER to go to next Node)")
    #    x = "filler"
    #    conn_names = []

    #    while x!="":
    #        x = input("- ")
    #        conn_names.append(x)

    #    conn_names = conn_names[:-1]
    #    if len(conn_names)>0:
    #        print("-"*20 + "\nEnter Prices for Node \"" + gr[i][0].name + "\" :\n")
    #    for j in range(len(conn_names)):
    #        p = int(input("Price of " + gr[i][0].name + "-->" + conn_names[j] + " : "))
    #        pr[i].append(p)
    #        gr[i].append(Node(name = conn_names[j]))
        
    #graph = Graph(gr, pr)
    ##PrintGraph(graph)
    ##print(graph.prices)
    ##pprint.pprint(graph.graph)
    return graph

def UserDefineGraphDirectional():
    gr = []
    pr = []
    print("Enter Node Names :\n(Just Press ENTER to go Enter Connections)")
    x = "filler"
    counter = 0
    while x!="":
        x = input("- ")

        gr.append([])
        pr.append([])

        gr[counter].append(Node(name = x))
        pr[counter].append(0)
        counter+=1
    
    gr = gr[:-1]
    pr = pr[:-1]

    for i in range(len(gr)):
        print("-"*20 + "\nEnter Outgoing Connections for Node \"" + gr[i][0].name + "\" :\n(Just Press ENTER to go to next Node)")
        x = "filler"
        conn_names = []

        while x!="":
            x = input("- ")
            conn_names.append(x)

        conn_names = conn_names[:-1]
        if len(conn_names)>0:
            print("-"*20 + "\nEnter Prices for Node \"" + gr[i][0].name + "\" :\n")
        for j in range(len(conn_names)):
            p = int(input("Price of " + gr[i][0].name + "-->" + conn_names[j] + " : "))
            pr[i].append(p)
            gr[i].append(Node(name = conn_names[j]))
        
    graph = Graph(gr, pr)
    
    return graph

def GraphtoJSON(graph):
    jsonGraph = {}
    jsonGraph["Connections"] = {}
    for i in range(len(graph.connections)):
        conn = []
        for j in range(len(graph.connections[i])):
            conn.append(graph.connections[i][j].name)
        jsonGraph["Connections"][graph.connections[i][0].name] = conn
    #pprint.pprint(jsonGraph)

    jsonGraph["Prices"] = {}
    for i in range(len(graph.prices)):
            prices = []
            for j in range(len(graph.prices[i])):
                prices.append(str(graph.prices[i][j]))
            jsonGraph["Prices"][graph.connections[i][0].name] = prices
    
    return jsonGraph

def JSONtoGraph(jsonGraph):
    Connections = jsonGraph["Connections"]
    Prices = jsonGraph["Prices"]
    gr = []
    pr = []

    for i in Connections:
        l = Connections[i]
        for j in range(len(l)):
            l[j] = Node(name = l[j])
        gr.append(l)

    for i in Prices:
        pr.append(Prices[i])

    graph = Graph(gr, pr)
    return graph

def WriteJSONtoFile(filename, jsonGraph):
    with open(filename + ".txt","w") as file:
        json.dump(jsonGraph, file)
    return

def ReadJSONfromFile(filename):
    with open(filename + ".txt") as file:
        jsonGraph = json.load(file)
    return jsonGraph

def PrintGraph(G):
    print("-"*40)
    for i in range(len(G.connections)):
        print("Connections for Node \"" + G.connections[i][0].name + "\" are :")
        for j in range(1, len(G.connections[i])):
            print(G.connections[i][0].name + "-->" + G.connections[i][j].name + "  Price: "+ str(G.prices[i][j]))

    print("-"*40)    
    return

def TestRun():
    WriteJSONtoFile("test",GraphtoJSON(UserDefineGraphDirectional()))
    PrintGraph(JSONtoGraph(ReadJSONfromFile("test")))
    return

def Menu(g):
    print("-"*40)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t1 - Enter Graph\n\t2 - Read Graph from file\n\t3 - Write Graph to file\n\t4 - Print currently loaded Graph\n\t5 - Quit")
    print("-"*40)
    if g == None:
        print("GRAPH LOADED: FALSE")
    else:
        print("GRAPH LOADED: TRUE")
    print("-"*40)
    return int(input(">>"))

#TestRun()
graph = None
while(1):
    try:
        x = Menu(graph)
    except:
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    if x == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            if int(input("\t1 - Directional\n\t2 - Undirectional\n" + "-"*40 + "\n>>")) == 2:
                graph = UserDefineGraphUndirectional()
            else:
                graph = UserDefineGraphDirectional()
        except:
            print("ERROR")
            input("\nPress ENTER to go back to Menu")
            
        os.system('cls' if os.name == 'nt' else 'clear')
    elif x == 2:
        try:
            graph = JSONtoGraph(ReadJSONfromFile(input("File name (Without extension) : ")))
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: Unable to Read file")
            input("\nPress ENTER to go back to Menu")
    elif x == 3:
        try:
            WriteJSONtoFile(input("File name (Without extension) : "), GraphtoJSON(graph))
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("ERROR: Unable to Read file")
            input("\nPress ENTER to go back to Menu")            
    elif x == 4:
        try:
            PrintGraph(graph)
        except:
            print("ERROR: Unable to Print Graph")
        input("\nPress ENTER to go back to Menu")
    elif x == 5:
        break
    x = 5

from graphics import *

#win = GraphWin()

#pt = Point(100,100)

#pt.draw(win)
#win.getKey()

##cir = Circle(pt, 50)
##cir.setFill('blue')
##cir.draw(win)

#line = Line(pt, Point(50,50))

#line.draw(win)

#win.getKey()
#line.move(10, 40)
#win.getKey()

#print(line)

#win = GraphWin('Face', 200, 150) # give title and dimensions

#head = Circle(Point(40,100), 25) # set center and radius
#head.setFill("yellow")
#head.draw(win)

#eye1 = Circle(Point(30, 105), 5)
#eye1.setFill('blue')
#eye1.draw(win)

#eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
#eye2.setWidth(3)
#eye2.draw(win)

#mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
#mouth.setFill("red")
#mouth.draw(win)

#label = Text(Point(100, 120), 'A face')
#label.draw(win)

#message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
#message.draw(win)
#win.getMouse()
#win.close()
