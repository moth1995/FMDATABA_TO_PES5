import requests
from bs4 import BeautifulSoup
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import webbrowser

import conseguir_jugadores
import jugador
import savefile
import conseguir_naciones
import conseguir_ligas
import conseguir_equipos

def convert(team,session,namelist,linklist,gamever):
    if team!="":
        if gamever!=0:
            team=linklist[namelist.index(team)]
            time.sleep(5)
            links,filename = conseguir_jugadores.conseguir_jugadores(team,session)
            #print(links,filename)
            #print("  ")
            players=[]
            for link in range(len(links)):
                player=jugador.player_scrapper(links[link],session)
                if type(player)==int:
                    messagebox.showerror(title=appname, message="Status code "+str(player))
                    break
                players.append(player)
            #print("fin")
            #print(players)
            if players!=[]:
                if gamever==1:
                    #this is for pes5 mdb
                    savefile.csv_to_mdb(filename,savefile.csv_parser(players))
                    messagebox.showinfo(title=appname, message="Your mdb file for "+str(filename) + "\nhas been generated")
                elif gamever==2:
                    #this is for pes6 csv
                    savefile.write_csv(filename,players)
                    messagebox.showinfo(title=appname, message="Your csv file for "+str(filename) + "\nhas been generated")
                else:
                    messagebox.showerror(title=appname, message="The game version doesnt have support yet")
            else:
                messagebox.showerror(title=appname, message="Couldn't retrieve data for players on " + str(filename))
        else:
            messagebox.showerror(title=appname, message="Please select a PES Version")
    else:
        messagebox.showerror(title=appname, message="Please select a club")

def login(username,password,resp):
    global logedaslbl
    payload = {'username': username, 'password': password,'ne':'2','g-recaptcha-response':resp}
    #print (payload)
    login_page = 'https://fmdataba.com/sign.php?ne=2'
    s = requests.Session()
    s.post(login_page, data=payload,headers=headnav)
    r=s.get(website,headers=headnav)
    login= BeautifulSoup(r.text,'html.parser').find_all('a',{'class':'dropdown-toggle'})[3].text.split()[0]
    #print(login)
    if login=="Login":
        #print("error al loguearse")
        return False
    else:
        #print("usted se ha logueado correctamente como "+login)
        logedaslbl.config(text="Login as "+ login)
        return s

def load_clubs(*args):
    global clubnames,clublinks
    league_selected=lgcmb.get()
    time.sleep(5)
    clubnames,clublinks=conseguir_equipos.conseguir_equipos(login_session,leag_val[leag_names.index(league_selected)])
    clubcmb.config(values=clubnames)
    clubcmb.set("")

def load_leagues(*args):
    global leag_names,leag_val,clubnames,clublinks
    clubnames,clublinks=[],[]
    nt_selected=ntcmb.get()
    time.sleep(5)
    leag_names,leag_val=conseguir_ligas.conseguir_ligas(login_session,ntlinks[nt_names.index(nt_selected)])
    lgcmb.config(values=leag_names)
    clubcmb.config(values=clubnames)
    lgcmb.set("")
    clubcmb.set("")

def load_cmb(session):
    global nt_names,ntlinks
    nt_names,ntlinks=conseguir_naciones.conseguir_paises(session)
    if nt_names!=[]:
        ntcmb.config(values=nt_names)

def login_action(*args):
    global login_session
    login_session=login(username_entry.get(),password_entry.get(),captcha_entry.get())
    if login_session:
        root.deiconify()
        loginsc.destroy()
        load_cmb(login_session)
    else:
        messagebox.showerror(title=appname, message="Login error please check again your credencials")

def close():
    loginsc.destroy()
    root.destroy()
    sys.exit()

website='https://fmdataba.com'
headnav={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
login_session=False
logedusername=""
appname='FMDATABA to PES Converter'
nt_names,ntlinks,leag_names,leag_val,clubnames,clublinks=[],[],[],[],[],[]

root = Tk()
root.title(appname)
w = 1200 # width for the Tk root
h = 700 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


loginsc = Toplevel()
loginsc.title(appname)
tw=400
th=350
tx = (ws/2) - (tw/2)
ty = (hs/2) - (th/2)
loginsc.geometry('%dx%d+%d+%d' % (tw, th, tx, ty))
loginsc.resizable(False, False)


username_lbl = Label(loginsc, text = 'Username:')
username_entry = Entry(loginsc,width=30)
password_lbl = Label(loginsc, text = 'Password:')
password_entry = Entry(loginsc,width=30, show = "*")
captcha_lbl = Label(loginsc, text = 'Captcha Token')
captcha_entry = Entry(loginsc,width=30)
goto_button=Button(loginsc,text='Go to FMDATABA login page', command=lambda:webbrowser.open('https://fmdataba.com/sign.php?ne=2',new=1))
login_button=Button(loginsc,text='Login', command=lambda:login_action())
exit_button = Button(loginsc,text='Cancel', command=lambda:close())
logedaslbl=Label(root)
loginsc.wm_protocol("WM_DELETE_WINDOW", lambda: close())
root.wm_protocol("WM_DELETE_WINDOW", lambda: close())
username_entry.bind('<Return>', login_action)
password_entry.bind('<Return>', login_action)
captcha_entry.bind('<Return>', login_action)


username_lbl.pack()
username_entry.pack()
password_lbl.pack()
password_entry.pack()
captcha_lbl.pack()
captcha_entry.pack()
goto_button.pack()
login_button.pack()
exit_button.pack()

ntcmb = ttk.Combobox(root,state="readonly", value=nt_names,width=20)
lgcmb = ttk.Combobox(root,state="readonly", value=leag_names,width=20)
clubcmb = ttk.Combobox(root,state="readonly", value=clubnames,width=20)
ntcmb.bind("<<ComboboxSelected>>", load_leagues)
lgcmb.bind("<<ComboboxSelected>>", load_clubs)
verlbl=Label(root,text='Select your PES Version')
option=IntVar()
option.set('0')
rbtn1=Radiobutton(root, text='PES5', variable=option, value=1)
rbtn2=Radiobutton(root, text='PES6', variable=option, value=2)
club_convert_btn=Button(root,text='Convert Club Team', command=lambda:convert(clubcmb.get(),login_session,clubnames,clublinks,option.get()))
#con el codigo de abajo creamos un spinbox y le seteamos el valor default a mostrar en 2
#sb = Spinbox(root, from_=1, to=12)
#sb.delete(0,"end")
#sb.insert(0,2)

logedaslbl.place(x=0,y=0)
ntcmb.place(x=400,y=160)
lgcmb.place(x=400,y=200)
clubcmb.place(x=400,y=240)
verlbl.place(x=400,y=280)
rbtn1.place(x=410,y=320)
rbtn2.place(x=470,y=320)
club_convert_btn.place(x=410,y=360)
root.resizable(False, False)
root.withdraw()
root.mainloop() 