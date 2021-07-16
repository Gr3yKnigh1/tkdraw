from __future__ import annotations
from typing import Optional

import tkinter as tk
import tkinter.colorchooser
import tkinter.filedialog

from color import Color
from stroke import Stroke
from utils import sign


class Sketchpad(tk.Canvas):

	last_pos: list[Optional[int]]
	is_drawing: bool
	width_change_step: int

	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self.files = [
			("All Files", "."), 
			("png", "*.png")
		]
		
		self.width_change_step = 1

		self.stroke = Stroke()
		self.stroke.width = 3

		self.last_pos = [None, None]
		self.is_drawing = False

		# Bindings
		self.bind("<Motion>", self.add_line)
		self.bind("<ButtonPress-1>", self.start_drawing)
		self.bind("<ButtonRelease-1>", self.stop_drawing)
		self.master.master.bind("c", self.choose_color)
		self.bind("<MouseWheel>", self.change_width)
		self.master.master.bind("s", self.save_canvas)

	def add_line(self, event) -> None:
		if self.is_drawing:
			self.create_line(self.last_pos[0], self.last_pos[1], event.x, event.y, 
				width=self.stroke.width, 
				fill=self.stroke.color.to_code()
				)
			self.last_pos = [event.x, event.y]

	def reset_last_positions(self) -> None:
		self.last_pos = [None, None]

	def start_drawing(self, event) -> None:
		self.is_drawing = True
		self.last_pos = [event.x, event.y]

	def stop_drawing(self, event) -> None:
		self.is_drawing = False
		self.reset_last_positions()

	def choose_color(self, event) -> None:
		print(1)
		color_code = tk.colorchooser.askcolor(title ="Choose color")
		self.stroke.color = Color(*color_code[0])

	def change_width(self, event) -> None:
		self.stroke.width += self.width_change_step * sign(event.delta)
		
		if self.stroke.width <= 0:
			self.stroke.width = 1
		elif self.stroke.width >= 20:
			self.stroke.width = 20

	def save_canvas(self, event) -> None:
		fev = self.postscript(file = 'if.ps')
		file = tk.filedialog.asksaveasfile(defaultextension = '.jpg')
		img = Image.open(fev)
		img.save(file + ".jpg")
