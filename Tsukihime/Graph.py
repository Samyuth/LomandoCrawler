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
        
    # Using BFS to generate a leveled tree
    def _create_leveled_tree(self):
        # Use BFS to generate a leveled tree
        queue1 = [[node, None] for node in self.find_sources()] # first index is the node, second is the parent
        queue2 = []
        self._found = set()
        while (len(queue1) > 0 or len(queue2) > 0):
            self._levels.append([]) # adding a new level
            # doing the search on a queue
            while(len(queue1) > 0):
                node = queue1.pop(0)

                # Continuing the search or denoting a node as a reference
                if (node[0] in self._found):
                    node.append(False)
                    self.graph.remove_edge(node[1], node[0])
                    # self.graph.remove_edges_from(list(self.graph.out_edges(node[0])))
                else:
                    node.append(True)
                    self._found.add(node[0])
                    for edge in list(self.graph.out_edges(node[0])):
                        queue2.append([edge[1], edge[0]])
                
                # Adding to the level
                self._levels[-1].append(node)

            # Swapping queues
            queue1 = queue2
            queue2 = []

    # Getter for the leveled tree structure
    def get_leveled_tree(self):
        self._create_leveled_tree()
        return self._levels

    # Sideways tree output
    def __str__(self):
        # Creating the leveled tree
        self._create_leveled_tree()

        # # Getting the width and depth
        # width = sum([trimmed._num_descendents[node[0]] for node in trimmed._levels[0]])
        # depth = len(trimmed._levels)

        # # Creating the final mapping
        # node_mapping = dict()
        # parent = None
        # for i in range(len(trimmed._levels)):
        #     start = 0
        #     for node in trimmed._levels[i]:
        #         # Finding the parent
        #         old_parent = parent
        #         parent = list(trimmed.graph.in_edges(node))
        #         print(parent)
        #         if len(parent) > 0:
        #             parent = parent[0][0]
        #         else:
        #             parent = False

        #         # Checking if the parent is the same as the previous node
        #         if old_parent == parent:
        #             parent = False

        #         # Updating the start if needed
        #         if parent and parent in node_mapping:
        #             start = node_mapping[parent][1]

        #         # Calculaitons for the coordinates
        #         end = start + (1 if (node[1] == False or trimmed._num_descendents[node[0]] == 0)
        #             else trimmed._num_descendents[node[0]])

        #         node.append(start) # start x
        #         node.append(end) # end x
        #         node.append(i) # y

        #         start = end

        #         # Updating the node mapping
        #         node_mapping[node[0]] = node[1:]

        output = ""
        for level in self._levels:
            output += str(level) + "\n"
        
        return output
        
if __name__ == "__main__":
    graph = nx.MultiDiGraph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")
    graph.add_node("f")
    graph.add_node("z")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    graph.add_edge("z", "c")
    graph.add_edge("b", "d")
    graph.add_edge("c", "d")
    graph.add_edge("d", "e")
    graph.add_edge("e", "f")
    
    true_graph = Graph(graph)
    
    #print(true_graph.get_leveled_tree())
    print(true_graph)
    #print(true_graph.get_num_descendents())
    # true_graph.plot_pretty()
    
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