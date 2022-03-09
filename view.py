import pygame as pg 


class View:
    _widthBlock: int 
    _heightBlock: int 

    def __init__(self,width_screen:int,height_screen:int,widthBlock:int,heightBlock:int):
        self.WIDTH = width_screen
        self.HEIGHT = height_screen
        self._widthBlock = widthBlock
        self._heightBlock = heightBlock
    
    def draw_game_state(self,screen:pg.Surface,rectangles:list,undrawed:list):
        """draw the gamestate, wich are the blocks that need to be broken"""
        undraw_color = (0,0,0)
        drawed_color = (255,0,0)
        self.update_game_state(screen,undrawed,undraw_color)
        self.update_game_state(screen,rectangles,drawed_color)

    def update_game_state(self,screen:pg.Surface,rectangles:list,color:tuple):
        """undraw the gamestate, wich are the blocks that need to be broken"""
        color_change = 7
        for rec in rectangles:
            pg.draw.rect(surface=screen,color=color,rect=pg.Rect(rec.x, rec.y, self._widthBlock,self._heightBlock))
        color_change+= 1 

    def undraw_ball(self,screen:pg.Surface,x:int,y:int,radius:int)->None:
        '''update the ball'''
        color = (0,0,0)
        pg.draw.circle(screen, color, (x, y), radius, 2)

    def draw_ball(self,screen:pg.Surface,x:int,y:int,radius:int)->None:
        '''draw the ball'''
        color = (255,255,255)
        pg.draw.circle(screen, color, (x, y), radius, 2)

    def undraw_player(self,screen:pg.Surface,x:int,y:int,pallet_thicness:int)->None:
        '''first undraw the person'''
        color = (0,0,0)
        pg.draw.rect(surface=screen,color=color,rect=pg.Rect(x,y,self._widthBlock,pallet_thicness))


    def draw_player(self,screen:pg.Surface,x:int,y:int,pallet_thicness:int)->None:
        '''draw the person with new coordinates'''
        color = (255,0,0)
        pg.draw.rect(surface=screen,color=color,rect=pg.Rect(x,y,self._widthBlock,pallet_thicness))