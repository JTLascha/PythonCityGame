import pygame

from . import assets, config, person

class _BaseSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, id, owner, max_population):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.id = id
        self.max_population = max_population
        self.people = []
        self.owner = owner

        self.image = None

    def draw(self, surface):
        """Draw the square contents (shared by all buildings)"""
        surface.blit(self.image, self.rect)

    def on_click(self):
        pass

    def add_person(person):
        person.id = self.get_population() + 1
        self.people.append(person)

    def remove_person(person_id):
        for i in range(0, len(self.people)):
            if self.people[i].id == person_id:
                return self.people.pop(i)

    def get_population(self):
        return len(self.people)

    def move_person(self, person_id, dest):
        person = self.remove_person(person_id)
        dest.add_person(person)



""" The values passed for the max population for each square were
    picked pretty much randomly. We will need to actually think about
    reasonable values for these in the future.
"""

class EmptySquare(_BaseSquare):
    def __init__(self, x, y, id, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, id, owner, 200)

        self.image = assets.get_image("empty")
        self.rect = self.image.get_rect().move((x, y))

    def on_click(self, state_machine):
        pass


class Restaurant(_BaseSquare):
    def __init__(self, x, y, id, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, id, owner, 100)

        self.image = assets.get_image("restaurant")
        self.rect = self.image.get_rect()

        # TODO: Add building properties

    def on_click(self, state_machine):
        pass

class Factory(_BaseSquare):
    def __init__(self, x, y, id, owner):
        _BaseSquare.__init__(self, x, y, id, owner, 300)
        
        # TODO: Add image asset

    def on_click(self, state_machine):
        pass
