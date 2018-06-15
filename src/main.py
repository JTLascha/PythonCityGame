import pygame
from pygame.locals import *

from . import assets, board, config

def main():
    pygame.init()

    screen = pygame.display.set_mode((config.WINDOW_SIZE, config.WINDOW_SIZE), HWSURFACE | DOUBLEBUF)
    pygame.display.set_caption("Python Board Game!")

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
                # TODO: Process mouse click
                pass
            elif event.type == KEYDOWN:
                if event.key == K_f:
                    draw_fps = not draw_fps

                elif event.key == K_ESCAPE:
                    running = False

                elif event.key == K_g:
                    screen = pygame.display.set_mode((config.WINDOW_SIZE, config.WINDOW_SIZE), FULLSCREEN | HWSURFACE | DOUBLEBUF)
    
        # Draw all objects to the screen
        game_board.draw(screen)

        if curr_menu is not None:
            curr_menu.draw(screen)

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



