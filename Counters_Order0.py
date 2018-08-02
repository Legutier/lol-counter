import os
import urllib2
import ast
campeones_lista=['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia',
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

def conv_str_dic(string):
    dic = ast.literal_eval(string)
    return dic
def faltan():
    lista_faltan=[]
    for champ in campeones_lista:
        gg=0
        a=open("Info_valiosa.txt","r")
        for linea in a:
            champ0,datos=linea.strip().split("@")
            if champ==champ0:
                gg=1
        a.close()
        if gg==0:
            lista_faltan.append(champ)
    return lista_faltan
def recorrer_paginas():
    for champ in campeones_lista:
        champ_lp=champ
        if (" " in champ) and (champ!='Dr. Mundo'):
            champ_lp=champ
            champ=champ.replace(" ","-")
        elif champ=='Dr. Mundo':
            champ_lp=champ
            champ="dr-mundo"
        elif "'" in champ:
            champ_lp=champ
            champ=champ.replace("'","").lower()
        print champ
        url= "http://www.lolcounter.com/champions/"+champ
        champ=champ_lp        
        print champ  
        respuesta = urllib2.urlopen(url)
        contenidoWeb = respuesta.read()
        a=open("contenido"+champ,"w")
        a.write(contenidoWeb[175000:220000])
        a.close()
        ordenar_contenido("contenido"+champ,champ)
        os.remove("contenido"+champ)
    return "Completado."

def ordenar_contenido(texto_contenido,champ):
    dic={}
    dic_weak={}
    dic_strong={}
    a=open(texto_contenido,"r")
    cont=0
    for linea in a:
        datos=linea.strip().split("'")
        if ("<p>"+champ+" is Weak Against</p>") in datos:
            cont=1
        elif ("<p>"+champ+" is Strong Against</p>") in datos:
            cont=2
        elif ("<p>"+champ+" goes Even With</p>") in datos:
            cont=3  
        if (cont==1 or cont==2) and ("<a href='/champions/" in linea.strip()):
            lc=(datos[1].split("/"))[2]
            dado=""
            count_ca=0
            count_co=0
            for letra in list(lc):
                count_ca+=1
                if count_ca==1:
                    letra=letra.upper()
                if "'"==letra:
                    count_co=1
                elif "-"==letra:
                    letra=" "
                dado+=letra
            lc=dado
            if count_co==1:
                lista_ggwp=["Cho'Gath", "Kha'Zix", "Kog'Maw", "Rek'Sai", "Vel'Koz"]
                gg_co=lc.replace("'","").lower()
                for ggwp in lista_ggwp:
                    cer=ggwp.replace("'","").lower()
                    if cer==gg_co:
                        lc=ggwp
            if (lc in campeones_lista) and (lc!=champ) :
                champ_tem=lc
                #print champ_tem
        if cont==1:
            if ("upvote" in linea)==True:
                datos_0=linea.strip().split().pop()
                up_votesw=""
                for n in datos_0:
                    if n in ["0","1","2","3","4","5","6","7","8","9"]:
                        up_votesw+=n
            elif ("downvote" in linea)==True:
                datos_1=linea.strip().split().pop()
                down_votesw=""
                for m in datos_1:
                    if m in ["0","1","2","3","4","5","6","7","8","9"]:
                        down_votesw+=m
            elif ("<div class='lane tag_" in linea)==True:
                datos_2=(linea.strip().split(">"))[1]
                linea_champw=datos_2[0]+datos_2[1]+datos_2[2]
            elif ("<div class='countertips'>" in linea)==True:
                if (champ_tem in dic_weak)==False:
                    dic_weak[champ_tem]=[up_votesw,down_votesw,linea_champw]
                elif (champ_tem in dic_weak)==True:
                    champ_tem0=champ_tem+"_"+linea_champw
                    dic_weak[champ_tem0]=[up_votesw,down_votesw,linea_champw]
        if cont==2:
            if ("upvote" in linea)==True:
                datos_0=linea.strip().split().pop()
                up_votess=""
                for n in datos_0:
                    if n in ["0","1","2","3","4","5","6","7","8","9"]:
                        up_votess+=n
            elif ("downvote" in linea)==True:
                datos_1=linea.strip().split().pop()
                down_votess=""
                for m in datos_1:
                    if m in ["0","1","2","3","4","5","6","7","8","9"]:
                        down_votess+=m
            elif ("<div class='lane tag_" in linea)==True:
                datos_2=(linea.strip().split(">"))[1]
                linea_champs=datos_2[0]+datos_2[1]+datos_2[2]
            elif ("<div class='countertips'>" in linea)==True:
                if (champ_tem in dic_strong)==False:
                    dic_strong[champ_tem]=[up_votess,down_votess,linea_champs]
                elif (champ_tem in dic_strong)==True:
                    champ_tem0=champ_tem+"_"+linea_champs
                    dic_strong[champ_tem0]=[up_votess,down_votess,linea_champs]  
        if cont==3:
            dic["dic_weak"]=dic_weak
            dic["dic_strong"]=dic_strong
            a.close()
            b=open("Info_valiosa.txt","a")
            b.write(champ+"@"+str(dic)+"\n")
            b.close()
            return "Ordenar_contenido "+champ+" Completado..."


       
def recorrer_paginas2():
    for champ in campeones_lista:
        gg=0
        if (" " in champ) and (champ!='Dr. Mundo'):
            champ=champ.replace(" ","-")
            gg=2
        elif "'" in champ:
            champ=champ.replace("'","")
            gg=1
        elif champ=='Dr. Mundo':
            champ="dr-mundo"
            gg=3
        print champ
        url= "http://www.lolcounter.com/champions/"+champ
        if ("-" in champ) and (gg==2):
            champ=champ.replace("-"," ")
        if (champ=="dr-mundo") and (gg==3):
            champ='Dr. Mundo'  
        if gg==1:
            count_a=0
            agg=list(champ)
            for nn in agg:
                count_a+=1
                champ+=nn
                if count_a==3:
                    champ=champ+"'"
                
        print champ  
        respuesta = urllib2.urlopen(url)
        contenidoWeb = respuesta.read()
        a=open("contenido"+champ,"w")
        a.write(contenidoWeb[175000:220000])
        a.close()
        ordenar_contenido("contenido"+champ,champ)
        os.remove("contenido"+champ)
    return "Completado."

recorrer_pagina2()













                    
                
            
            
            
    
    
