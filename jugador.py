'''
No soy un experto en programacion, la mayoria de este codigo son snippets que encontre por ahi, van a haber horrores de programacion
si sabes como hacerlo mejor, sos enteramente bienvenido, deja documentado siempre por favor, yo hago lo que puedo, gracias a 
StackOverflow, Google, ehh creo que GeeksForGeeks o algo asi, al alcohol y el cafe que me mantuvo despierto a ciertas horas, 
algunas cosas las hice yo pensandolas o modificando ejemplos, espero que este codigo ayude a la comunidad de pes 6
Besitos
'''
import random
import time
from bs4 import BeautifulSoup
from datetime import datetime



def fm_to_pes6(stat):
    start=[40,43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97]
    stop =[43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97,100]
    #print(stat)
    stat=round(stat)
    #print(stat)
    PES6_stat=random.randrange(start[stat-1],stop[stat-1])
    #print(PES6_stat)
    return PES6_stat

def fm_to_pes6_1_a_8(stat):
    start=[1,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8]
    #print(stat)
    stat=round(stat)
    #print(stat)
    PES6_stat=start[stat-1]
    #print(PES6_stat)
    return PES6_stat

def fm_to_pes6_A_a_C(stat):
    start=['C','C','C','C','C','B','B','B','B','B','B','B','B','B','A','A','A','A','A','A']
    #print(stat)
    stat=round(stat)
    #print(stat)
    PES6_stat=start[stat-1]
    #print(PES6_stat)
    return PES6_stat

