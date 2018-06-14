import pygame, sys
import board as BoardClass
from pygame.locals import *

pygame.init()

#this is setting up the size of the screen and all the buffers needed for the main game
GAMESPACE = 512 #this is how much space we want to have the main game take place in
yBuffer = 20 #buffer on top
xBuffer = 384 # buffer on right for info
DISPLAYSURF = pygame.display.set_mode((GAMESPACE+xBuffer,GAMESPACE+yBuffer)) #creating the screen

pygame.display.set_caption('PythonCityGame') #naming it

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0, 255)
fpsClock = pygame.time.Clock()

PLAYERS = 4 #temp
mousex = 0
mousey = 0


field = BoardClass.board(DISPLAYSURF,GAMESPACE,16,16,yBuffer,xBuffer)

'''
board = []
for x in range(0,16):
	board.append([])
for y in range(0,16):
	for x in range(0,16):
		#board[y].append(pygame.Rect((16+x*32,16+y*32),(size))
		#board[y][x].move(16+x*32,16+y*32)
		#color = (x*32,y*32,0)
		board[y].append(pygame.draw.rect(DISPLAYSURF, (x*10%255,y*10%255,y*x*10%255),(x*32,24+y*32,32,32)))
		#DISPLAYSURF.fill(((x*32)%255,(y*32)%255,(x%y*32)%255),board[y][x])
'''
numOfPlayers = 2
player = 0
pygame.display.update()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mousex,mousey = event.pos
			if mousex < GAMESPACE and ( mousey > yBuffer and mousey < GAMESPACE + yBuffer):
				if field.buyTile(player,mousex,mousey):
					player= (player+1)%numOfPlayers
		#elif event.type == pygame.MOUSEBUTTONUP:
			#field.resetBars()
		#DISPLAYSURF.fill((mousex%255,mousey%255,0))
		pygame.display.update()
		