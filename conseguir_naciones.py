import requests
from bs4 import BeautifulSoup

def conseguir_paises(s):
    home_page = 'https://fmdataba.com/'
    page = s.get(home_page,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    soup = BeautifulSoup(page.text, 'html.parser')
    if page.status_code==200:
        table = soup.find_all('select',attrs={'class':'gitt form-control'})
        #print(len(table))
        trs = table[-1].find_all('option')
        #print (len(trs))
        paises = [paises.text for paises in trs]
        #print (len(paises))
        #print(paises[8])
        #indices = [i for i, s in enumerate(paises) if 'Argentina' in s]
        paises_links = [tr.get('value') for tr in trs]
        #print (len(paises_links))
        #print(paises_links[indices[0]])
        #paises_dict = {} 
        #for pais in paises: 
        #    for link in paises_links: 
        #        paises_dict[pais] = link 
        #        paises_links.remove(link) 
        #        break  
        #return paises_dict
        return paises, paises_links
    return [], []