def convert_stats(stats,is_player,reg_pos,posiciones,primercol):
    #separo todas las habilidades de la tabla 'MENTAL' en variables para hacer los calculos
    fm_agresividad=stats['MENTAL']['Aggression']
    fm_anticipacion=stats['MENTAL']['Anticipation']
    fm_valentia=stats['MENTAL']['Bravery']
    fm_serenidad=stats['MENTAL']['Composure']
    fm_concentracion=stats['MENTAL']['Concentration']
    fm_decisiones=stats['MENTAL']['Decisions']
    fm_determinacion=stats['MENTAL']['Determination']
    fm_talento=stats['MENTAL']['Flair']
    fm_liderazgo=stats['MENTAL']['Leadership']
    fm_desmarques=stats['MENTAL']['Off The Ball']
    fm_colocacion=stats['MENTAL']['Positioning']
    fm_juego_en_equipo=stats['MENTAL']['Teamwork']
    fm_vision=stats['MENTAL']['Vision']
    fm_sacrificio=stats['MENTAL']['Work Rate']
    #separo todas las habilidades de la tabla 'PHYSICAL' en variables para hacer los calculos
    fm_aceleracion=stats['PHYSICAL']['Acceleration']
    fm_agilidad=stats['PHYSICAL']['Agility']
    fm_equilibrio=stats['PHYSICAL']['Balance']
    fm_alcance_de_salto=stats['PHYSICAL']['Jumping Reach']
    fm_recuperacion_fisica=stats['PHYSICAL']['Natural Fitness']
    fm_velocidad=stats['PHYSICAL']['Pace']
    fm_resistencia=stats['PHYSICAL']['Stamina']
    fm_fuerza=stats['PHYSICAL']['Strength']
    #defino en 0 todas las habilidades de la tabla 'GOALKEEPING' ya que si es jugador jamas voy a traerme los datos para el dict
    fm_alcance_aereo=fm_mando_en_el_area=fm_comunicacion=fm_eccentricity=fm_control=fm_blocaje=fm_saques_de_puerta=fm_uno_contra_uno=fm_pases=fm_golpeo_de_punios=fm_reflejos=fm_salidas=fm_saque_con_la_mano=0
    #defino en 0 todas las habilidades de la tabla 'TECHNICAL' ya que si es jugador jamas voy a traerme los datos para el dict
    fm_saques_de_esquina=fm_centros=fm_regate=fm_remate=fm_tiros_libres=fm_cabeceo=fm_tiros_lejanos=fm_saques_largos=fm_marcaje=fm_pases=fm_penaltis=fm_entradas=fm_tecnica=0
    #fm_control=0 #los jugadores y arqueros ya comparten esta variable no hace falta definirla dos veces pero lo pongo
    #defino todas las variables de stats para pes en 0 en caso de que falle
    PES6_Weak_Foot_Accuracy=PES6_Weak_Foot_Frequeency=PES6_Attack =PES6_Defense =PES6_Balance =PES6_Stamina =PES6_Speed =PES6_Acceleration =PES6_Response =PES6_Agility =PES6_Dribble_Accuracy =PES6_Dribble_Speed =PES6_Short_Pass_Accuracy =PES6_Short_Pass_Speed =PES6_Long_Pass_Accuracy =PES6_Long_Pass_Speed =PES6_Shot_Accuracy =PES6_Shot_Power =PES6_Shot_Technique =PES6_Free_Kick_Accuracy =PES6_Swerve =PES6_Heading =PES6_Jump =PES6_Technique =PES6_Agression =PES6_Mentality =PES6_GK_Skills =PES6_Team_Work =PES6_Consistency=PES6_Condition=0
    #defino en 0 todas las variables de las habilidades especiales 
    PES6_Dribbling =PES6_Tactical_Dribble =PES6_Positioning =PES6_Reaction =PES6_Playmaking =PES6_Passing =PES6_Scoring =PES6_1_1_Scoring =PES6_Post_Player =PES6_Lines =PES6_Middle_Shooting =PES6_Side =PES6_Centre =PES6_Penalties =PES6_1_Touch_Pass =PES6_Outside =PES6_Marking =PES6_Sliding =PES6_Covering =PES6_D_Line_Control =PES6_Penalty_Stopper =PES6_1_On_1_Stopper =PES6_Long_Throw =0
    if is_player:
        fm_saques_de_esquina=stats[primercol]['Corners']
        fm_centros=stats[primercol]['Crossing']
        fm_regate=stats[primercol]['Dribbling']
        fm_remate=stats[primercol]['Finishing']
        fm_control=stats[primercol]['First Touch']
        fm_tiros_libres=stats[primercol]['Free Kick']
        fm_cabeceo=stats[primercol]['Heading']
        fm_tiros_lejanos=stats[primercol]['Long Shots']
        fm_saques_largos=stats[primercol]['Long Throws']
        fm_marcaje=stats[primercol]['Marking']
        fm_pases=stats[primercol]['Passing']
        fm_penaltis=stats[primercol]['Penalty Taking']
        fm_entradas=stats[primercol]['Tackling']
        fm_tecnica=stats[primercol]['Technical']
        #convertir de fm a pes 6 para jugadores
        PES6_Weak_Foot_Accuracy =fm_to_pes6_1_a_8((((fm_remate+fm_control+fm_tecnica)/3)+fm_remate)/2)
        PES6_Weak_Foot_Frequeency=fm_to_pes6_1_a_8(fm_decisiones)
        PES6_Attack = fm_to_pes6((fm_desmarques*0.7)+(fm_anticipacion*0.3))
        if reg_pos==2 or reg_pos==3 or reg_pos==5:
            if PES6_Attack<70 and PES6_Attack>0:
                PES6_Attack=PES6_Attack-10
            elif PES6_Attack<86 and PES6_Attack>=70:
                PES6_Attack=PES6_Attack-15
            elif PES6_Attack<100 and PES6_Attack>=86:
                PES6_Attack=PES6_Attack-20
        PES6_Defense = fm_to_pes6((fm_anticipacion*0.1)+(fm_marcaje*0.3)+(fm_colocacion*0.5)+(fm_entradas*0.1))
        if reg_pos==8 or reg_pos==9 or reg_pos==10 or reg_pos==11 or reg_pos==12:
            if PES6_Defense<70 and PES6_Defense>0:
                PES6_Defense=PES6_Defense-10
            elif PES6_Defense<86 and PES6_Defense>=70:
                PES6_Defense=PES6_Defense-15
            elif PES6_Defense<100 and PES6_Defense>=86:
                PES6_Defense=PES6_Defense-20
        PES6_Balance = fm_to_pes6((fm_equilibrio+fm_fuerza)/2)
        PES6_Stamina = round((fm_to_pes6(15)+fm_to_pes6(fm_resistencia))/2)
        PES6_Speed = fm_to_pes6(fm_velocidad)
        PES6_Acceleration = fm_to_pes6(fm_aceleracion)
        PES6_Response = fm_to_pes6(fm_anticipacion)
        PES6_Agility = fm_to_pes6(fm_agilidad)
        PES6_Dribble_Accuracy = fm_to_pes6((fm_regate+fm_control)/2)
        PES6_Dribble_Speed = fm_to_pes6((fm_regate*0.5)+(fm_aceleracion*0.25)+(fm_velocidad*0.25))
        PES6_Short_Pass_Accuracy = fm_to_pes6(fm_pases)
        PES6_Short_Pass_Speed = fm_to_pes6((fm_pases+fm_tecnica)/2)
        PES6_Long_Pass_Accuracy = fm_to_pes6((fm_centros+fm_pases)/2)
        PES6_Long_Pass_Speed = fm_to_pes6((fm_centros+fm_pases+fm_tecnica)/3)
        PES6_Shot_Accuracy = fm_to_pes6((fm_remate+fm_serenidad)/2)
        PES6_Shot_Power = fm_to_pes6((fm_tiros_lejanos*0.7)+(fm_remate*0.3))
        PES6_Shot_Technique = fm_to_pes6((fm_remate+fm_control+fm_tecnica)/3)
        PES6_Free_Kick_Accuracy = fm_to_pes6(fm_tiros_libres)
        PES6_Swerve = fm_to_pes6((fm_tiros_libres+fm_saques_de_esquina)/2)
        PES6_Heading = fm_to_pes6(fm_cabeceo)
        PES6_Jump = fm_to_pes6(fm_alcance_de_salto)
        PES6_Technique = fm_to_pes6((fm_talento+fm_tecnica)/2)
        PES6_Agression = fm_to_pes6((fm_vision*0.5)+(fm_desmarques*0.5))
        PES6_Mentality = fm_to_pes6((fm_sacrificio*0.7)+(fm_valentia*0.3))
        PES6_GK_Skills = 50
        PES6_Team_Work = fm_to_pes6(fm_juego_en_equipo)
        PES6_Consistency = fm_to_pes6_1_a_8(fm_determinacion)
        PES6_Condition =fm_to_pes6_1_a_8(fm_recuperacion_fisica)
    else:
        fm_alcance_aereo=stats[primercol]['Aerial Reach']
        fm_mando_en_el_area=stats[primercol]['Command Of Area']
        fm_comunicacion=stats[primercol]['Communication']
        fm_eccentricity=stats[primercol]['Eccentricity']
        fm_control=stats[primercol]['First Touch']
        fm_blocaje=stats[primercol]['Handling']
        fm_saques_de_puerta=stats[primercol]['Kicking']
        fm_uno_contra_uno=stats[primercol]['One On Ones']
        fm_pases=stats[primercol]['Passing']
        fm_golpeo_de_punios=stats[primercol]['Punching (Tendency)']
        fm_reflejos=stats[primercol]['Reflexes']
        fm_salidas=stats[primercol]['Rushing Out']
        fm_saque_con_la_mano=stats[primercol]['Throwing']
        #convertir de fm a pes 6 para arqueros
        PES6_Weak_Foot_Accuracy =fm_to_pes6_1_a_8((2+fm_remate)/2)
        PES6_Weak_Foot_Frequeency=fm_to_pes6_1_a_8(fm_decisiones)
        PES6_Attack = 30
        PES6_Defense = fm_to_pes6((fm_colocacion+fm_mando_en_el_area)/2)
        PES6_Balance = fm_to_pes6((fm_equilibrio+fm_mando_en_el_area)/2)
        PES6_Stamina = round((fm_to_pes6(15)+fm_to_pes6(fm_resistencia))/2)
        PES6_Speed = fm_to_pes6(fm_velocidad)
        PES6_Acceleration = fm_to_pes6(fm_aceleracion)
        PES6_Response = fm_to_pes6(fm_reflejos*0.8+fm_anticipacion*0.2)
        PES6_Agility = fm_to_pes6((fm_agilidad+fm_alcance_aereo)/2)
        PES6_Dribble_Accuracy = fm_to_pes6((fm_talento+fm_control)/2)
        PES6_Dribble_Speed = fm_to_pes6((fm_talento+fm_control+fm_velocidad)/3)
        PES6_Short_Pass_Accuracy = fm_to_pes6(fm_pases)
        PES6_Short_Pass_Speed = fm_to_pes6((fm_pases*0.8+fm_control*0.2))
        PES6_Long_Pass_Accuracy = fm_to_pes6(fm_saques_de_puerta)
        PES6_Long_Pass_Speed = fm_to_pes6(fm_saques_de_puerta*0.8+fm_control*0.2)
        PES6_Shot_Accuracy = 45
        PES6_Shot_Power = fm_to_pes6(fm_saques_de_puerta)
        PES6_Shot_Technique = 45
        PES6_Free_Kick_Accuracy = fm_to_pes6(fm_saques_de_puerta*0.4+fm_talento*0.6)
        PES6_Swerve = 45
        PES6_Heading = 55
        PES6_Jump = fm_to_pes6((fm_alcance_de_salto+fm_alcance_aereo)/2)
        PES6_Technique = fm_to_pes6(fm_talento)
        PES6_Agression = fm_to_pes6((fm_colocacion*0.7+fm_anticipacion*0.3))
        PES6_Mentality = fm_to_pes6((fm_salidas*0.25+fm_uno_contra_uno*0.5+fm_serenidad*0.25))
        PES6_GK_Skills = fm_to_pes6(fm_blocaje*0.4+fm_alcance_aereo*0.4+fm_mando_en_el_area*0.2)
        PES6_Team_Work = fm_to_pes6(fm_comunicacion)
        PES6_Consistency = fm_to_pes6_1_a_8(fm_determinacion)
        PES6_Condition =fm_to_pes6_1_a_8(fm_recuperacion_fisica)
    if fm_regate>15:
        PES6_Dribbling = 1
    if fm_equilibrio>15:
        PES6_Tactical_Dribble = 1
    if round((fm_vision+fm_desmarques)/2)>15:
        PES6_Positioning = 1
    if fm_desmarques>15:
        PES6_Reaction = 1
    if fm_liderazgo>15:
        PES6_Playmaking = 1
    if fm_concentracion>15:
        PES6_Passing = 1
    if fm_anticipacion>15:
        PES6_Scoring = 1
    if round((fm_serenidad+fm_remate)/2)>15:
        PES6_1_1_Scoring = 1
    if round((fm_fuerza+fm_juego_en_equipo)/2)>15:
        PES6_Post_Player = 1
    if fm_decisiones>15:
        PES6_Lines = 1
    if fm_tiros_lejanos>15:
        PES6_Middle_Shooting = 1
    if (posiciones[3]+posiciones[5]+posiciones[7]+posiciones[9])>2:
        PES6_Side = 1
    if (posiciones[1]+posiciones[2]+posiciones[4]+posiciones[6]+posiciones[8]+posiciones[10]+posiciones[11])>2:
        PES6_Centre = 1
    if fm_penaltis>15:
        PES6_Penalties = 1
    if round((fm_tecnica+fm_pases)/2)>15:
        PES6_1_Touch_Pass = 1
    if fm_tecnica>15:
        PES6_Outside = 1
    if fm_marcaje>15:
        PES6_Marking = 1
    if fm_entradas>15:
        PES6_Sliding = 1
    if fm_colocacion>15:
        PES6_Covering = 1
    if round((fm_colocacion+fm_liderazgo)/2)>15:
        PES6_D_Line_Control = 1
    if round((fm_serenidad+fm_uno_contra_uno)/2)>15:
        PES6_Penalty_Stopper = 1
    if fm_uno_contra_uno>15:
        PES6_1_On_1_Stopper = 1
    if fm_saques_largos>15:
        PES6_Long_Throw = 1
    PES6_Injury_Tolerance= fm_to_pes6_A_a_C((fm_resistencia+fm_recuperacion_fisica)/2)
    PES6_stats=[PES6_Weak_Foot_Accuracy,PES6_Weak_Foot_Frequeency,PES6_Attack ,PES6_Defense ,PES6_Balance ,PES6_Stamina ,PES6_Speed ,
    PES6_Acceleration ,PES6_Response ,PES6_Agility ,PES6_Dribble_Accuracy ,PES6_Dribble_Speed ,PES6_Short_Pass_Accuracy ,PES6_Short_Pass_Speed ,
    PES6_Long_Pass_Accuracy ,PES6_Long_Pass_Speed ,PES6_Shot_Accuracy ,PES6_Shot_Power ,PES6_Shot_Technique ,PES6_Free_Kick_Accuracy ,
    PES6_Swerve ,PES6_Heading ,PES6_Jump ,PES6_Technique ,PES6_Agression ,PES6_Mentality ,PES6_GK_Skills ,PES6_Team_Work ,PES6_Consistency,
    PES6_Condition,PES6_Dribbling ,PES6_Tactical_Dribble ,PES6_Positioning ,PES6_Reaction ,PES6_Playmaking ,PES6_Passing ,PES6_Scoring ,
    PES6_1_1_Scoring ,PES6_Post_Player ,PES6_Lines ,PES6_Middle_Shooting ,PES6_Side ,PES6_Centre ,PES6_Penalties ,PES6_1_Touch_Pass ,
    PES6_Outside ,PES6_Marking ,PES6_Sliding ,PES6_Covering ,PES6_D_Line_Control ,PES6_Penalty_Stopper ,PES6_1_On_1_Stopper ,PES6_Long_Throw ,
    PES6_Injury_Tolerance]
    return PES6_stats


