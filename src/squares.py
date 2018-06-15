import pygame

from . import assets, config

class _BaseSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, id, owner):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.id = id
        self.owner = owner

        self.image = None

    def draw(self, surface):
        """Draw the square contents (shared by all buildings)"""
        surface.blit(self.image, self.rect)

    def on_click(self):
        pass


class EmptySquare(_BaseSquare):
    def __init__(self, x, y, id, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, id, owner)

        self.image = assets.get_image("empty")
        self.rect = self.image.get_rect().move((x, y))

    def on_click(self, state_machine):
        pass


class Restaurant(_BaseSquare):
    def __init__(self, x, y, id, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, id, owner)

        self.image = assets.get_image("restaurant")
        self.rect = self.image.get_rect()

        # TODO: Add building properties

    def on_click(self, state_machine):
        pass

