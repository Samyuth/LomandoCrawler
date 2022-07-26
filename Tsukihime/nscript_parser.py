# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 02:05:23 2022

@author: Sagi
"""

'''
Sample choice node text:
;-BLOCK-------------------------------------------------------------------------
*f20 # Label 
gosub *regard_update
!sd
if %sceneskip==1 && %1020==1 skip 4
gosub *s20
mov %1020,1
skip 9
`You have already viewed this scene.
`Would you like to skip?
br
selgosub `1. Skip`, *skip20,
	`2. Don't skip`, *s20
skip 3
*skip20
return
;gosub *s20
select `1. There's only a few minutes until homeroom. I have to head there right away.`, *f21,
	`2. || I'm curious, so I'll go take a look.`, *f22


'''

import re
from Graph import *

class TextNode():
    def __init__(self, label=None, text=None, children=None):
        if label is not None:
            self.label = label
        else:
            self.label = None

        if text is not None:
            self.text = text
        else:
            self.text = ""
        
        if children is not None:
            self.children = children
        else:
            self.children = []
            
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
    
    def add_children(self, children):
        self.children += children

class ChoiceNode(TextNode):
    def add_choices(self, choices):
        self.choices = choices
    
    def get_choices(self):
        if self.choices:
            return self.choices
        else:
            return None

class TsukihimeNode(TextNode):
    def get_labels(self, string):
        return re.findall("\*.*(?=,)|\*.*(?=\s)|\*.*", string)
    
    def parse_text(self):
        if self.text is None:
            print("No text to parse")
            return -1
        
        line_ctr = 0
        lines = self.text.splitlines()
        no_lines = len(lines)
        while (line_ctr < no_lines):
            if lines[line_ctr].find("select") != -1:
                children = []   
                while (line_ctr < no_lines
                       and re.search("`[0-9].*`", lines[line_ctr])):
                    children += self.get_labels(lines[line_ctr])
                    line_ctr += 1
                self.add_children(children)
            elif lines[line_ctr].find("goto") != -1:
                self.add_children(self.get_labels(lines[line_ctr]))
            
            line_ctr += 1
            
class NscriptParser(Graph):
    # method to parse the script
    def parse(self):
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
            if re.match("\*f.*", line):
                nodes_present = True
                choice_nodes.append(TsukihimeNode(text=""))
            if nodes_present:
                choice_nodes[-1].add_text(line)
            if re.match("^\*f", line):
                choice_nodes[-1].change_label(line.strip())
    
            choices.writelines(line)
            line = nscript.readline()
        
        while (line):
            if re.match("^\*", line):
                nodes.append(TextNode(line))
            remaining.writelines(line)
            line = nscript.readline()        

        nscript.close()
        header.close()
        remaining.close()
        choices.close()

        choice_nodes = list(filter(lambda x: x.get_label() is not None, choice_nodes))
        for node in choice_nodes:
            node.parse_text()
        
        for node in choice_nodes:
            self.graph.add_node(node.label)
            for child in node.children:
                if child not in self.graph:
                    self.graph.add_node(child)
                self.graph.add_edge(node.label, child)
        
        return choice_nodes
    
if __name__ == "__main__":
    
    parser = NscriptParser()
    choice_nodes = parser.parse()
    
    leveled_tree = parser.get_leveled_tree()
    output = parser.output_tree_sideways()
    '''
    with open("ouput.txt", "w") as outfile:
        outfile.write(output)
    '''
    #parser.plot()
    #parser.plot_pretty()
