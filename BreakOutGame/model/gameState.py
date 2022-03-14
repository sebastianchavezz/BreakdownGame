

from dataclasses import dataclass
import pygame as pg
class GameState:

    WIDTH: int
    HEIGHT : int
    begin_height :int =100
    height_blocks: int
    width_blocks: int
    rects : list
    undrawed_rects: list
    height_of_all_blocks : int 
    ball_acceralor: int =1
    rects_in_game = True

    
    def __init__(self,height_blocks:int,width_blocks:int,canvasWIDTH:int,canvasHEIGHT:int):
        self.height_blocks = height_blocks
        self.width_blocks = width_blocks
        self.WIDTH = canvasWIDTH
        self.HEIGHT = canvasHEIGHT
        self.height_of_all_blocks = self.height_blocks*8 +self.begin_height
        self.rects  = []
        self.undrawed_rects  = []
        print(self.height_blocks)
        self.add_rectangles()
        self.score :int =0
        self.collide : bool = False
    def add_rectangles(self):
        '''Add the data of all rectangles in a list of OBJECTS, easy to acces'''
        for y in range(self.begin_height,self.height_of_all_blocks,self.height_blocks):
            for x in range(0,self.WIDTH,self.width_blocks):
                self.rects.append(Rectangles(x,y,self.width_blocks,self.height_blocks))
                

    def check_collition_with_ball(self,ball):
        for indx in range(len(self.rects)-1,-1,-1):
            if self.rects[indx].collides_to_rectangles(ball):
                print(self.rects[indx])
                
                self.undrawed_rects.append(self.rects[indx])
                
                self.rects.remove(self.rects[indx])
                
                self.ball_acceralor +=1
                self.score +=1
                self.collide = True
                break
            
                
    def clear_undraw(self):
        self.undrawed_rects = []
    
    def check_game_done(self):
        if len(self.rects)==0:
            return False
        return True
            

@dataclass
class Rectangles:
    x: int
    y:int
    width_block:int
    height_block:int
    rect :pg.Rect
    def __init__(self,x:int,y:int,width_block:int,height_block:int):
        self.x = x
        self.y =y
        self.width_block = width_block
        self.height_block = height_block
        self.topX:int = self.x+self.width_block
        self.topY : int= self.y+self.height_block
        self.rect = pg.Rect(self.x,self.y,self.width_block,self.height_block)

    def collides_to_rectangles(self,ball)->bool:
        if self.collides_to_bottom(ball) or self.collides_to_top(ball)or self.collides_to_left(ball) or self.collides_to_right(ball):
            return True

    def collides_to_top(self,ball)->bool:
        if self.x <= ball.rect.x+ball.radius//2 < self.topX and self.y <= ball.rect.bottom + ball.threshold < self.topY:

            ball.change_richting_y()
            return True
    
    def collides_to_bottom(self,ball)->bool:
        if self.x <= ball.rect.x+ball.radius//2 < self.topX and self.y <= ball.rect.y - ball.threshold < self.topY:
            ball.change_richting_y()
            return True
    
    def collides_to_left(self,ball)->bool:
        if self.x <= ball.rect.x+ball.radius +ball.threshold< self.topX and self.y <= ball.rect.y +ball.radius//2 < self.topY:
            ball.change_richting_x()
            return True

    def collides_to_right(self,ball)->bool:
        if self.x <= ball.rect.x - ball.threshold< self.topX and self.y <= ball.rect.y + ball.radius//2 < self.topY:
            ball.change_richting_x()
            return True