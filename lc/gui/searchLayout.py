import tkinter as tk
from tkinter import ttk, Tk, messagebox as mbox
from api.champion import Champion	

class SearchLayout():
	'''
	Tkinter Layout for LOL data search widget.
	'''
	def __init__(self, window, champion_list,_bg,_fg):
		'''
		Search layout is initialized.
		'''
		#variables are set
		self._bg = _bg
		self._fg = _fg
		self.frame = tk.Frame(window)
		self.frame.config(bg=_bg)
		self.frame.grid(column=0,row=0)
		self.champion_list = champion_list
		self.query_frame = tk.LabelFrame(self.frame, bg=self._bg)
		self.query_frame.config(bg=self._bg, fg = self._fg)
		self.search_frame = tk.LabelFrame(self.frame)
		self.search_frame.config(fg = self._fg, bg = self._bg)
		self.champion = tk.StringVar()
		self.search_frame.grid(column= 0, row = 0, padx=20, pady=20)
		#we call layout to show
		self.layout()
		return
		
	def layout(self):
		#the initial widget is set
		label = tk.Label(self.search_frame, text="Escoge el campeón", fg=self._fg,bg=self._bg)
		label.grid(column=0,row=0)
		champion = tk.StringVar()
		champion_chosen = ttk.Combobox(self.search_frame, width=12, textvariable=self.champion)
		champion_chosen['values'] = self.champion_list
		champion_chosen.grid(column=0, row= 3)
		Search_button = tk.Button(self.search_frame, text="Buscar", fg=self._fg, bg=self._bg,
								  command=lambda: self.search(self.champion.get()))
		Search_button.grid(column=1, row=3)
		return

	def search(self, champion):
		champs_label = []
		'''
		Returns counters of champion on widget.
		'''
		i = 0
		#clear previous area for counters if needed
		self.query_frame.grid_remove()
		self.query_frame = tk.Frame(self.frame)
		#the query is done via Champion API
		query =Champion(champion)
		self.query_frame.grid(column=0,row=1)
		counters = query.get_counters()
		worst = query.get_strongs()
		#champions are added on counter list
		counter_frame = tk.LabelFrame(self.query_frame, bg=self._bg)
		counter_frame.grid(column=0,row=0)
		for counter in counters:
			champs_label.append(tk.Label(counter_frame, text = counter, fg = self._fg, bg = self._bg))
		title = tk.Label(counter_frame, text = 'Best against '+champion, fg = self._fg, bg = self._bg)
		title.grid(column=0,row=0)
		separator = ttk.Separator(counter_frame,orient= tk.HORIZONTAL)
		separator.grid(row = 1, sticky='ew')
		for label in champs_label:	
			label.grid(column=0, row=i+2)
			i += 1
		separator_column = ttk.Separator(self.query_frame, orient=tk.VERTICAL)
		separator_column.grid(column=1,sticky="ns")
		#this are the worst champions against it.
		worst_frame = tk.LabelFrame(self.query_frame, bg = self._bg, fg = self._fg)
		worst_frame.grid(column=2,row=0)
		champs_label = []
		i=0
		for champ in worst:
			champs_label.append(tk.Label(worst_frame, text = champ, bg=self._bg, fg = self._fg))
		title = tk.Label(worst_frame, text = 'Worst against ' + champion, bg=self._bg, fg = self._fg)
		title.grid(column=0,row=0)
		separator_w = ttk.Separator(worst_frame, orient=tk.HORIZONTAL)
		separator_w.grid (row = 1, sticky ="ew")
		for label in champs_label:
			label.grid(column=0, row=i+2)
			i+=1
		return

	def delete(self):
		self.frame.grid_remove()