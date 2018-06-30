import pygame
from pygame.locals import *

from . import assets, board, config, menus, person

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

    # Load our main font for text
    font = pygame.font.Font(None, 20)

    # Create and setup game board
    game_board = board.Board(num_players=2)

    # Create main clock for constant FPS
    main_clock = pygame.time.Clock()
    draw_fps = True
    
    # Store menu/option screen to draw above the board
    curr_menu = None
    
    # Main game loop
    running = True
    while running:

        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                click_index = game_board.get_click_index(*pygame.mouse.get_pos())
                if click_index is not None:
                    curr_menu = game_board.get_menu(click_index)
                else:
                    curr_menu = None
                
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
    
        # Draw all objects to the screen
        map_surface.fill((0, 0, 0))
        menu_surface.fill((0, 0, 0))
        screen.fill((0, 0, 0))

        game_board.draw(map_surface)

        if pygame.mouse.get_focused():
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX < config.MAP_HEIGHT:
                game_board.draw_outline(map_surface, mouseX, mouseY)

        menu_surface.fill((0, 0, 0))
        if curr_menu is not None:
            curr_menu.draw(menu_surface)

        screen.blit(map_surface, (0, 0))
        screen.blit(menu_surface, (config.MAP_WIDTH, 0))

        if draw_fps:
            fps_text = font.render(str(int(main_clock.get_fps())), 1, (0, 0, 0), (255, 255,255))
            fps_position = fps_text.get_rect()
            screen.blit(fps_text, fps_position)
        
        pygame.display.flip()

        # We want a fixed FPS
        main_clock.tick(config.FRAME_RATE)

    pygame.quit()

    print("")
    return



