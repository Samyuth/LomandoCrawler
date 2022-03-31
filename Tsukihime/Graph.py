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
    
    def _tree_generator(self, depth, node):
        if depth == len(self._levels):
            self._levels.append([])
        
        self._levels[depth].append(node)
        
        out_edges = self.graph.out_edges(node)
        
        if len(out_edges) == 0 or node in self._found:
            return
        
        self._found.add(node)
        
        for edge in out_edges:
            self._tree_generator(depth+1, edge[1])
        
    # Returns a leveled tree structure
    # Driver function for generation algorithm
    def _create_leveled_tree(self):
        sources = self.find_sources()
        # DFS for all the starting nodes
        for node in sources:
            self._tree_generator(0, node)
           
    # getting the max level size as well as label length
    def __get_max_level_size(self):
        if (len(self._levels) == 0):
            self._create_leveled_tree()
        max_size = 0
        # getting max width
        for level in self._levels:
            if len(level) > max_size:
                max_size = len(level)
        # getting max node label width width
        max_len = max([len(node) for node in graph.nodes])
        return (max_size, max_len)
    
    # Calculating sideways tree string array
    def __format_leveled_tree_sideways(self):
        max_size, max_len = self.__get_max_level_size()
        
        # output array
        rows = [""] * (2 * max_size - 1)
        
        # set for if the node has already been printed or not
        found = set()
        
        # populating the array
        for level in self._levels:
            pos = 0
            for node in level:
                # width to print
                width = 2*len(self.graph.out_edges(node)) - 1
                # if the node has no children or it was already printed
                if width == -1 or node in found:
                    rows[pos] += "{0:^{1}}".format(node, max_len)
                    found.add(node)
                    continue  
                
                for i in range(width):
                    # print of actual node
                    if i == width // 2:
                        rows[pos] += "{0:^{1}}".format(node, max_len) + " -"
                    else:
                        rows[pos] += " " * max_len + "  "
                    
                    # print pipe if tree has multiple children
                    if width > 1:
                        rows[pos] += "|"
                    else:
                        rows[pos] += "-"
                       
                    # print dash if it leads to a child node
                    if i % 2 == 0:
                        rows[pos] += "- "
                    else:
                        rows[pos] += "  "
                        
                    pos += 1
                
                found.add(node)
                pos += 1
        
        return rows
    
    # Calculating vertical tree string array
    def __format_leveled_tree_vertical(self):
        max_size = self.__get_max_level_size()
    
    # Sideways tree output
    def output_tree_sideways(self):
        rows = self.__format_leveled_tree_sideways()
        
        return "\n".join(rows)
    
    # Getter for the leveled tree structure
    def get_leveled_tree(self):
        self._create_leveled_tree()
        return self._levels
    
        
if __name__ == "__main__":
    graph = nx.MultiDiGraph()
    graph.add_node("abc")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")
    graph.add_node("f")
    graph.add_node("z")
    graph.add_edge("b", "abc")
    graph.add_edge("b", "c")
    graph.add_edge("c", "d")
    graph.add_edge("abc", "d")
    graph.add_edge("d", "e")
    graph.add_edge("e", "f")  
    graph.add_edge("z", "c")
    
    true_graph = Graph(graph)
    
    print(true_graph.get_leveled_tree())
    print(true_graph.output_tree_sideways())