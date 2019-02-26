from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def soup_request(url):
    req = Request(url, headers={'User-Agent' : "counter-lol"})
    respuesta = urlopen(req)
    contenido_web = respuesta.read()
    soup = BeautifulSoup(contenido_web, "html.parser")
    return soup
