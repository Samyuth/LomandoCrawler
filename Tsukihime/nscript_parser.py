# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 02:05:23 2022

@author: Sagi
"""

import requests
import bs4

# Gets all the valid encodings from python 3 for Japanese
# Takes as input a list of valid languages eg. ["Japanese"] and
# optionally a flag to test every encoding or not
# Returns a tuple with a list of valid encodings and their aliases
def get_language_encodings(valid_langs, every=False):
    
    encodings = []
    aliases = []
    
    response = requests.get("https://docs.python.org/3.7/library/codecs.html#standard-encodings")
    
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
    
    return (encodings, aliases)

# Function to try a single encoding
# Takes as input an encoding
# Returns true if the encoding is valid, false if not
def try_encoding(encoding):
    try:
        nscript = open("nscript.dat", encoding=encoding)
        nscript.readline()
        nscript.close()
        return True

    except:
        return False

# Function to try all encodings
# Returns a list of all valid encodings
def try_encodings():
    encodings, aliases = get_language_encodings(["Japanese", "all languages"], True)
    valid_encodings = []
    
    for encoding in encodings:
        if (try_encoding(encoding)):
            valid_encodings.append(encoding)
    
    return valid_encodings
            
    
if __name__ == "__main__":
    valid_encodings = try_encodings()
    
    print(valid_encodings)

    nscript = open("nscript.dat", encoding="cp932")