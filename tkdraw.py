from __future__ import annotations

import tkinter as tk


def sign(x: int) -> int:
	return x / abs(x)


class Color(object):

	r: int
	g: int
	b: int

	def __init__(self, r: int, g: int, b: int) -> None:
		self.r = r
		self.g = g
		self.b = b

	def to_code(self) -> str:
		return Color.get_code(self.r, self.g, self.b)

	@staticmethod
	def get_code(r: int, g: int, b: int) -> str:
		return f'#{r:02x}{g:02x}{b:02x}'


class Stroke(object):

	color: Color
	width: int

	def __init__(self) -> None:
		self.color = Color(0, 0, 0)
		self.width = 1


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


	# ToDO(Gr3yKnigh1): Replace with square instead of line
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
		if color_code is None:
			return
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


def main() -> None:
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()
	

if (__name__ == "__main__"):
	main()
