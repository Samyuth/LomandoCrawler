# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:37:45 2022

Utility file to convert script to an html document

@author: Sagi
"""

import bs4
import re

doc_start = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Script</title>
</head>
<body>
'''
    
doc_end = '''</body>
</html>'''

# gets all labels in the nscripter script
# takes as input absolute path nscripter script
# returns a list of labels
def get_all_labels(filename):
    nscript = open(filename, encoding="cp932")

    labels = []

    line = nscript.readline()
    while (line):
        if re.match("^\*", line):
            labels.append(line)
        line = nscript.readline()
        
    nscript.close()
    
    return labels

#writes to an html file
def write_to_doc(filename):
    nscript = open(filename, "r",encoding="cp932")
    script = open("script.html", "w", encoding="cp932")
    script.write(doc_start)

    lines = []
    labels = set([label.strip() for label in get_all_labels(filename)])

    line = nscript.readline()
    while (line):
        if re.match("^\*", line):
            line = f'<div id="{line.strip()}">{line}</div>'
            lines.append(line)
        else:
            labels_in_line = re.findall(r"\*[a-z, A-Z, 0-9]+", line)
            for label in labels_in_line:
                if label.strip() in labels:
                    line = line.replace(label.strip(), f'<a href="#{label.strip()}">{label}</a>')
        
        script.write(line)
        script.write("<br>")
        
        line = nscript.readline()
    
    script.write(doc_end)  
    script.close()
    nscript.close()
    
    return lines, labels
    
if __name__ == "__main__":
    lines, labels = write_to_doc("../nsdec/NSDEC/result.txt")
    
    labels = sorted(list(labels))