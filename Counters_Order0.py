import os
from urllib.request import urlopen, Request

champions_list=['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia',
                 'Annie', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank',
                 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia',
                 "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven',
                 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora',
                 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas',
                 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia',
                 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx',
                 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle',
                 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw",
                 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu',
                 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi',
                 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus',
                 'Nautilus', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna',
                 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Rakan', 'Rammus',
                 "Rek'Sai", 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze',
                 'Sejuani', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion',
                 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Syndra',
                 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh',
                 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch',
                 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vi',
                 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah',
                 'Xerath', 'Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs',
                 'Zilean', 'Zoe', 'Zyra']

def main(champion):
    """
    Funcion principal.
    """
    champion_aux = champion.lower().strip().replace(" ", "-")
    print(champion_aux)
    url= "http://www.lolcounter.com/champions/"+champion_aux
    req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
    respuesta = urlopen(req)
    contenido_web = respuesta.read()
    a=open("contenido_"+champion,"w")
    a.write(str(contenido_web[175000:220000]))
    a.close()
    return "Completado."

print(main(champions_list[0]))
