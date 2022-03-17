# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 02:05:23 2022

@author: Sagi
"""

import re

class Node():
    def __init__(self, label=None, text=None):
        if label is not None:
            self.label = label
        else:
            self.label = None

        if text is not None:
            self.text = text
        else:
            self.text = None
            
    def get_text(self):
        if self.text:
            return self.text
        else:
            return None

    def get_label(self):
        if self.label:
            return self.label
        else:
            return None
    
    def add_text(self, text):
        self.text += text

    def change_label(self, label):
        self.label = label

class ChoiceNode(Node):
    pass
    
if __name__ == "__main__":
    #valid_encodings = try_encodings()
    
    #print(valid_encodings)

    nscript = open("./nsdec/NSDEC/result.txt", encoding="cp932")
    line = nscript.readline()
    
    header = open("./parsed_texts/header.txt", "w", encoding="cp932")
    remaining = open("./parsed_texts/remaining.txt", "w", encoding="cp932")
    choices = open("./parsed_texts/choices.txt", "w", encoding="cp932")
    
    choice_nodes = []
    nodes = []
    nodes_present = False

    while (line and line.strip() != "*start"):
        header.writelines(line)
        line = nscript.readline()
    
    while (line and line.strip() != "; $Id: 4.txt 1282 2006-08-04 18:12:29Z chendo $"):
        if re.match("^;-BLOCK.*$", line):
            nodes_present = True
            choice_nodes.append(ChoiceNode(text=""))
        if nodes_present:
            choice_nodes[-1].add_text(line)
        if re.match("^\*f", line):
            choice_nodes[-1].change_label(line.strip())

        choices.writelines(line)
        line = nscript.readline()
    
    nodes_size = 0
    
    while (line):
        if re.match("^\*", line):
            nodes.append(Node(line))
        remaining.writelines(line)
        line = nscript.readline()        

    nscript.close()
    header.close()
    remaining.close()
    choices.close()
    
    choice_nodes = list(filter(lambda x: x.get_label() is not None, choice_nodes))