def get_abilities(soup, keyword):
    table = soup.select_one('div:has(h3:contains("' + keyword + '")) + div > table')
    d = {item.select_one('td:nth-child(odd)').text: int(item.select_one('td:nth-child(even)').text) for item in table.select('tr')}
    return d

def get_fav_side(posiciones):
    fav_side='B'
    both_sides=0
    left_side=0
    right_side=0
    for l in range(len(posiciones)):
        if posiciones[l][-1]=='C' or posiciones[l][-1]=='K' or posiciones[l][-1]=='M':
            both_sides=both_sides+1
        elif posiciones[l][-1]=='L':
            left_side=left_side+1
        elif posiciones[l][-1]=='R':
            right_side=right_side+1
    if both_sides>left_side and both_sides>right_side:
        fav_side='B'
    elif left_side>both_sides and left_side>right_side:
        fav_side='L'
    elif right_side>both_sides and right_side>left_side:
        fav_side='R'
    return fav_side
    
def get_pos_reg(pos):
    return {
        'GK': 0,
        'DC': 3,
        'DL': 4,
        'DR': 4,
        'DM': 5,
        'WBL': 6,
        'WBR': 6,
        'MC': 7,
        'ML': 8,
        'MR': 8,
        'AMC': 9,
        'AML': 10,
        'AMR': 10,
        'STC': 12   
    }.get(pos, 0)    # si no encontramos la posicion devolvemos 0 que es GK


