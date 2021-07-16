from __future__ import annotations

import tkinter as tk

from sketchpad import Sketchpad


class Application(tk.Frame):

	def __init__(self, master: tk.Tk=None) -> None:
		super().__init__(master)

		self.master.title("Sketchpad")
		self.master.geometry("900x600")
		self.on_widgets_load()
		self.pack()


	def on_widgets_load(self) -> None:
		c = Sketchpad(master=self, width=900, height=600, bg="white")
		c.pack()

		# Bindings
		self.master.bind("<Escape>", lambda event: self.master.destroy())
