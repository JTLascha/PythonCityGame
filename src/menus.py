class _Menu:
    """Base menu object"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pass

class BuyMenu(_Menu):
    def __init__(self, x, y):
        _Menu.__init__(x, y)

    def draw(self, surface):
        pass
