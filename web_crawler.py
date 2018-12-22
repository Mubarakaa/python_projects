# -*- coding: utf-8 -*-
"""

Author - Mubaraka Bharucha
"""

import requests
from bs4 import BeautifulSoup
import time
import urllib

def continue_crawl(search_history, target_url, max_steps):
    if search_history[-1] == target_url:
        print("We have found the target article")
        return False
    elif len(search_history) > max_steps :
        print("Crawling limit exceeded")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("Running in a loop. Aborting...")
        return False
    else:
        return True
    
    
def find_first_link(page_link):
    
    response = requests.get(page_link)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    for x in soup.find(id="mw-content-text").div: 
        if x.name == 'p' and x.find('a'):
            href = x.a.get('href')
            return urllib.parse.urljoin('https://en.wikipedia.org/', href)
    


start_link = 'https://en.wikipedia.org/wiki/Dead_Parrot_sketch'
end_link = 'https://en.wikipedia.org/wiki/Science'

search_history = [start_link]

while continue_crawl(search_history, end_link, 25): 
    
    link = find_first_link(search_history[-1])
    print(link)
    if not link:
        print("This article has no links. Aborting...")
        break
    
    search_history.append(link)
    
    time.sleep(2)



        
        




