import pygame

from . import config, squares

class Board:
	def __init__(self, num_players):
		self.num_players = num_players

		self.board_squares = []

		for y in range(config.SQUARE_SIZE//2, config.WINDOW_SIZE - config.SQUARE_SIZE//2, config.SQUARE_SIZE*2):
			for x in range(config.SQUARE_SIZE//2, config.WINDOW_SIZE - config.SQUARE_SIZE//2, config.SQUARE_SIZE*2):
				self.board_squares.append(squares.EmptySquare(x, y, len(self.board_squares), None))

	def draw(self, surface):
		surface.fill((0, 255, 0))
		for s in self.board_squares:
			s.draw(surface)

	def get_click_id(self, mouseX, mouseY):
		for s in self.board_squares:
			if mouseX >= s.x and mouseX <= s.x + 32:
				if mouseY >= s.y and mouseY <= s.x + 32:
					return s.id

	def replace_square(self, id, new_square):
		self.board_squares[id] = new_square

	def get_square(self, id):
		return self.board_squares[id]