def get_pos(posicion,posiciones):
    equivalencias= {
        0: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11   
    }
    indice=equivalencias.get(posicion)
    posiciones[indice]=1
    return posiciones



def club_actual(club,real_club):
    resp=club
    if club!=real_club:
        resp=real_club
    return resp

def nombre(name):
    x=""
    x=name.split()
    if len(x)==1:
       name=x[0]
    else:
        primer_nombre = x[0]
        apellido = x[-1]
        name=primer_nombre[0] + ". " + apellido
        if len(name)>16:
            name=apellido
            if len(name)>16:
              name=apellido[:15]
    
    return name

def nombre_remera(name):
    x=name.split()
    name=x[-1].upper()
    a,b = 'ÁÀÉÈÍÌÓÒÚÙÜÑ','AAEEIIOOUUUN'
    trans = str.maketrans(a,b)
    name=name.translate(trans)
    if len(name)>8:
        if len(name)>16:
            name[:15]
        name=name
    elif len(name)<5:
        name="  ".join(name)
    elif len(name)<9:
        name=" ".join(name)
    return name

'''
esta logica la pueden cambiar segun a ustedes les parezca, pes6 tiene solo 2 opciones para la pierna buena
'''


def pierna_buena(foot):
    if foot=="Left" or foot=="Left Only":
        foot="L"
    elif foot=="Right" or foot=="Right Only":
        foot="R"
    elif foot=="Both":
        foot="R"
    elif foot=="Either":
        foot="L"
    return foot


