from __future__ import annotations


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
