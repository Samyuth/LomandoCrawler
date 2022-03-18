# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:12:37 2022

Utility file with functions to test every python encodoing
on a specific file

@author: Sagi
"""

import requests
import bs4
from sys import version_info

# Gets all valid encodings for a specific python version from the python docs
def get_all_encodings():
    
    encodings = []
    encoding_tables = []
    
    response = requests.get("https://docs.python.org/%d.%d/library/codecs.html" % (version_info.major, version_info.minor))
    
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
    tables = soup.findAll("table", {"class": "docutils align-default"})
    
    for table in tables:
        headers = table.find("thead").findAll("th")
        
        if (headers[0].text == "Codec"):
            encoding_tables.append(table)

    for encoding_table in encoding_tables:
        for row in encoding_table.findAll("tr"):
            cells = row.findAll("td")
            
            if (len(cells) > 0):
                encodings.append(cells[0].text)
    
    return encodings

# Gets all the valid encodings from python docs for a specific set of languages from the python docs
# Takes as input a list of valid languages eg. ["Japanese"] and
# optionally a flag to test every encoding or not
# Returns a list of current python encodings
def get_language_encodings(valid_langs, every=False):
    
    encodings = []
    
    response = requests.get("https://docs.python.org/%d.%d/library/codecs.html" % (version_info.major, version_info.minor))
    
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
    tables = soup.findAll("table", {"class": "docutils align-default"})
    
    for table in tables:
        headers = table.find("thead").findAll("th")
        
        if (headers[0].text == "Codec" and headers[2].text == "Languages"):
            encoding_table = table
    
    for row in encoding_table.findAll("tr"):
        cells = row.findAll("td")
        
        if (len(cells) > 0 and ((cells[2].text in valid_langs) or every == True)):
            encodings.append(cells[0].text)
    
    return encodings

# Function to try a single encoding
# Takes as input an encoding and the absolute path file to try
# Returns true if the encoding is valid, false if not
def try_encoding(encoding, filename):
    try:
        nscript = open(filename, encoding=encoding)
    except:
        return False
    
    try:
        nscript.readline()
    except:
        return False
    
    try:
        nscript.close()
        return True
    except:
        return False

# Function to try all language encodings
# Takes as input filename to try
# Returns a list of all valid encodings
def try_language_encodings(filename):
    encodings = get_language_encodings([], True)
    valid_encodings = []
    
    for encoding in encodings:
        if (try_encoding(encoding, filename)):
            valid_encodings.append(encoding)
    
    return valid_encodings

# Function to try Japanses language encodings
# Takes as input filename to try
# Returns a list of the valid encodings
def try_japanese_encodings(filename):
    encodings = get_language_encodings([], True)
    valid_encodings = []
    
    for encoding in encodings:
        if (try_encoding(encoding, filename)):
            valid_encodings.append(encoding)
    
    return valid_encodings

if __name__ == "__main__":
    valid_encodings = get_all_encodings()
    
    print(valid_encodings)