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


game_rectangles = GameState(_heightBlock,_widthBlock,WIDTH,HEIGHT)


def main():
    
    
    pg.init()
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    player = Player(WIDTH,HEIGHT,_widthBlock)
    ball = Ball(WIDTH,HEIGHT,screen)
    clock = pg.time.Clock()
    screen.fill(pg.Color('black'))
    running = True
    
    while running:
        player.moving_left = False
        player.moving_right = False
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] :
            view.undraw(screen=screen,pallet=player.paddle)
            player.moving_left = True
            player.move_left()
        if keys[pg.K_RIGHT]:
            view.undraw(screen=screen,pallet=player.paddle)
            player.move_right()
            player.moving_right= True
                
        
        #updating the ball, first undraw the ball then draw it again in an other position
        view.undraw(screen,ball.rect)
        ball.update_ball()
        player.check_collision_ball(ball)
        #update gamestate logic and collition
        
        if (ball.rect.y < game_rectangles.height_of_all_blocks + 20):
            game_rectangles.check_collition_with_ball(ball) 
            if game_rectangles.ball_acceralor %8==0:
                ball.accelerate_ball()
                player.moving_distance += 1
                game_rectangles.ball_acceralor = 1

        #draw player
        
        
        view.draw_game_state(screen=screen,rectangles=game_rectangles.rects,undrawed=game_rectangles.undrawed_rects)
        view.draw(screen=screen,pallet=player.paddle)
        view.draw(screen,ball.rect)
        clock.tick(60)
        pg.display.flip()




if __name__ == '__main__':
    main()


