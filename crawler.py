import requests
import os
import re

def crawl():
    print(parse("https://lomando.com/"))

def parse(url):
    '''
    cmd = 'curl https://lomando.com/main.html | grep "\.html"'
    
    os.system(cmd)
    '''

    response = requests.get("https://lomando.com/")
    
    return re.findall("[a-zA-Z]+\.html", response.text)

if __name__ == "__main__":
    crawl()
