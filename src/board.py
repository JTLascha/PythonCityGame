import pygame

from . import config, squares

class Board:
	def __init__(self, num_players):
		self.num_players = num_players

		self.board_squares = []

		for y in range(config.SQUARE_SIZE // 2, config.WINDOW_HEIGHT - config.SQUARE_SIZE - config.SQUARE_SIZE // 2, int(config.SQUARE_SIZE*1.5)):
			for x in range(config.SQUARE_SIZE // 2, config.MAP_WIDTH - config.SQUARE_SIZE - config.SQUARE_SIZE // 2, int(config.SQUARE_SIZE*1.5)):
				self.board_squares.append(squares.ForSaleSquare(x, y, len(self.board_squares), None))

	def draw(self, surface):
		surface.fill((0, 0xa9, 0x30))
		for s in self.board_squares:
			s.draw(surface)

	def draw_outline(self, surface, mouseX, mouseY):
		for s in self.board_squares:
			if s.rect.collidepoint(mouseX, mouseY):
				pygame.draw.rect(surface, (0xee, 0xdd, 0x2a), (s.x, s.y, config.SQUARE_SIZE + 2, config.SQUARE_SIZE + 2), 1)


	def get_click_index(self, mouseX, mouseY):
		for s in self.board_squares:
			if s.rect.collidepoint(mouseX, mouseY):
				return s.index

	def replace_square(self, index, new_square):
		self.board_squares[index] = new_square

	def get_square(self, index):
		return self.board_squares[index]

	def get_menu(self, index):
		return self.board_squares[index].get_menu()