'''
aca lo que hacemos es calcular la edad que tiene nuestro jugador, segun su fecha de nacimiento contra el dia de hoy
'''

def edad_actual(born_date):
   born_date = datetime.strptime(born_date, '%d/%m/%Y').date()
   edad_hoy= datetime.now().year - born_date.year
   return edad_hoy

'''
si encuentro la nacionalidad simplemente devuelvo la misma variable que me dieron, si no la encontro
entonces devuelvo free nationalitiy, que seria el ultimo valor en nuestra lista de nacionalidades
'''


def get_pes_6_nationality(nation,nationalities):
    if nation in nationalities:
        resp=nation
    else:
        resp=nationalities[-1]
    return resp

def conseguir_info_jugador(jugador,s):
    '''
    aca hacemos todo el parseo de texto, primero recibimos s que es la variable que contiene nuestra sesion inicia en la pagina
    con nuestro user y password asi no nos dropea el sitio por ser un bot, luego le pasamos jugador que es la url del jugador
    con habilidades a parsear y todo eso, todo lo demas que vas a ver abajo es simple y comun parseo de texto
    '''
    name, dorsal, meta_height, meta_weight,foot, age, nation,club, real_club, stats,primercol,is_player,posicion_reg,posiciones,status_code="",0,0,0,"","","","","",{},"",True,"",[],404
    #jugador='https://fmdataba.com/20/p/155151/marc-andre-ter-stegen/'
    #page = s.get('https://fmdataba.com/20/p/147073/lionel-messi/', headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    #page = s.get('https://fmdataba.com/20/p/150823/arda-turan/', headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    page = s.get(jugador, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    #print(page.status_code)
    if page.status_code==200:
        status_code=page.status_code
        soup = BeautifulSoup(page.text, 'html.parser')
        #esta variable la imprimo a veces, te muestra el nombre de usuario, es simplemente para chequeo de que seguis logueado hasta este punto
        #print(soup.find_all('a',{'class':'dropdown-toggle'})[3].find('b').text) 
        meta_height=int(soup.find('meta',attrs={'itemprop':'height'}).get('content').split()[0])
        meta_weight=int(soup.find('meta',attrs={'itemprop':'weight'}).get('content').split()[0])
        tables_hidden_overflow=soup.find_all('table',attrs={'class':'table', 'style':'margin-bottom: 0px; overflow:hidden;'})
        born_date= tables_hidden_overflow[1].find_all('td',attrs={'class':"", 'colspan':"3"})[-1]
        unwanted=born_date.find('strong')
        unwanted.extract()
        age=born_date.text.strip("(" " " ")")
        nation=tables_hidden_overflow[1].find_all('img',attrs={'style':'margin-right:10px; margin-top:-4px;'})[0].get('alt')
        dorsal=soup.find_all('div',attrs={'class':'forma61'})
        if dorsal is not None and len(dorsal) > 0:
            dorsal = dorsal[0].text
        else:
            dorsal = "0"
        dorsal=int(dorsal)
        foot=tables_hidden_overflow[3].find_all('td',attrs={'class':'text-center'})[-2].text
        name=soup.find_all('span',attrs={'itemprop':'name', 'class':'hide'})[0].text
        posiciones=soup.find_all('div',attrs={'class':'posse','style':'zoom:115%;'})[0].find_all('div')
        posiciones=[posiciones[posicion].get('class')[1] for posicion in range(len(posiciones))]
        #La primer posicion que aparece en fmdataba va a ser la posicion registrada
        posicion_reg=posiciones[0]
        #los jugadores cedidos no aparecen en el club al cual fueron cedidos
        club=soup.find_all('strong',attrs={'itemprop':'affiliation'})[0].text
        #real_club=soup.find_all('table',attrs={'style':'margin-bottom: 0px;'})
        #if real_club is not None and len(real_club)>6:
        #    real_club=real_club[4].find_all('tr')[1].find_all('td')[2].text
        #else:
        real_club=club
        stats = {}
        columnas=[]
        primercol = soup.find_all('h3',attrs={'style':'font-size: 13px;'})[1].text
        is_player=True
        if primercol == 'TECHNICAL':
            columnas=['TECHNICAL','MENTAL','PHYSICAL']
            is_player=True
        elif primercol=='GOALKEEPING':
            columnas=['GOALKEEPING','MENTAL','PHYSICAL']
            is_player=False
        for ability in columnas:
            stats[ability] = get_abilities(soup, ability)
    else:
        status_code=page.status_code
    return name, dorsal, meta_height, meta_weight,foot, age,nation, club, real_club, stats,primercol,is_player,posicion_reg,posiciones,status_code


