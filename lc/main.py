import tkinter as tk
from tkinter import  ttk, Tk, messagebox as mbox
from champion import Champion	
from PIL import Image, ImageTk 

champion_list = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", 
"Ashe", "Aurelion Sol", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", 
"Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", 
"Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", 
"Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", 
"Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx","Kai'sa", "Kalista", "Karma", 
"Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", 
"Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", 
"Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", 
"Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu", "Olaf", 
"Orianna", "Ornn", "Pantheon", "Poppy", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Renekton", 
"Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", 
"Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Tailyah", 
"Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", 
"Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", 
"Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yorick", "Zac", 
"Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]
#a = Champion('Singed')
#a.get_guides()
#print(a.get_counters())


def search(champion):
	counter_label = []
	i = 0
	query =Champion(champion)
	query_frame = ttk.LabelFrame(window)
	query_frame.grid(column=0,row=1)
	counters = query.get_counters()
	for counter in counters:
		counter_label.append(ttk.Label(query_frame, text = counter))
	for label in counter_label:	
		label.grid(column=i, row=0)
		i += 1


def _quit():
	window.quit()
	window.destroy()
	exit()


def aboutmsg():
	mbox.showinfo('LOL counter 0.1.0', '2018, hecho por Lukas Gutiérrez.\n\nContacto:\nlukasgutierrezlisboa@gmail.com')


def menu():
	menu_bar =  tk.Menu(window)
	window.config(menu=menu_bar)
	menu_inicio = tk.Menu(menu_bar, tearoff = 0)
	menu_inicio.add_command(label='buscar')
	menu_inicio.add_separator()
	menu_inicio.add_command(label='Salir', command=_quit)
	menu_bar.add_cascade(label="Inicio", menu=menu_inicio)
	menu_help = tk.Menu(window)
	menu_help.add_command(label='About', command = aboutmsg)
	menu_bar.add_cascade(label='Ayuda', menu=menu_help)
	

def search_layout():
	search_frame = ttk.LabelFrame(window)
	search_frame.grid(column= 0, row = 0, padx=20, pady=20)
	label = ttk.Label(search_frame, text="Escoge el campeón")
	label.grid(column=0,row=0)
	champion = tk.StringVar()
	champion_chosen = ttk.Combobox(search_frame, width=12, textvariable=champion)
	champion_chosen['values'] = champion_list
	champion_chosen.grid(column=0, row= 3)
	Search_button = ttk.Button(search_frame, text="Buscar", command=lambda: search(champion.get()))
	Search_button.grid(column=1, row=3)


if __name__ == "__main__":
	window = Tk()
	#	window.iconbitmap(r'.\src\favicon.ico')
	window.title('LOL data')
	window.resizable(0, 0)		
	menu()
	search_layout()
	window.mainloop()

