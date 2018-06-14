'''This is the module that will house the playing field for our class'''
import pygame, sys
from pygame.locals import *
from enum import Enum

#The enum of all the possible building types
class Building(Enum):
	NOTHING = 0
	CAPITAL = 1
	OFFICE = 2

#enum of all the possible land types
class Land(Enum):
	SEA = 0
	GRASS = 1
	FOREST = 2
	MOUNTAIN = 3

#enum of all the road types
class Road(Enum):
	NONE = 0
	UP = 1
	DOWN = 2
	LEFT = 4
	RIGHT = 8
	UPDOWN = 3
	UPLEFT = 5
	UPRIGHT = 9
	LEFTRIGHT = 12
	LEFTDOWN = 6
	RIGHTDOWN = 10
	

class MyStruct():
	def __init__(self,rect,ownership = -1,field = Land.GRASS,building = Building.NOTHING,road = Road.NONE):
		self.rectangle = rect
		self.owner = ownership
		self.landType = field
		self.buildingType = building
		self.roadType = road

	
class board():
	#so you need to pass it in a display so it can add the rects and everything
	#the defaults are ultimately meaningless, and are just there to make testing easier
	def __init__(self, display,gameSpace = 512,fWidth=16,fHight=16,fyBuffer = 20, fxBuffer= 384): #eventually this will have display, and a file name be passed in, we read in from the file, and then add in the rectangles
		self.field = []
		self.display = display
		self.GAMESPACE = gameSpace
		self.YBUFFER = fyBuffer
		self.XBUFFER = fxBuffer
		self.WIDTH = fWidth
		self.HIGHT = fHight
		if self.HIGHT < self.WIDTH:
			self.TILESIZE = gameSpace/self.WIDTH
		else:
			self.TILESIZE = gameSpace/self.HIGHT
		pygame.font.init()
		self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
		for y in range(0,self.HIGHT):
			self.field.append([])
		for y in range(0,self.HIGHT):
			for x in range(0,self.WIDTH):
				self.field[y].append(MyStruct(pygame.draw.rect(self.display, (((x+y)%2)*255,((x+y)%2)*255,((x+y)%2)*255),(x*self.TILESIZE,self.YBUFFER +y*self.TILESIZE,self.TILESIZE,self.TILESIZE))))
		
		self.field[0][0].owner = 0
		self.field[0][0].buildingType = Building.CAPITAL
		self.field[self.HIGHT-1][self.WIDTH-1].owner = 1
		self.field[self.HIGHT-1][self.WIDTH-1].buildingType = Building.CAPITAL
		pygame.draw.rect(self.display, (0*77,(0+1)*123%255,(0+2)*79%255),(0*self.TILESIZE,self.YBUFFER +0*self.TILESIZE,self.TILESIZE,self.TILESIZE))
		pygame.draw.rect(self.display, (1*77,(1+1)*123%255,(1+2)*79%255),(15*self.TILESIZE,self.YBUFFER +15*self.TILESIZE,self.TILESIZE,self.TILESIZE))
		
	def printMessage(self, string,locX,locY):
		textsurface = self.myfont.render(string,False,(0,255,0),12)
		self.display.blit(textsurface,(locX,locY))
		pygame.display.update()

	#checks if a tile is next to an already owned tile
	def nextToOwned(self,player, X, Y):	
		if X != 0 and self.field[Y][X-1].owner == player:
			return True
		elif Y != 0 and self.field[Y-1][X].owner == player:
			return True
		elif Y != self.HIGHT-1 and self.field[Y+1][X].owner == player:
			return True
		elif X != self.WIDTH-1 and self.field[Y][X+1].owner == player:
			return True
		else:
			return False
		
	def resetBars(self): #right now just sets it back to a black space, but later will need to redraw any information we have up
		pygame.draw.rect(self.display,(0,0,0),(0,0,self.GAMESPACE+self.XBUFFER,self.YBUFFER))
		pygame.draw.rect(self.display,(0,0,0),(self.GAMESPACE,0,self.XBUFFER,self.GAMESPACE+self.YBUFFER))
		pygame.display.update()
	
	def buyTile(self,player,locX,locY):
		self.resetBars()
		locX = int(locX/self.TILESIZE)
		locY = int((locY-20)/self.TILESIZE)
		if self.field[locY][locX].owner != -1:
			string = "That tile is already owned by " + str(self.field[locY][locX].owner)
			self.printMessage(string,self.GAMESPACE,128)
			return False
		elif self.nextToOwned(player,locX,locY):
			string = "Player " + str(player) + " do you want to buy this tile?"
			self.printMessage(string,self.GAMESPACE,128)
			string = "Yes"
			self.printMessage(string,self.GAMESPACE,148)
			string = "No"
			self.printMessage(string,self.GAMESPACE+40,148)
			while True:
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						mousex,mousey = event.pos
						if mousex > self.GAMESPACE:
							if mousey > 148 and mousey < 168:
								if mousex < self.GAMESPACE+40:
									self.field[locY][locX].owner = player
									pygame.draw.rect(self.display, (player*77,(player+1)*123%255,(player+2)*79%255),(locX*self.TILESIZE,self.YBUFFER +locY*self.TILESIZE,self.TILESIZE,self.TILESIZE))
									self.resetBars()
									return True
								else: 
									self.resetBars()
									return False
		else:
			string = str(player) + " need to own a tile next to this to buy it!"
			self.printMessage(string,self.GAMESPACE,128)
			return False
		
		
	
	
	