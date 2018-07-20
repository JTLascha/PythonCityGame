import pygame

from . import assets, config, menus, person

class _BaseSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, index, owner, max_population):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.index = index
        self.owner = owner
        self.max_population = max_population
        self.people = []

        self.image = None

    def draw(self, surface):
        """Draw the square contents (shared by all buildings)"""
        surface.blit(self.image, self.rect)

    def get_menu(self):
        """Get menu object referencing this square (self)"""
        pass

    def add_person(self, person):
        """Adds a person object to the square"""
        person.id = self.get_population() + 1
        self.people.append(person)

    def remove_person(self, person_id):
        """Removes and returns the person with the given id from the square"""
        for i in range(0, len(self.people)):
            if self.people[i].id == person_id:
                return self.people.pop(i)

    def get_population(self):
        """Number of people in the square"""
        return len(self.people)

    def move_person(self, person_id, dest):
        """Removes person from this square and adds them to the given square"""
        person = self.remove_person(person_id)
        dest.add_person(person)


class ForSaleSquare(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 0)

        self.image = assets.get_image("forsale")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))

        self.rect = self.image.get_rect().move((x, y))

    def get_menu(self):
        return menus.BuyMenu(self)


class EmptySquare(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 0)

        self.image = assets.get_image("empty")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))

    def get_menu(self):
        return menus.BuildMenu(self)
        


class Restaurant(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 15)

        self.image = assets.get_image("restaurant")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))

        # TODO: Add building properties

    def get_menu(self):
        pass


class Factory(_BaseSquare):
    def __init__(self, x, y, index, owner):
        _BaseSquare.__init__(self, x, y, index, owner, 300)
        
        self.image = assets.get_image("factory")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))

    def get_menu(self):
        pass
