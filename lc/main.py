import tkinter as tk
from tkinter import  ttk, Tk, messagebox as mbox
from api.champion import Champion	
from gui.searchLayout import SearchLayout
from PIL import Image, ImageTk 

version = '0.2.0 \'Iron 2\''
class App():

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
	
	def __init__(self, _version):
		self.window = Tk()
		self.window.title('LOL Data')
		self.window.resizable(0,0)
		self.menu()
		self.version = _version
		self.s_widget = SearchLayout(self.window,self.champion_list)
		self.version_label = ttk.Label(self.window, text=self.version).grid(column=0,row=10)
		self.window.mainloop()

	def _quit(self):
		self.window.quit()
		self.window.destroy()
		exit()


	def aboutmsg(self):
		mbox.showinfo('LOL Data', self.version
					+'\n\n2018, hecho por Lukas Gutiérrez.\nProyecto bajo licencia MIT.' 
					+'\nhttps://github.com/Legutier/lol-counter/blob/master/LICENSE' 
					+'\n\nContacto:\nlukasgutierrezlisboa@gmail.com')


	def search_layout(self):
		self.s_widget.delete()
		self.s_widget = SearchLayout(self.window, self.champion_list)


	def menu(self):
		menu_bar =  tk.Menu(self.window)
		self.window.config(menu=menu_bar)
		menu_inicio = tk.Menu(menu_bar, tearoff = 0)
		menu_inicio.add_command(label='buscar',command=self.search_layout)
		menu_inicio.add_separator()
		menu_inicio.add_command(label='Salir', command=self._quit)
		menu_bar.add_cascade(label="Inicio", menu=menu_inicio)
		menu_help = tk.Menu(self.window)
		menu_help.add_command(label='About', command = self.aboutmsg)
		menu_bar.add_cascade(label='Ayuda', menu=menu_help)	


if __name__ == "__main__":
	App(version)
