from champion import Champion

champion_list = ["Alistar", "Annie", "Ashe", "Fiddlesticks", "Jax", "Kayle", "Master Yi", "Morgana",
"Nunu", "Ryze", "Sion", "Sivir", "Soraka", "Teemo", "Tristana", "Twisted Fate",
"Warwick", "Singed", "Zilean", "Evelynn", "Twitch", "Tryndamere", "Karthus",
"Amumu", "Cho'Gath", "Anivia", "Rammus", "Veigar", "Kassadin", "Gangplank",
"Taric", "Malphite", "Janna", "Blitzcrank", "Dr. Mundo", "Katarina", "Corki",
"Nasus", "Heimerdinger", "Shaco", "Udyr", "Nidalee", "Poppy", "Gragas"]

a = Champion('Singed')
print(a.get_counters())
print(a.get_guides())
