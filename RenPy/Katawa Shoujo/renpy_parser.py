from Graph import *
import re

graph = nx.MultiDiGraph()

f = open("RenPy\\Katawa Shoujo\\imachine.rpy", "r")
visited = []
branchlist = []
choice_dictionary = {}
prevline = ""
for line in f:
    
    if prevline != "":
        line = prevline
        prevline = ""
    splitline = line.split(" ")
    #print(splitline)
    if splitline[0] in "label":
        nodename = splitline[1].strip()
        nodename = nodename[:-1]
        #print(nodename)
        if nodename not in visited:
            graph.add_node(nodename)
            visited.append(nodename)
        for branch in branchlist:
            print(branch)
            graph.add_edge(branch, nodename)
        choice_dictionary[nodename] = set()
        loop = True
        branchlist = []
        while(loop == True):
            line = f.readline()
            if "jump_out" in line:
                jumpline = line.split("jump_out")
                secondnode = jumpline[1][1:].strip()
                #print(secondnode)
                choice_dictionary[nodename].add(secondnode)
                if secondnode not in visited and "restart" not in secondnode:
                    graph.add_node(secondnode)
                    visited.append(secondnode)
                #print("{} | {}".format(nodename, secondnode))
                if "restart" not in secondnode:
                    graph.add_edge(nodename, secondnode)
            elif "iscene" in line:
                isceneline = line.split("iscene")
                secondnode = isceneline[1].strip()
                secondnode = re.findall('"([^"]*)"', secondnode)[0]
                #print(secondnode)
                choice_dictionary[nodename].add(secondnode)
                if secondnode not in visited:
                    graph.add_node(secondnode)
                    visited.append(secondnode)
                if(secondnode != nodename):
                    #print("{} | {}".format(nodename, secondnode))
                    graph.add_edge(nodename, secondnode)
                    branchlist.append(secondnode)
            if "label" in line:
                loop = False
            if "# Decompiled by unrpyc:" in line:
                loop = False
        prevline = line
        
#print(choice_dictionary)
actual_graph = Graph(graph)
#print(visited)
actual_graph.plot_pretty()
#print(actual_graph)

    

