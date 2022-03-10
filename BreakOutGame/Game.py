import pygame as pg
from .model.gameState import GameState
from .view.view import View
from .model.player import Player
from .model.ball import Ball
pg.init()

class GameData:
    pass

class Game:
    _widthBlock = 50
    _heightBlock = 30
    
    def __init__(self,window,window_width,window_height):
        self.screen = window
        self.WIDTH = window_width
        self.HEIGHT = window_height
        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.view = View(self.WIDTH,self.HEIGHT,self._widthBlock,self._heightBlock)
        self.game_rectangles = GameState(self._heightBlock,self._widthBlock,self.WIDTH,self.HEIGHT)
        self.player = Player(self.WIDTH,self.HEIGHT,self._widthBlock)
        self.ball = Ball(self.WIDTH,self.HEIGHT,self.screen)

        self.running =True


    
    def move_pallet(self,left:bool):
        '''True moving left, False moving right'''
        if left:
            self.player.moving_left = True
            self.view.undraw(self.screen,self.player.paddle)
            self.player.move_left()
            return
        
        self.player.moving_right = True
        self.view.undraw(self.screen,self.player.paddle)
        self.player.move_right()
        

    def update_screen(self):
        self.view.undraw(self.screen,self.ball.rect)
        self.ball.update_ball()
        self.player.check_collision_ball(self.ball)
        self.view.draw_game_state(screen=self.screen,rectangles=self.game_rectangles.rects,undrawed=self.game_rectangles.undrawed_rects)
        self.view.draw(screen=self.screen,pallet=self.player.paddle)
        self.view.draw(self.screen,self.ball.rect)
        #update gamestate logic and collition
        
        if (self.ball.rect.y < self.game_rectangles.height_of_all_blocks + 20):
            self.game_rectangles.clear_undraw()
            self.game_rectangles.check_collition_with_ball(self.ball) 
            if self.game_rectangles.ball_acceralor %9==0:
                self.ball.accelerate_ball()
                self.player.moving_distance += 0.5
                self.game_rectangles.ball_acceralor = 1


    
        self.player.moving_left = False
        self.player.moving_right = False


    def is_ball_in_Game(self)->bool:
        return self.ball.ball_in_game