def player_scrapper(link,session):
    nationalities = ["Austria","Belgium","Bulgaria","Croatia","Czech Republic","Denmark","England","Finland","France","Germany","Greece",
    "Hungary","Ireland","Italy","Latvia","Netherlands","Northern Ireland""Norway","Poland","Portugal","Romania","Russia","Scotland","Serbia and Montenegro",
    "Slovakia","Slovenia","Spain","Sweden","Switzerland","Turkey","Ukraine","Wales","Angola","Cameroon","Cote d'Ivoire","Ghana","Nigeria",
    "South Africa","Togo","Tunisia","Costa Rica","Mexico","Trinidad and Tobago","United States","Argentina","Brazil","Chile","Colombia",
    "Ecuador","Paraguay","Peru","Uruguay","Iran","Japan","Saudi Arabia","South Korea","Australia","Bosnia and Herzegovina","Estonia",
    "Israel","Honduras","Jamaica","Panama","Bolivia","Venezuela","China","Uzbekistan","Albania","Cyprus","Iceland","Macedonia","Armenia",
    "Belarus","Georgia","Liechtenstein","Lithuania","Algeria","Benin","Burkina Faso","Cape Verde","Congo","DR Congo","Egypt","Equatorial Guinea",
    "Gabon","Gambia","Guinea","Guinea-Bissau","Kenya","Liberia","Libya","Mali","Morocco","Mozambique","Senegal","Sierra Leone","Zambia","Zimbabwe",
    "Canada","Grenada","Guadeloupe","Martinique","Netherlands Antilles","Oman","New Zealand","Free Nationality"]
    time.sleep(20)
    name, dorsal, meta_height, meta_weight,foot, age,nation, club, real_club, stats,primercol,is_player,posicion_reg,posiciones,status_code=conseguir_info_jugador(link,session)
    if status_code==200:
        csv_NAME=nombre(name)
        csv_SHIRT_NAME=nombre_remera(name)
        csv_REGISTERED_POSITION=get_pos_reg(posicion_reg)
        csv_POSICIONES=[0,0,0,0,0,0,0,0,0,0,0,0]
        #ponemos 1 a la posicion registrada
        csv_POSICIONES=get_pos(get_pos_reg(posicion_reg),csv_POSICIONES)
        #ahora le pasamos todas las demas posiciones para que se pongan como secundarias
        for i in range(len(posiciones)):
            csv_POSICIONES=get_pos(get_pos_reg(posiciones[i]),csv_POSICIONES)
        if csv_POSICIONES[11]==1 and csv_POSICIONES[9]==1:
            #con esto seteamos el segundo delantero, si es CF y AMF es SS tambien
            csv_POSICIONES[10]=1
        csv_HEIGHT = meta_height
        csv_WEIGHT = meta_weight
        csv_STRONG_FOOT=pierna_buena(foot)
        csv_FAVOURED_SIDE=get_fav_side(posiciones)
        PES6_stats=convert_stats(stats,is_player,csv_REGISTERED_POSITION,csv_POSICIONES,primercol)
        csv_AGE=edad_actual(age)
        csv_CLUB_NUMBER=dorsal
        csv_NATIONALITY=get_pes_6_nationality(nation,nationalities)
        csv_CLUB_TEAM=club_actual(club,real_club)
        return tuple([""]+[csv_NAME]+[csv_SHIRT_NAME]+csv_POSICIONES+[csv_REGISTERED_POSITION]+[int(csv_HEIGHT)]+[csv_STRONG_FOOT]+
            [csv_FAVOURED_SIDE]+PES6_stats+[1,1,1,1]+[csv_AGE]+[int(csv_WEIGHT)]+[csv_NATIONALITY]+[1,0,1,0,0,0,0,0,0,0,0,0,0,0,'N','None',0,0]+
            [csv_CLUB_TEAM]+[csv_CLUB_NUMBER])
    #print('el sitio esta dando un status code: '+str(status_code))
    else:
        return status_code
