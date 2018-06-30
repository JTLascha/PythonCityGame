import pygame

class _Menu:
    """Base menu object"""
    def __init__(self, building):
        self.building = building

    def draw(self, surface):
        """Draws the contents of the menu to the surface"""
        pass

    def handle_click(self, mouse_pos):
        """Handles any mouse click events on the menu"""
        pass

class BuyMenu(_Menu):
    def __init__(self, building):
        _Menu.__init__(self, building)

        self.font = pygame.font.Font(None, 32)

    def draw(self, surface):
        building_text = self.font.render("Building #" + str(self.building.index), 1, (255, 255,255))
        surface.blit(building_text, building_text.get_rect())

        price_text = self.font.render("Price: $200", 1, (255, 255,255))
        surface.blit(price_text, price_text.get_rect().move(0, 50))

    def handle_click(self, mouse_pos):
        pass
