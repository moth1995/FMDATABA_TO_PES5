import requests
from bs4 import BeautifulSoup

def conseguir_equipos(s,liga):
    #equipos = 'https://fmdataba.com/20/l/199/primera-division/best-players/'
    page = s.get(liga,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    if page.status_code==200:
        soup = BeautifulSoup(page.text, 'html.parser')
        equipos_table = soup.find_all('table',attrs={'class':'table table-striped','style':'margin-bottom: 0px;'})
        #print(len(equipos_table))
        tds = equipos_table[-3].find_all('a')
        #print (len(tds))
        equipos = [equipos.text for equipos in tds]
        #print (len(equipos))
        #print(equipos[0])
        equipos_links = [td.get('href') for td in tds]
        #print (len(equipos_links))
        #print(equipos_links[0])
        return equipos, equipos_links
    return [],[]