'''
Esta lista nacionalidades fue saca de https://github.com/lazanet/PES-Editor-6/blob/rebased/PES_Editor/src/editor/Stats.java
si la nacionalidad coincide con la que nos brinda fmdataba.com entonces usamos esa, si no usamos el ultimo valor de la lista que es
"Free Nationality" esta lista de nacionalidades fue saca del pes 6 original, puede no coincidir tal vez con tu exe
Gracias a PeterC10 que se tomo el trabajo de hacerlo.
Pd. si alguna nacionalidad saca de fmdataba.com esta listada aca pero tiene un nombre raro habria que hacer un dictionary
para emular la funcionalidad de switch que no existe en python mas info aca https://www.geeksforgeeks.org/switch-case-in-python-replacement/
o en Google :)
'''
'''
startTime = datetime.now()


nationalities = ["Austria","Belgium","Bulgaria","Croatia","Czech Republic","Denmark","England","Finland","France","Germany","Greece",
"Hungary","Ireland","Italy","Latvia","Netherlands","Northern Ireland""Norway","Poland","Portugal","Romania","Russia","Scotland","Serbia and Montenegro",
"Slovakia","Slovenia","Spain","Sweden","Switzerland","Turkey","Ukraine","Wales","Angola","Cameroon","Cote d'Ivoire","Ghana","Nigeria",
"South Africa","Togo","Tunisia","Costa Rica","Mexico","Trinidad and Tobago","United States","Argentina","Brazil","Chile","Colombia",
"Ecuador","Paraguay","Peru","Uruguay","Iran","Japan","Saudi Arabia","South Korea","Australia","Bosnia and Herzegovina","Estonia",
"Israel","Honduras","Jamaica","Panama","Bolivia","Venezuela","China","Uzbekistan","Albania","Cyprus","Iceland","Macedonia","Armenia",
"Belarus","Georgia","Liechtenstein","Lithuania","Algeria","Benin","Burkina Faso","Cape Verde","Congo","DR Congo","Egypt","Equatorial Guinea",
"Gabon","Gambia","Guinea","Guinea-Bissau","Kenya","Liberia","Libya","Mali","Morocco","Mozambique","Senegal","Sierra Leone","Zambia","Zimbabwe",
"Canada","Grenada","Guadeloupe","Martinique","Netherlands Antilles","Oman","New Zealand","Free Nationality"]
equipo=input("ingrese un link: ")
#equipo='https://fmdataba.com/20/c/2191/fc-barcelona/'
#equipo='https://fmdataba.com/20/c/4174/at-lugano/'

if 'https://fmdataba.com/20/c/' in equipo:
    print('el link va bien es de club')
    username=""
    password=""
    try:
        f=open("accountfile.txt","r")
        lines=f.readlines()
        if len(lines)>1:
            username=lines[0]
            password=lines[1]
        f.close()
        if username=="" and password=="":
            username=input("ingrese su usuario: ")
            password=getpass("ingrese su contraseña: ")
            savecredencial=input("desea guardar sus credenciales? (si/no): ")
            if savecredencial=='si':
                file = open("accountfile.txt","w")
                file.write(username)
                file.write("\n")
                file.write(password)
                file.close()
    except FileNotFoundError:
        username=input("ingrese su usuario: ")
        password=getpass("ingrese su contraseña: ")
        savecredencial=input("desea guardar sus credenciales? (si/no): ")
        if savecredencial=='si':
            file = open("accountfile.txt","w")
            file.write(username)
            file.write("\n")
            file.write(password)
            file.close()

    #username='marcos_flores'
    #password='saq12345'
    payload = {'username': username, 'password': password,'ne':'2'}
    login_page = 'https://fmdataba.com/sign.php?'
    s = requests.Session()
    p=s.post(login_page, data=payload,headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
'''
'''    
    esta variable es para saber si se logueo, si estas logueado vas a ver que el valor imprimido es igual a username
    si no vas a ver que dice Login
'''   
'''
    login= BeautifulSoup(p.text,'html.parser').find_all('a',{'class':'dropdown-toggle'})[3].text.split()[0]
    #print(login)
    if login=="Login":
        print("error al loguearse")
        print(login)
    else:
        print("usted se ha logueado correctamente")
        print(login)
        links,nombre_del_csv = conseguir_jugadores.conseguir_jugadores(equipo)
        status_code=conseguir_info_jugador(links[0],s)[14]
        print(datetime.now() - startTime)
        #aca chequeamos con el primer link el mensaje que nos da el sitio si nos 200 entonces pasamos a hacer todo
        if status_code==200:
            #creamos el csv
            with open(nombre_del_csv + '.csv', 'w',newline='') as f:
                csv_escribir = csv.writer(f)
                csv_escribir.writerow(["ID","NAME","SHIRT_NAME","GK  0","CWP  2","CBT  3","SB  4","DMF  5","WB  6","CMF  7","SMF  8","AMF  9",
                "WF 10","SS  11","CF  12","REGISTERED POSITION","HEIGHT","STRONG FOOT","FAVOURED SIDE","WEAK FOOT ACCURACY","WEAK FOOT FREQUENCY",
                "ATTACK","DEFENSE","BALANCE","STAMINA","TOP SPEED","ACCELERATION","RESPONSE","AGILITY","DRIBBLE ACCURACY","DRIBBLE SPEED",
                "SHORT PASS ACCURACY","SHORT PASS SPEED","LONG PASS ACCURACY","LONG PASS SPEED","SHOT ACCURACY","SHOT POWER","SHOT TECHNIQUE",
                "FREE KICK ACCURACY","SWERVE","HEADING","JUMP","TECHNIQUE","AGGRESSION","MENTALITY","GOAL KEEPING","TEAM WORK","CONSISTENCY",
                "CONDITION / FITNESS","DRIBBLING","TACTIAL DRIBBLE","POSITIONING","REACTION","PLAYMAKING","PASSING","SCORING","1-1 SCORING",
                "POST PLAYER","LINES","MIDDLE SHOOTING","SIDE","CENTRE","PENALTIES","1-TOUCH PASS","OUTSIDE","MARKING","SLIDING","COVERING",
                "D-LINE CONTROL","PENALTY STOPPER","1-ON-1 STOPPER","LONG THROW","INJURY TOLERANCE","DRIBBLE STYLE","FREE KICK STYLE","PK STYLE",
                "DROP KICK STYLE","AGE","WEIGHT","NATIONALITY","SKIN COLOR","FACE TYPE","PRESET FACE NUMBER","HEAD WIDTH","NECK LENGTH","NECK WIDTH",
                "SHOULDER HEIGHT","SHOULDER WIDTH","CHEST MEASUREMENT","WAIST CIRCUMFERENCE","ARM CIRCUMFERENCE","LEG CIRCUMFERENCE",
                "CALF CIRCUMFERENCE","LEG LENGTH","WRISTBAND","WRISTBAND COLOR","INTERNATIONAL NUMBER","CLASSIC NUMBER","CLUB TEAM","CLUB NUMBER"])
            #iteramos por todos los links conseguidos de los jugadores y los guardamos en el csv ya convertidos
            for link in range(len(links)):
                #print(conseguir_info_jugador(links[link],s))
                #agregamos esto para que tengamos 15 segundos entre cada descarga de la pagina, asi no nos bloquea por ser un bot
                time.sleep(30)
                name, dorsal, meta_height, meta_weight,foot, age,nation, club, real_club, stats,primercol,is_player,posicion_reg,posiciones,status_code=conseguir_info_jugador(links[link],s)
                if status_code==200:
                    csv_NAME=nombre(name)
                    csv_SHIRT_NAME=nombre_remera(name)
                    csv_REGISTERED_POSITION=get_pos_reg(posicion_reg)
                    csv_POSICIONES=[0,0,0,0,0,0,0,0,0,0,0,0]
                    #ponemos 1 a la posicion registrada
                    csv_POSICIONES=get_pos(get_pos_reg(posicion_reg),csv_POSICIONES)
                    #ahora le pasamos todas las demas posiciones para que se pongan como secundarias
                    for i in range(len(posiciones)):
                        csv_POSICIONES=get_pos(get_pos_reg(posiciones[i]),csv_POSICIONES)
                    if csv_POSICIONES[11]==1 and csv_POSICIONES[9]==1:
                        #con esto seteamos el segundo delantero, si es CF y AMF es SS tambien
                        csv_POSICIONES[10]=1
                    csv_HEIGHT = meta_height
                    csv_WEIGHT = meta_weight
                    csv_STRONG_FOOT=pierna_buena(foot)
                    csv_FAVOURED_SIDE=get_fav_side(posiciones)
                    PES6_stats=convert_stats(stats,is_player,csv_REGISTERED_POSITION,csv_POSICIONES)
                    csv_AGE=edad_actual(age)
                    csv_CLUB_NUMBER=dorsal
                    csv_NATIONALITY=get_pes_6_nationality(nation,nationalities)
                    csv_CLUB_TEAM=club_actual(club,real_club)
                    #print(csv_NAME)
                    #print(posiciones)
                    #print(links[link])
                    #print (PES6_stats)
                    with open(nombre_del_csv + '.csv', 'a',newline='') as f:
                        csv_escribir = csv.writer(f)
                        csv_escribir.writerow([""]+[csv_NAME]+[csv_SHIRT_NAME]+csv_POSICIONES+[csv_REGISTERED_POSITION]+[csv_HEIGHT]+[csv_STRONG_FOOT]+
                        [csv_FAVOURED_SIDE]+PES6_stats+[1,1,1,1]+[csv_AGE]+[csv_WEIGHT]+[csv_NATIONALITY]+[1,0,1,0,0,0,0,0,0,0,0,0,0,0,'N','None',0,0]+
                        [csv_CLUB_TEAM]+[csv_CLUB_NUMBER])
                    #test=[0,1,2,3]
                    #print(test)
                    #test[0]=7
                    #print(test)
                else:
                    #si entramos aca es porque la pagina nos bloqueo mientras sacabamos info
                    print('el sitio esta dando un status code: '+str(status_code))
                    break
        else:
            print('el sitio esta dando un status code: '+str(status_code))
else:
    print('link incorrecto, por favor brinde uno valido de club')
'''