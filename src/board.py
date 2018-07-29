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
        self.rows = 6 				# These are hardcoded to 6 for our current board.
        self.columns = 6			# If we implement different sizes of boards, these will need to be set based on the board.

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

    def replace_square(self, index, square_type, owner):
        """Completely replaces the square at a certain index"""
        self.board_squares[index] = square_type(self.board_squares[index].x, self.board_squares[index].y, index, owner)

    def get_square(self, index):
        """Returns the Square object at index"""
        return self.board_squares[index]

    def get_menu(self, index):
        """Returns the Menu object of the Square at index"""
        return self.board_squares[index].get_menu()

    def genProfit(self):
        """Iterates through the board getting the profit of each square adds it to the player list and returns it"""
        p = []
        for temp in range(0, 2):
            p.append(0)
        for s in self.board_squares:
            profit = s.produce()
            if profit[0] is not None:
                p[profit[0].num] += profit[1]
        return p

    def updateQoL(self):
	"""Iteratres through the board updating the QoL of each square"""
	#neighbors is a set of numbers to add to index x to get x's neighboring squares
	neighbors = set([0, -1 - self.columns, -self.columns, 1 -self.columns, -1, 0, 1, self.columns - 1, self.columns, self.columns + 1])
	for x in range(0,len(self.board_squares)):
		#check is the subset of neighbors we're actually going to check
		QoL = 0
		count = 0
		check = neighbors
		if x % self.columns == 0:
			check = check - set([-self.columns -1, -1, self.columns - 1])
		elif x % self.columns == self.columns - 1:
			check = check - set([1 - self.columns, 1, self.columns + 1])
		if int(x / self.columns) == 0:
			check = check - set([-self.columns - 1, -self.columns, 1 - self.columns])
		elif int(x / self.columns) == self.rows - 1:
			check = check - set([self.columns - 1, self.columns, self.columns + 1])
		for n in check:
			QoL += self.board_squares[x + n].getOldQoL()
			count += 1
		QoL = QoL / count
		self.board_squares[x].updateQoL(QoL)
