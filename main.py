
from BreakOutGame.Game import Game
import pygame as pg
def main():
    MAX_FPS = 60
    WIDTH = 700
    HEIGHT = 1000
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    screen.fill(pg.Color('black'))
    game = Game(screen,WIDTH,HEIGHT)
    clock = pg.time.Clock()
    run = True
    while run:
        run = game.is_ball_in_Game()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run= False
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] :
            game.move_pallet(left=True)
        if keys[pg.K_RIGHT]:
            game.move_pallet(left=False)

        game.update_screen()
        clock.tick(MAX_FPS)
        pg.display.flip()


if __name__ == '__main__':
    main()