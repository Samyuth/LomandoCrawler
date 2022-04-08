# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:50:22 2022

@author: Sagi
"""

import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import numpy as np
import json

class Graph:
    # Constructor
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.network = Network()
    
    # Method to plot digraph with matplotlib
    def plot(self, figsize):
        pos = nx.spring_layout(self.graph, scale=20, k=3/np.sqrt(self.graph.order()))
        plt.figure(3,figsize=figsize)
        nx.draw(self.graph, pos, with_labels=True)
    
    # Method to plot digraph with pyvis
    def plot_pretty(self):
        net = Network()
        net.from_nx(self.graph)
        net.show("visual.html")
        self.network = net
    
    # Method to output the network x json
    def output_network_json(self):
        data = dict()
        data["nodes"] = self.network.nodes
        data["edges"] = self.network.edges
        with open("network.json", "w") as outfile:
            outfile.write(json.dumps(data, indent=4))