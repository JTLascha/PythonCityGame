import pygame

from . import squares

class _Menu:
    """Base menu object"""
    def __init__(self, building):
        self.building = building
        self.font = pygame.font.Font(None, 32)

    def draw(self, surface):
        """Draws the contents of the menu to the surface"""
        pass

    def handle_click(self, mouseX, mouseY):
        """Handles any mouse click events on the menu"""
        pass

class BuyMenu(_Menu):
    def __init__(self, building):
        _Menu.__init__(self, building)

    def draw(self, surface):
        building_text = self.font.render("Lot #" + str(self.building.index), 1, (255, 255,255))
        surface.blit(building_text, building_text.get_rect())

        price_text = self.font.render("Price: $200", 1, (255, 255,255))
        surface.blit(price_text, price_text.get_rect().move(0, 50))

        self.buy_button = self.font.render("Buy!", 1, (255, 255, 0), (150, 150, 150))
        self.buy_position = self.buy_button.get_rect().move(0, 100)
        surface.blit(self.buy_button, self.buy_position)

    def handle_click(self, mouseX, mouseY, player):
        if self.buy_position.collidepoint(mouseX, mouseY):
            if player.money >= 200:
                player.money -= 200
                return squares.EmptySquare(self.building.x, self.building.y, self.building.index, player)

        return None

class BuildMenu(_Menu):
    def __init__(self, building):
        _Menu.__init__(self, building)

    def draw(self, surface):
        building_text = self.font.render("Lot #" + str(self.building.index), 1, (255, 255,255))
        surface.blit(building_text, building_text.get_rect())

        self.restaurant_button = self.font.render("Build Restaurant ($100)", 1, (255, 255, 0), (150, 150, 150))
        self.restaurant_position = self.restaurant_button.get_rect().move(0, 100)
        surface.blit(self.restaurant_button, self.restaurant_position)

        self.factory_button = self.font.render("Build Factory ($150)", 1, (255, 255, 0), (150, 150, 150))
        self.factory_position = self.factory_button.get_rect().move(0, 150)
        surface.blit(self.factory_button, self.factory_position)

    def handle_click(self, mouseX, mouseY, player):
        if self.restaurant_position.collidepoint(mouseX, mouseY):
            if player.money >= 100:
                player.money -= 100
                return squares.Restaurant(self.building.x, self.building.y, self.building.index, player)

        elif self.factory_position.collidepoint(mouseX, mouseY):
            if player.money >= 150:
                player.money -= 150
                return squares.Restaurant(self.building.x, self.building.y, self.building.index, player)

        return None
