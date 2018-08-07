import os
from urllib.request import urlopen, Request

def get_champion(champion):
    """
    fucntion to get the information page about champion
    """
    champion_aux = champion.lower().strip().replace(" ", "-")
    print(champion_aux)
    url= "http://www.lolcounter.com/champions/"+champion_aux
    req = Request(url, headers={'User-Agent' : "counter-lol"}) 
    respuesta = urlopen(req)
    contenido_web = respuesta.read()
    a=open("content_"+champion,"w")
    a.write(str(contenido_web[175000:220000]))
    a.close()
    return "listo"
