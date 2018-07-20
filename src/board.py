import pygame

from . import config, squares

class Board:
	# def __init__(self):
	# 	self.board_squares = []

	# 	for y in range(config.SQUARE_SIZE // 2, config.WINDOW_HEIGHT - config.SQUARE_SIZE - config.SQUARE_SIZE // 2, int(config.SQUARE_SIZE*1.5)):
	# 		for x in range(config.SQUARE_SIZE // 2, config.MAP_WIDTH - config.SQUARE_SIZE - config.SQUARE_SIZE // 2, int(config.SQUARE_SIZE*1.5)):
	# 			self.board_squares.append(squares.ForSaleSquare(x, y, len(self.board_squares), None))

	def __init__(self, building_list):
		self.board_squares = []

		for b in building_list:
			self.board_squares.append(squares.ForSaleSquare(b[0], b[1], len(self.board_squares), None))

	def draw(self, surface):
		"""Draws all squares in the board to the surface"""
		surface.fill((0, 0xa9, 0x30))
		for s in self.board_squares:
			s.draw(surface)

	def draw_outline(self, surface, mouseX, mouseY):
		"""Draws an outline around the square the mouse is hovering over"""
		for s in self.board_squares:
			if s.rect.collidepoint(mouseX, mouseY):
				pygame.draw.rect(surface, (0xee, 0xdd, 0x2a), (s.x, s.y, config.SQUARE_SIZE + 2, config.SQUARE_SIZE + 2), 1)


	def get_click_index(self, mouseX, mouseY):
		"""Returns the index of the square clicked"""
		for s in self.board_squares:
			if s.rect.collidepoint(mouseX, mouseY):
				return s.index

	def replace_square(self, index, new_square):
		"""Completely replaces the square at a certain index"""
		self.board_squares[index] = new_square

	def get_square(self, index):
		"""Returns the Square object at index"""
		return self.board_squares[index]

	def get_menu(self, index):
		"""Returns the Menu object of the Square at index"""
		return self.board_squares[index].get_menu()
