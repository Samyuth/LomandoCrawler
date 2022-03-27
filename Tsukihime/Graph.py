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
  |-B---D
A-|
  |-C---D---E

Z---C

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
        self.__levels = []
        self.__found = set()

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
    
    def __tree_generator(self, depth, node):
        if depth == len(self.__levels):
            self.__levels.append([])
        
        self.__levels[depth].append(node)
        
        out_edges = self.graph.out_edges(node)
        
        if len(out_edges) == 0 or node in self.__found:
            return
        
        self.__found.add(node)
        
        for edge in out_edges:
            self.__tree_generator(depth+1, edge[1])
        
    # Returns a leveled tree structure
    # Driver function for generation algorithm
    def __create_leveled_tree(self):
        sources = self.find_sources()
        # DFS for all the starting nodes
        for node in sources:
            self.__tree_generator(0, node)
    
    # Getter for the leveled tree structure
    def get_leveled_tree(self):
        self.__create_leveled_tree()
        return self.__levels
        
if __name__ == "__main__":
    graph = nx.MultiDiGraph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("b", "a")
    graph.add_edge("b", "c")
    
    true_graph = Graph(graph)
    
    print(true_graph.get_leveled_tree())