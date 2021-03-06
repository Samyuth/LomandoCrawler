import requests
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import numpy as np
from Graph import *

import os
import re

class Crawler(Graph):
    # Constructor
    def __init__(self, template, root_page):
        self.template = template
        self.root_page = root_page
        self.pages = set()
        self.graph = nx.MultiDiGraph()
        self.network = Network()

    # Method to parse url and extract html
    def parse(self, page):
        '''
        cmd = 'curl https://lomando.com/main.html | grep "\.html"'

        os.system(cmd)
        '''
    
        response = requests.get(self.template + page)
        
        return re.findall("[a-zA-Z]+\.html", response.text)
    
    # Method to create the directed graph (BFS)
    def crawl(self):
        # Initializing queue with root
        queue = [self.root_page]

        # Going till queue empty
        while (len(queue) > 0):
            parent = queue.pop(0)
            
            # Adding to pages and queue
            self.pages.add(parent)
            children = set(self.parse(parent))
            queue = queue + list(children - self.pages)
            
            # Adding graph nodes and edges
            self.graph.add_node(parent)
            for child in children:
                self.graph.add_edge(parent, child)
    
    # Method to return a sorted list of the visited pages
    def sorted_pages(self):
        return sorted(list(self.pages))

if __name__ == "__main__":
    
    # Initializing
    print("Testing initialization:")
    crawler = Crawler("https://lomando.com/", "main.html")
    print(crawler.template + crawler.root_page)
    print()
    
    # Test for parse method
    print("Testing parse function:")
    print(crawler.parse("main.html"))
    print(set(crawler.parse("main.html")))
    print()

    # Test for crawl method
    print("Testing crawl funciton:")
    crawler.crawl()
    print(crawler.sorted_pages())
    print(crawler.graph)
 
    # Testing draw with matplotlib
    crawler.plot()
    
    # Testing draw with pyvis
    crawler.plot_pretty()
