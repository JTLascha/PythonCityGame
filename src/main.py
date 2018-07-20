import pygame
from pygame.locals import *

from . import assets, board, config, level, menus, person, squares

class Player:
    def __init__(self, num, start_money):
        self.num = num
        self.money = start_money

def main():
    pygame.init()

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), HWSURFACE | DOUBLEBUF)
    pygame.display.set_caption("Python Board Game!")

    # Setup map and menu surfaces
    map_surface = pygame.Surface((config.MAP_WIDTH, config.MAP_HEIGHT))
    menu_surface = pygame.Surface((config.MENU_WIDTH, config.MENU_HEIGHT))

    # Load images and music
    assets.load_images("assets/")
    assets.load_music("assets/")

    # Load our main fonts for text
    font = pygame.font.Font(None, 20)
    font_medium = pygame.font.Font(None, 32)

    # Create and setup game board
    game_board = level.get_level_board("levels/", "level1.lvl")

    num_players = 2
    players = []
    if num_players == 2:
        players.append(Player(0, 500))
        players.append(Player(1, 500))
        game_board.replace_square(0, squares.EmptySquare, players[0])
        game_board.replace_square(len(game_board.board_squares) - 1, squares.EmptySquare, players[1])
        # game_board.board_squares[0] = squares.EmptySquare(game_board.board_squares[0].x, game_board.board_squares[0].y, 0, players[0])
        # game_board.board_squares[-1] = squares.EmptySquare(game_board.board_squares[-1].x, game_board.board_squares[-1].y, game_board.board_squares[-1].index, players[1])

    # Create main clock for constant FPS
    main_clock = pygame.time.Clock()
    draw_fps = True
    
    # Store menu/option screen to draw above the board
    curr_menu = None
    
    curr_player = 0

    # Main game loop
    running = True
    while running:

        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Handle click events
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < config.MAP_WIDTH:
                    click_index = game_board.get_click_index(*pygame.mouse.get_pos())
                    if click_index is not None:
                        curr_menu = game_board.get_menu(click_index)
                    else:
                        curr_menu = None
                else:
                    if curr_menu:
                        new_building = curr_menu.handle_click(pygame.mouse.get_pos()[0] - config.MAP_WIDTH, pygame.mouse.get_pos()[1], players[curr_player])
                        if new_building:
                            game_board.board_squares[new_building.index] = new_building
                            curr_menu = None
            
            # Handle keyboard events
            elif event.type == KEYDOWN:
                if event.key == K_f:
                    draw_fps = not draw_fps

                elif event.key == K_ESCAPE:
                    running = False

                elif event.key == K_g:
                    if screen.get_flags() & FULLSCREEN:
                        pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
                    else:
                        pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), FULLSCREEN | HWSURFACE | DOUBLEBUF)

                elif event.key == K_RETURN:
                    if curr_player == num_players - 1:
                        # process round end, calculate new turn order
                        curr_player = 0
                    else:
                        curr_player += 1

    
        # Draw all objects to the surfaces
        map_surface.fill((0, 0, 0))
        menu_surface.fill((0, 0, 0))
        screen.fill((0, 0, 0))

        game_board.draw(map_surface)

        # Highlit squares if hovered over
        if pygame.mouse.get_focused():
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX < config.MAP_HEIGHT:
                game_board.draw_outline(map_surface, mouseX, mouseY)

        menu_surface.fill((0, 0, 0))
        if curr_menu is not None:
            curr_menu.draw(menu_surface)
        else:
            # Draw stats menu (when there is no menu selected)
            pass

        # Draw both the map and menu to the screen
        screen.blit(map_surface, (0, 0))
        screen.blit(menu_surface, (config.MAP_WIDTH, 0))

        if draw_fps:
            fps_text = font.render(str(int(main_clock.get_fps())), 1, (0, 0, 0), (255, 255,255))
            fps_position = fps_text.get_rect()
            screen.blit(fps_text, fps_position)

        # Draw money of current player
        money_text = font_medium.render("Money: $" + str(players[curr_player].money), 1, (0, 0, 0))
        money_position = money_text.get_rect().move(50, 0)
        screen.blit(money_text, money_position)

        # Draw player number
        player_text = font_medium.render("Player: #" + str(curr_player), 1, (0, 0, 0))
        player_position = player_text.get_rect().move(400, 0)
        screen.blit(player_text, player_position)
        
        pygame.display.flip()

        # We want a fixed FPS
        main_clock.tick(config.FRAME_RATE)

    pygame.quit()

    print("")
    return



