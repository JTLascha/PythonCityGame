import pygame

from . import assets, config

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
                return EmptySquare(self.building.x, self.building.y, self.building.index, player)

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
                return Restaurant(self.building.x, self.building.y, self.building.index, player)

        elif self.factory_position.collidepoint(mouseX, mouseY):
            if player.money >= 150:
                player.money -= 150
                return Restaurant(self.building.x, self.building.y, self.building.index, player)

        return None
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
        self.baseQoL = 50
        self.QoL = 50
        self.QoLModRange = 1

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

   # call this in the map class updateQoL function
    def updateQoL(self, change):
        self.QoL = self.Qol + change


class ForSaleSquare(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 0)

        self.image = assets.get_image("forsale")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))

        self.rect = self.image.get_rect().move((x, y))

    def get_menu(self):
        return BuyMenu(self)


class EmptySquare(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 0)

        self.image = assets.get_image("empty")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))

    def get_menu(self):
        return BuildMenu(self)



class Restaurant(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 15)

        self.image = assets.get_image("restaurant")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 65
        # TODO: Add building properties

    def get_menu(self):
        pass


class Factory(_BaseSquare):
    def __init__(self, x, y, index, owner):
        _BaseSquare.__init__(self, x, y, index, owner, 300)

        self.image = assets.get_image("factory")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 0
    def get_menu(self):
        pass
