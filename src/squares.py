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

        building_qol_text = self.font.render("Quality of Life: " + str(self.building.QoL), 1, (255, 255, 255))
        qol_position = building_qol_text.get_rect().move(0, 50)
        surface.blit(building_qol_text, qol_position)

        price_text = self.font.render("Price: $200", 1, (255, 255,255))
        surface.blit(price_text, price_text.get_rect().move(0, 100))

        self.buy_button = self.font.render("Buy!", 1, (255, 255, 0), (150, 150, 150))
        self.buy_position = self.buy_button.get_rect().move(0, 150)
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
        owner_position = owner_text.get_rect().move(0, 100)
        surface.blit(owner_text, owner_position)

        building_qol_text = self.font.render("Quality of Life: " + str(self.building.QoL), 1, (255, 255, 255))
        qol_position = building_qol_text.get_rect().move(0, 50)
        surface.blit(building_qol_text, qol_position)

        self.restaurant_button = self.font.render("Build Restaurant ($100)", 1, (255, 255, 0), (150, 150, 150))
        self.restaurant_position = self.restaurant_button.get_rect().move(0, 150)
        surface.blit(self.restaurant_button, self.restaurant_position)

        self.factory_button = self.font.render("Build Factory ($100)", 1, (255, 255, 0), (150, 150, 150))
        self.factory_position = self.factory_button.get_rect().move(0, 200)
        surface.blit(self.factory_button, self.factory_position)

        self.park_button = self.font.render("Build Park ($50)", 1, (255, 255, 0), (150, 150, 150))
        self.park_position = self.park_button.get_rect().move(0, 250)
        surface.blit(self.park_button, self.park_position)

        self.blight_button = self.font.render("Build Blight ($50)", 1, (255, 255, 0), (150, 150, 150))
        self.blight_position = self.blight_button.get_rect().move(0, 300)
        surface.blit(self.blight_button, self.blight_position)

        self.sell_button = self.font.render("Sell the Land for $100", 1, (255, 255, 0), (150, 150, 150))
        self.sell_position = self.sell_button.get_rect().move(0, 350)
        surface.blit(self.sell_button, self.sell_position)


    def handle_click(self, mouseX, mouseY, player):
        if self.restaurant_position.collidepoint(mouseX, mouseY):
            if player.money >= 100:
                if self.building.owner.num != player.num:
                    return None

                player.money -= 100
                return Restaurant(self.building.x, self.building.y, self.building.index, player)

        elif self.factory_position.collidepoint(mouseX, mouseY):
            if player.money >= 100:
                if self.building.owner.num != player.num:
                    return None

                player.money -= 100
                return Factory(self.building.x, self.building.y, self.building.index, player)

        elif self.park_position.collidepoint(mouseX, mouseY):
            if player.money >= 50:
                if self.building.owner.num != player.num:
                    return None

                player.money -= 50
                return PublicPark(self.building.x, self.building.y, self.building.index, player)

        elif self.blight_position.collidepoint(mouseX, mouseY):
            if player.money >= 50:
                if self.building.owner.num != player.num:
                    return None

                player.money -= 50
                return Blight(self.building.x, self.building.y, self.building.index, player)

        elif self.sell_position.collidepoint(mouseX, mouseY):
            if self.building.owner.num != player.num:
                return None

                player.money += 100
                return ForSaleSquare(self.building.x, self.building.y, self.building.index, player)

        return None

