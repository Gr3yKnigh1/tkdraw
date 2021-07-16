from __future__ import annotations

from color import Color


class Stroke(object):

	color: Color
	width: int

	def __init__(self) -> None:
		self.color = Color(0, 0, 0)
		self.width = 1
