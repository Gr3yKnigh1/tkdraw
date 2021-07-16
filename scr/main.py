from __future__ import annotations

import tkinter as tk

from application import Application


def main() -> None:
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()
	

if (__name__ == "__main__"):
	main()
