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

        owner_text = self.font.render("Owner: Player " + str(self.building.owner.num + 1), 1, (255,255,255))
        owner_position = owner_text.get_rect().move(0, 50)
        surface.blit(owner_text, owner_position)

        self.restaurant_button = self.font.render("Build Restaurant ($100)", 1, (255, 255, 0), (150, 150, 150))
        self.restaurant_position = self.restaurant_button.get_rect().move(0, 100)
        surface.blit(self.restaurant_button, self.restaurant_position)

        self.factory_button = self.font.render("Build Factory ($150)", 1, (255, 255, 0), (150, 150, 150))
        self.factory_position = self.factory_button.get_rect().move(0, 150)
        surface.blit(self.factory_button, self.factory_position)

    def handle_click(self, mouseX, mouseY, player):
        if self.restaurant_position.collidepoint(mouseX, mouseY):
            if player.money >= 100:
                if self.building.owner.num != player.num:
                    return None

                player.money -= 100
                return Restaurant(self.building.x, self.building.y, self.building.index, player)

        elif self.factory_position.collidepoint(mouseX, mouseY):
            if player.money >= 150:
                if self.building.owner.num != player.num:
                    return None

                player.money -= 150
                return Factory(self.building.x, self.building.y, self.building.index, player)

        return None

class OwnedMenu(_Menu):
    def __init__(self, building):
        _Menu.__init__(self, building)

    def draw(self, surface):
        building_text = self.font.render("Owner: Player " + str(self.building.owner.num + 1), 1, (255, 255, 255))
        surface.blit(building_text, building_text.get_rect())

        building_qol_text = self.font.render("Quality of Life: " + str(self.building.QoL), 1, (255, 255, 255))
        qol_position = building_qol_text.get_rect().move(0, 100)
        surface.blit(building_qol_text, qol_position)

        profit_text = self.font.render("Profit: " + str(self.building.profits), 1, (255, 255, 255))
        profit_position = profit_text.get_rect().move(0, 50)
        surface.blit(profit_text, profit_position)

class HelpMenu(_Menu):
    def __init__(self):
        _Menu.__init__(self, None)

    def draw(self, surface):
        enter_text = "Press Enter to end your turn."
        m_key_text = "Press m to mute."
        f_key_text = "Press f to toggle fps."
        esc_text   = "Press esc to quit."

        enter = self.font.render(enter_text, 1, (255, 255, 255))
        surface.blit(enter, enter.get_rect())
        
        m_key = self.font.render(m_key_text, 1, (255, 255, 255))
        m_key_position = m_key.get_rect().move(0, 30)
        surface.blit(m_key, m_key_position)

        f_key = self.font.render(f_key_text, 1, (255, 255, 255))
        f_key_position = f_key.get_rect().move(0, 60)
        surface.blit(f_key, f_key_position)

        esc_key = self.font.render(esc_text, 1, (255, 255, 255))
        esc_key_position = esc_key.get_rect().move(0, 90)
        surface.blit(esc_key, esc_key_position)

class _BaseSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, index, owner, max_population):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        self.profits = 0
        self.x = x
        self.y = y
        self.index = index
        self.owner = owner
        self.max_population = max_population
        self.image = None
        self.QoL = 0
        self.baseQoL = 0

    def produce(self):
        money = self.profits * self.QoL / 100
        return (self.owner, money)

    def draw(self, surface):
        """Draw the square contents (shared by all buildings)"""
        surface.blit(self.image, self.rect)

    def get_menu(self):
        """Get menu object referencing this square (self)"""
        pass

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

        self.image = assets.get_image("restaurant" + str(self.owner.num))
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 80
        self.baseQoL = 80
        self.profits = 50

    def get_menu(self):
        return OwnedMenu(self)

class Factory(_BaseSquare):
    def __init__(self, x, y, index, owner):
        _BaseSquare.__init__(self, x, y, index, owner, 300)

        self.image = assets.get_image("factory" + str(self.owner.num))
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 0
        self.baseQoL = 0
        self.profits = 400
    def get_menu(self):
        return OwnedMenu(self)
