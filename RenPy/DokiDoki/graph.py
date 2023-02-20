# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:50:22 2022
@author: Sagi
"""

import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import numpy as np

'''
Ascii format for leveled tree
   |- B --- D --- E --- F
A -|
   |- C --- D
Z --- C
// on move to next child pos+= 2
0              |- G   <-- pos_b, pos_c, pos_g
1        |- C -|
2  |- B -|     |- H    <-- pos_h        // pos + first_child.width // 2
3  |     |
4  |     |- D          <-- pos_d
A -|
6  |     |- F         <-- pos_e, pos_f
7  |- E -|           // pos + node.width - 1 - last_child.width // 2
8        |- I --- J        <-- pos_i
'''

class Graph:
    # Constructor
    def __init__(self, graph=None):
        if graph is not None:
            self.graph = graph
            self.network = Network()
            self.network.from_nx(graph)
        else:
            self.graph = nx.MultiDiGraph()
            self.network = Network()
        self._levels = []
        self._found = set()
        self._num_descendents = dict()
        self.__rows = None

    # Method to plot digraph with matplotlib
    def plot(self):
        pos = nx.spring_layout(self.graph, scale=20, k=3/np.sqrt(self.graph.order()))
        plt.figure(3,figsize=(20,40))
        nx.draw(self.graph, pos, with_labels=True)

    # Method to plot digraph with pyvis
    def plot_pretty(self):
        net = Network()
        net.from_nx(self.graph)
        net.show("visual.html")
        self.network = net
        
    # Method to find sources
    def find_sources(self):
        sources = []
        for node in self.graph.nodes:
            if len(self.graph.in_edges(node)) == 0:
                sources.append(node)
        return sources
    
    # Generates the a tree structure that is leveled
    def __tree_generator(self, depth, node):
        if depth == len(self._levels):
            self._levels.append([])
        
        self._levels[depth].append(node)
        
        out_edges = self.graph.out_edges(node)
        
        if len(out_edges) == 0 or node in self._found:
            return
        
        self._found.add(node)
        
        for edge in out_edges:
            self.__tree_generator(depth+1, edge[1])
    
    # Recursively obtain the leaves obrained for all nodes in a path
    def __find_num_descendents(self, node):
        out_edges = self.graph.out_edges(node)
        
        # only increment if you reach a leaf
        if len(out_edges) == 0:
            self._num_descendents[node] = 0
            return 1
        elif node in self._num_descendents:
            return 0
        
        self._num_descendents[node] = 0
        
        for edge in out_edges:
            # Memoizing
            if edge[1] in self._num_descendents:
                self._num_descendents[node] += 1
            else:
                self._num_descendents[node] += self.__find_num_descendents(edge[1])
        
        return self._num_descendents[node]
    
    def get_num_descendents(self):
        return self._num_descendents
        
    # Returns a leveled tree structure
    # Driver function for generation algorithm
    def _create_leveled_tree(self):
        sources = self.find_sources()
        # Call the builder functions for each of the starting nodes
        for node in sources:
            self.__tree_generator(0, node)
            self.__find_num_descendents(node)
           
    # getting the max level size as well as label length
    def __get_max_level_size(self):
        if (len(self._levels) == 0):
            self._create_leveled_tree()
        # getting max width by number of leaf nodes for root nodes
        max_width = sum([self._num_descendents[node] for node in self._levels[0]])
        # getting max node label width width
        max_len = max([len(node) for node in self.graph.nodes])
        return (max_width, max_len)
    
    # Recursively building out a tree from a node
    # takes as an argument the starting position
    def __build_tree_string(self, node, pos, max_len, depth):
        children = [edge[1] for edge in self.graph.out_edges(node)]
        
        # leaf node case
        if len(children) == 0 or node in self._found:
            # adding to the found set
            self._found.add(node)
            # printing out
            outstr = "{0:^{1}}".format(node, max_len)
            for i in range(max_len):
                self.__rows[pos][depth*(max_len + 5)+i] = outstr[i]
            # incrementing position
            return pos + 2  
        
        self._found.add(node)
        
        node_width = 2 * self._num_descendents[node] - 1
        
        # getting the width hanging out from the first child and last child subtree
        if (2*self._num_descendents[children[0]]-1)//2 == -1:
            first_child_pos = pos
        else:
            first_child_pos = pos + (2*self._num_descendents[children[0]]-1)//2
        if (2*self._num_descendents[children[-1]]-1)//2 == -1:
            last_child_pos = pos + node_width - 1
        else:
            last_child_pos = pos + node_width - 1 - (2*self._num_descendents[children[-1]]-1)//2
        node_pos = first_child_pos + (last_child_pos - first_child_pos)//2

        # Setting the node by copying
        outstr = "{0:^{1}}".format(node, max_len)
        for i in range(max_len):
            self.__rows[node_pos][depth*(max_len + 5)+i] = outstr[i]
        # Printing line from node
        if (len(children) == 1):
            self.__rows[node_pos][depth*(max_len + 5)+ max_len + 1] = "-"
            self.__rows[node_pos][depth*(max_len + 5)+ max_len + 2] = "-"
            self.__rows[node_pos][depth*(max_len + 5)+ max_len + 3] = "-"
        elif (len(children) > 1):
            self.__rows[node_pos][depth*(max_len + 5)+ max_len + 1] = "-"
            # When there are multiplie children print a flat line
            for i in range(first_child_pos, last_child_pos+1):
                self.__rows[i][depth*(max_len + 5)+ max_len + 2] = "|"
        # Print a dash at the location of the child node and call child
        for child in children:
            if (2*self._num_descendents[child]-1)//2 == - 1:
                child_pos = pos
            else:
                child_pos = pos + (2*self._num_descendents[child]-1)//2
            self.__rows[child_pos][depth*(max_len + 5)+ max_len + 3] = "-"
            pos = self.__build_tree_string(child, pos, max_len, depth+1)

        return pos
    
    # Getter for the leveled tree structure
    def get_leveled_tree(self):
        self._create_leveled_tree()
        return self._levels

    # Sideways tree output
    def __str__(self):
        max_width, max_len = self.__get_max_level_size()
        
        # Initializing variables
        depth = len(self._levels)
        str_depth = (5*(depth-1) + max_len * depth)
        self.__rows = [[" "] * str_depth for i in range(2 * max_width - 1)]
        self._found = set()

        pos = 0
        for node in self._levels[0]:
            pos = self.__build_tree_string(node, pos, max_len, 0)
        
        return "\n".join(["".join(self.__rows[i]) for i in range(len(self.__rows))])
        
if __name__ == "__main__":
    graph = nx.MultiDiGraph()
    graph.add_node("abc")
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")
    graph.add_node("f")
    graph.add_node("z")
    graph.add_edge("b", "abc")
    graph.add_edge("b", "a")
    graph.add_edge("b", "c")
    graph.add_edge("c", "d")
    graph.add_edge("abc", "d")
    graph.add_edge("d", "e")
    graph.add_edge("e", "f")  
    graph.add_edge("z", "c")
    
    true_graph = Graph(graph)
    
    #print(true_graph.get_leveled_tree())
    print(true_graph)
    #print(true_graph.get_num_descendents())
    
    graph2 = nx.MultiDiGraph()
    graph2.add_node("a")
    graph2.add_node("b")
    graph2.add_node("c")
    graph2.add_node("d")
    graph2.add_node("e")
    graph2.add_node("f")
    graph2.add_node("g")
    graph2.add_node("h")
    graph2.add_node("i")
    graph2.add_node("j")
    graph2.add_edge("a", "b")
    graph2.add_edge("a", "e")
    graph2.add_edge("e", "f")
    graph2.add_edge("e", "i")
    graph2.add_edge("i", "j")
    graph2.add_edge("b", "c")
    graph2.add_edge("b", "d")
    graph2.add_edge("c", "g")
    graph2.add_edge("c", "h")
    
    true_graph = Graph(graph2)
    
    print(true_graph)
