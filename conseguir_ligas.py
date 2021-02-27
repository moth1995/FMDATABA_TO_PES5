import requests
from bs4 import BeautifulSoup

def conseguir_ligas(s,ligas_paises):
    #ligas_paises = 'https://fmdataba.com/20/n/9/argentina/best-players/'
    page1 = s.get(ligas_paises,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    soup1 = BeautifulSoup(page1.text, 'html.parser')
    if page1.status_code==200:
        liga_table = soup1.find_all('table',attrs={'class':'table table-striped','style':'margin-bottom: 0px;'})
        #print(len(liga_table))
        tds = liga_table[-2].find_all('a')
        #print (len(tds))
        divisiones = [divisiones.text for divisiones in tds]
        #print (len(divisiones))
        #print(divisiones)
        divisiones_links = [td.get('href') for td in tds]
        #print (len(divisiones_links))
        #print(divisiones_links)
        return divisiones, divisiones_links
    return [],[]
