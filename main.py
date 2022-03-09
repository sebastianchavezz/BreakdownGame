import pygame as pg
from model.gameState import GameState
from view.view import View
from model.player import Player
from model.ball import Ball

MAX_FPS = 25
WIDTH = 700
HEIGHT = 1000
_widthBlock = 50
_heightBlock = 30
view = View(WIDTH,HEIGHT,_widthBlock,_heightBlock)
player = Player(WIDTH,HEIGHT,_widthBlock,_heightBlock)
ball = Ball(WIDTH,HEIGHT)
game_rectangles = GameState(_heightBlock,_widthBlock,WIDTH,HEIGHT)


def main():
    
    
    pg.init()
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color('black'))
    running = True

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                view.undraw_player(screen=screen,x=player.x,y=player.y,pallet_thicness=player.pallet_thickness)
                player.move_left()
            if keys[pg.K_RIGHT]:
                view.undraw_player(screen=screen,x=player.x,y=player.y,pallet_thicness=player.pallet_thickness)
                player.move_right()

                    
        
        #updating the ball, first undraw the ball then draw it again in an other position
        view.undraw_ball(screen,ball.x,ball.y,ball.radius)
        
        player.check_collision_ball(ball)
        #update gamestate logic and collition
        
        if (ball.y < game_rectangles.height_of_all_blocks + 20):
            game_rectangles.check_collition_with_ball(ball) 

        #draw player
        view.draw_player(screen=screen,x=player.x,y=player.y,pallet_thicness=player.pallet_thickness)
        
        ball.update_ball()
        view.draw_game_state(screen=screen,rectangles=game_rectangles.rects,undrawed=game_rectangles.undrawed_rects)
        view.draw_ball(screen,ball.x,ball.y,ball.radius)
        
        
        clock.tick(MAX_FPS)
        pg.display.flip()




if __name__ == '__main__':
    main()


