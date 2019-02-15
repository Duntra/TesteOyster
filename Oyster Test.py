import bs4
import re
import urllib3
import urllib
import requests
from tkinter import *
from bs4 import BeautifulSoup as soup
gui=Tk()
bot = StringVar()
#################### Aqui crio o básico da GUI#####################################
gui.title ("Análise de HTML - Cristiano Maciel")
guilabel = Label (gui,text="Análise de HTML - Cristiano Maciel")
guilabel2 = Label(gui,text="Insira aqui sua URL")
entrada = Entry(gui,textvariable=bot)

guilabel.grid(columnspan=4,sticky='N')
guilabel2.grid(row=1,column=1)
entrada.grid(row=1,column=2,columnspan=2,sticky='NSEW')

#################### Defino a função que vai ser ativada com o botão na GUI ##########################
def funcao():
    guilabel3 = Label(gui, text="URL analisada...")
    guilabel3.grid(row=3, column=1)
    url = bot.get() #Aqui capturo a URL a partir da entrada da GUI
    r = requests.get(url)
    req = urllib.request.Request(url)
    client = urllib.request.urlopen(req).read()
    page_soup = soup(client, "html.parser")
    #Aqui encontro o Título da Página
    titulo = page_soup.title.string

    #Aqui confirmo a versão HTML do arquivo
    if re.search('XHTML 1.0',r.text):
        vers = 'Versão XHTML 1.0'
    elif re.search('XHTML 1.1', r.text):
        vers = 'Versão XHTML 1.1'
    elif re.search('<!DOCTYPE html>',r.text):
        vers = 'Versão HTML 5.0'
    elif re.search('HTML 4.01', r.text):
        vers = 'Versão HTML 4.01'
    elif re.search('HTML 3.2', r.text):
        vers = 'Versão HTML 3.2'
    else:
        vers = 'Versão não encontrada'

    # Aqui aplico a GUI os resultados referentes ao título da página e versão do documento
    guilabel4 = Label(gui, text=vers)
    guilabel4.grid(row=5, column=1,columnspan=3,sticky='NSEW')
    guilabel5 = Label(gui, text="Titulo da Página:")
    guilabel5.grid(row=6, column=0, columnspan=2, sticky='E')
    guilabel6 = Label(gui, text=titulo)
    guilabel6.grid(row=6, column=2, columnspan=2, sticky='NSEW')

    # Aqui removo do link alguns caractéres para que eu fique apenas com o domínio do site
    if re.search("\.com(.*)",str(url)) is not None:
        urll = re.search("\.com(.*)", str(url)).group(0)
        print(urll)
    else:
        pass
    if re.search("\.org(.*)",str(url)) is not None:
        urll = re.search("\.org(.*)", str(url)).group(0)
        print(urll)
    else:
        pass
    if re.search("\.net(.*)",str(url)) is not None:
        urll = re.search("\.net(.*)", str(url)).group(0)
        print(urll)
    else:
        pass
    if re.search("\.edu(.*)",str(url)) is not None:
        urll = re.search("\.edu(.*)", str(url)).group(0)
        print(urll)
    else:
        pass

    urlclean = str(url).replace(urll,"")
    print(urlclean)
    # Aqui removo do link outros caracteres para que eu fique apenas com o domínio do site
    sitedomain = str(urlclean).replace("https://","")
    sitedomain2 = str(sitedomain).replace("http://","")
    sitedomain3 = str(sitedomain2).replace("www","")
    print(sitedomain3)



    # Aqui declaro variaveis quais serão úteis para encontrar a quantidade de links externos e internos
    links = []
    links2 = []
    links3 = []
    linkes = []
    linksextn = []



    # Aqui procuro links internos
    for link in page_soup.findAll('a', attrs={'href': re.compile(sitedomain3)}):
        links.append(link.get('href'))
    print(links)
    for link in page_soup.findAll('a', attrs={'href': re.compile('^#+|^/')}):
        links2.append(link.get('href'))
    print(links2)
    for link in links2:
        if link not in links:
            links3.append(link)
    linksin = links + links3
    print (links3)
    print(linksin)
    print("Links Internos:", len(linksin))

    # Aqui os resultados referentes aos links internos são expostos no GUI
    guilabel7 = Label(gui, text="Links Internos:")
    guilabel7.grid(row=7, column=0, columnspan=2, sticky='E')
    guilabel8 = Label(gui, text=len(linksin))
    guilabel8.grid(row=7, column=2, columnspan=2, sticky='W')

    # Aqui procuro links internos
    for link in page_soup.findAll('a', attrs={'href': re.compile('http')}):
        linkes.append(link.get('href'))

    for link in linkes:
        if link not in links:
            linksextn.append(link)
    print(linkes)
    print("Links Externos:", len(linksextn))
    # Aqui os resultados referentes aos links externos são expostos no GUI
    guilabel9 = Label(gui, text="Links Externos:")
    guilabel9.grid(row=8, column=0, columnspan=2, sticky='E')
    guilabel10 = Label(gui, text=len(linksextn))
    guilabel10.grid(row=8, column=2, columnspan=2, sticky='W')

# Aqui crio o botão da GUI
botao = Button(gui, text="GO!", command=funcao, bg="cyan")
botao.grid(row=2,column=3)
gui.mainloop()