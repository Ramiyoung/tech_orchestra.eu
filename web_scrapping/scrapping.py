# scrapper.py
import requests, sys, pprint, re, scrapping
from bs4 import BeautifulSoup

links = []
def scrapper(websites, depth):
    for w in websites:
        try:
            page = requests.get(w)
            status_code = page.status_code
        except:
            pass
        else:
            if re.match('4', str(page.status_code)) or re.match('5', str(page.status_code)):
                pass
            else:
                wsu = w.split('/')
                print("[{position}]: {website}".format(position=websites.index(w), website=w))
                p_wsu = [e for e in wsu if "http" not in e ]
                domparam = list(filter(None, p_wsu))
                html_file = ('-'.join(domparam))
                
                soup = BeautifulSoup(page.content, "html.parser")
                for link in soup.find_all('a'):
                    if not isinstance (link.get('href'), type(None)) : 
                        if not re.match('#', link.get('href')):
                            if re.match('/',link.get('href')):
                                links.append(w + link.get('href'))
                            else:
                                links.append(link.get('href'))
    return links

            #f = open(html_file + '.html', "w")
            #f.write(str(soup))
            #f.close()