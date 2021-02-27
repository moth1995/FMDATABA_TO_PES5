import requests
from bs4 import BeautifulSoup

def conseguir_jugadores(equipo,s):
    page = s.get(equipo,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    if page.status_code==200:
        soup = BeautifulSoup(page.text, 'html.parser')
        jugadores_table = soup.find_all('table',attrs={'class':'table table-striped','id':"tablo61",'style':'margin-bottom: 0px;'})[0].find_all('tbody')[0].find_all('td',attrs={'style':'font-size:12px;'})
        equipos_misma_liga = soup.find_all('table',attrs={'class':'table table-striped','style':'margin-bottom: 0px;'})[1]
        equipos_misma_liga_links = [links.get('href') for links in equipos_misma_liga.find_all('a')]
        equipos_misma_liga_nombres = [links.text for links in equipos_misma_liga.find_all('small')]
        equipo_nombre="no encontrado"
        if equipo in equipos_misma_liga_links:
            equipo_nombre=equipos_misma_liga_nombres[equipos_misma_liga_links.index(equipo)]
        #solo para hacer debug
        #for x in range(len(tds)):
        #    print (jugadores_table[x].find('strong').text)
        #    print (jugadores_table[x].find('a').get('href'))
        #nombres=[jugadores_table[x].find('strong').text for x in range(len(jugadores_table))]
        links=[jugadores_table[x].find('a').get('href') for x in range(len(jugadores_table))]
        #print(nombres)
        return links,equipo_nombre
        #creo un diccionario con los nombres y los links de los jugadores
        #res = {} 
        #for nombre in nombres: 
        #    for link in links: 
        #        res[nombre] = link 
        #        links.remove(link) 
        #        break  
        #print (res)
        #for link in range(len(links)):
        #    jugador.jugador=links[link]
    return [],[]
#equipo = 'https://fmdataba.com/20/c/2606/argentinos-juniors/'
#print(conseguir_jugadores(equipo))