class OwnedMenu(_Menu):
    def __init__(self, building):
        _Menu.__init__(self, building)

    def draw(self, surface):
        building_text = self.font.render("Owner: Player " + str(self.building.owner.num + 1), 1, (255, 255, 255))
        surface.blit(building_text, building_text.get_rect())

        building_qol_text = self.font.render("Quality of Life: " + str(self.building.QoL), 1, (255, 255, 255))
        qol_position = building_qol_text.get_rect().move(0, 50)
        surface.blit(building_qol_text, qol_position)

        profit_text = self.font.render("Profit: " + str(self.building.profits), 1, (255, 255, 255))
        if(self.building.fee):
            profit_text = self.font.render("Fees: " + str(self.building.profits * -1), 1, (255, 255, 255))
            profit_position = profit_text.get_rect().move(0, 100)
            surface.blit(profit_text, profit_position)

        self.demolish_button = self.font.render("Demolish", 1, (255, 255, 0), (150, 150, 150))
        self.demolish_position = self.demolish_button.get_rect().move(0, 150)
        surface.blit(self.demolish_button, self.demolish_position)

    def handle_click(self, mouseX, mouseY, player):
        if self.demolish_position.collidepoint(mouseX, mouseY):
            if self.building.owner.num == player.num:
                    return EmptySquare(self.building.x, self.building.y, self.building.index, player)
        return None

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
        self.QoL = 30
        self.oldQoL = 30
        self.minQoL = 0
        self.maxQoL = 100
        self.QoLBonus = 0
        self.fee = False

    def produce(self):
        money = self.profits * self.QoL / 100
        return (self.owner, money)

    def draw(self, surface):
        """Draw the square contents (shared by all buildings)"""
        surface.blit(self.image, self.rect)

    def get_menu(self):
        """Get menu object referencing this square (self)"""
        pass
    def getOldQoL(self):
        return self.oldQoL

   # call this in the map class updateQoL function
    def updateQoL(self, newQoL):
        self.oldQoL = self.QoL
        self.QoL = (newQoL + self.QoL + self.QoLBonus) / 2
        if self.QoL > self.maxQoL:
            self.QoL = self.maxQoL
        if self.QoL < self.minQoL:
            self.QoL = self.minQoL


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

        self.QoL = 50
        self.oldQoL = 50
        self.QoLBonus = 5
        self.maxQoL = 100
        self.image = assets.get_image("empty")
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.maxQoL = 25

    def get_menu(self):
        return BuildMenu(self)


class Restaurant(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 15)

        self.image = assets.get_image("restaurant" + str(self.owner.num))
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 50
        self.QoLBonus = 20
        self.oldQoL = 50
        self.profits = 100
        self.maxQoL = 100

    def get_menu(self):
        return OwnedMenu(self)


# The Public Park is a great addition to any city. It will help raise QoL significantly, but instead of producing money, it costs money to maintain. Thanks to maintainance, it can never be below 50 QoL.
class PublicPark(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 15)

        self.fee = True
        self.image = assets.get_image("park" + str(self.owner.num))
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 100
        self.QoLBonus = 60
        self.oldQoL = 100
        self.profits = -50
        self.minQoL = 50
        self.maxQoL = 200

    def get_menu(self):
        return OwnedMenu(self)

# Blight is a costly way to make life worse for everyone. It can only have negative QoL, which means its "profits" will actually cost its owner money.
class Blight(_BaseSquare):
    def __init__(self, x, y, index, owner):
        # Call parent constructor
        _BaseSquare.__init__(self, x, y, index, owner, 15)

        self.fee - True
        self.image = assets.get_image("blight" + str(self.owner.num))
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 0
        self.QoLBonus = -100
        self.oldQoL = -100
        self.profits = 150
        self.maxQoL = 0
        self.QoLBonus = -100
        self.minQoL = -100

    def get_menu(self):
        return OwnedMenu(self)


class Factory(_BaseSquare):
    def __init__(self, x, y, index, owner):
        _BaseSquare.__init__(self, x, y, index, owner, 300)

        self.image = assets.get_image("factory" + str(self.owner.num))
        self.image = pygame.transform.scale(self.image, (config.SQUARE_SIZE, config.SQUARE_SIZE))
        self.rect = self.image.get_rect().move((x, y))
        self.QoL = 0
        self.oldQoL = 0
        self.QoLBonus = -20
        self.profits = 400
        self.maxQoL = 100
    
    def get_menu(self):
        return OwnedMenu(self)
