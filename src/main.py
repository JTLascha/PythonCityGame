import random

import pygame
from pygame.locals import *

from . import assets, board, config, level, squares

class Player:
    def __init__(self, num, start_money):
        self.num = num
        self.money = start_money + (num * 100) # bonus money given out based on player number


def getNextPlayer(playerList,gameBoard):
    p = playerList
    b = gameBoard
    turn = 0
    truTurn = 0
    while True:
        b.updateQoL() # update the QoL in each square every turn
        truTurn = (truTurn+ 1)%3
        if truTurn == 2:
            prof = b.genProfit()
            p[0].money += prof[0]
            p[1].money += prof[1]
        if p[0].money < 0:
            p[0].money = 0
        if p[1].money < 0:
            p[1].money = 0
            if p[0].money >= 6000 or p[1].money >= 6000:
                if p[0].money != p[1].money:
                    yield -1
            
            if p[0].money <= p[1].money:
                turn = 0
            else:
                turn = 1
            truTurn = 0
        else:
            if turn == 0:
                turn = 1
            else:
                turn = 0
        yield turn

def main():
    pygame.init()

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), HWSURFACE | DOUBLEBUF)
    pygame.display.set_caption("Python Board Game!")

    # Setup map and menu surfaces
    map_surface = pygame.Surface((config.MAP_WIDTH, config.MAP_HEIGHT))
    menu_surface = pygame.Surface((config.MENU_WIDTH, config.MENU_HEIGHT))

    # Load images and music
    assets.load_images("assets/")
    music = assets.load_music("assets/")

    # Setup music player
    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(random.choice(music))
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()

    mute = False

    # Load our main fonts for text
    font = pygame.font.Font(None, 20)
    font_medium = pygame.font.Font(None, 32)

    # Create and setup game board
    game_board = level.get_level_board("levels/", "level1.lvl")

    num_players = 2
    winner = -1
    players = []
    if num_players == 2:
        players.append(Player(0, 500))
        players.append(Player(1, 500))
        game_board.replace_square(0, squares.EmptySquare, players[0])
        game_board.replace_square(len(game_board.board_squares) - 1, squares.EmptySquare, players[1])
        # game_board.board_squares[0] = squares.EmptySquare(game_board.board_squares[0].x, game_board.board_squares[0].y, 0, players[0])
        # game_board.board_squares[-1] = squares.EmptySquare(game_board.board_squares[-1].x, game_board.board_squares[-1].y, game_board.board_squares[-1].index, players[1])
    getNextTurn = getNextPlayer(players,game_board)
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
                    curr_player = next(getNextTurn)
                    if curr_player == -1:
                        if players[0].money < players[1].money:
                            winner = 1
                            curr_player = 1
                        else:
                            winner = 0
                            curr_player = 0

                elif event.key == K_m:
                    mute = not mute
                    if mute:
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(0.8)

                elif event.key == K_h:
                    curr_menu = squares.HelpMenu()

            # Handle song ending
            elif event.type == SONG_END:
                pygame.mixer.music.load(random.choice(music))
                pygame.mixer.music.play()
    
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
        player_text = font_medium.render("Player: #" + str(curr_player + 1), 1, (0, 0, 0))	#prints curr_player + 1 so players don't have to deal with null indexing
        player_position = player_text.get_rect().move(200, 0)
        screen.blit(player_text, player_position)

         # Draw help text
        help_text = font_medium.render("Press h for help", 1, (0, 0, 0))
        help_position = help_text.get_rect().move(400, 0)
        screen.blit(help_text, help_position)       

        pygame.display.flip()

         # We want a fixed FPS
        main_clock.tick(config.FRAME_RATE)
        if winner != -1:
            running = False
            running2 = True
            while running2:
                map_surface.fill((0, 0, 0))
                menu_surface.fill((0, 0, 0))
                screen.fill((0, 0, 0))
                player_text = font_medium.render("Player: #" + str(curr_player + 1) +" has won!", 1, (50,205,50))
                player_position = player_text.get_rect().move(config.WINDOW_WIDTH/2 - 50, config.WINDOW_HEIGHT/2)
                screen.blit(player_text, player_position)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running2 = False

    pygame.quit()

    print("")
    return



