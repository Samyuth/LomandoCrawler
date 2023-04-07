import re
from Graph import *
import json

class TextNode():
    def __init__(self, label=None, call=None,jump=None,text=None, children=None):
        if label is not None:
            self.label = label
        else:
            self.label = None
        if call is not None:
            self.call = call
        else:
            self.call = None
        if jump is not None:
            self.jump = jump
        else:
            self.jump = None
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
    def get_call(self):
        if self.call:
            return self.call
        else:
            return None
    def get_jump(self):
        if self.jump:
            return self.jump
        else:
            return None
    def add_text(self, text):
        self.text += text

    def change_label(self, label):
        self.label = label
    def change_call(self, call):
        self.call = call
    def change_jump(self, jump):
        self.jump = jump
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

class DokiDokiNode(TextNode):
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
            
