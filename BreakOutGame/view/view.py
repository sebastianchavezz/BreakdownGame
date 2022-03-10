
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
        
        if len(rectangles) ==0:
            return
        for rec in rectangles:
            pg.draw.rect(surface=screen,color=color,rect=rec.rect)
        

    

    def undraw(self,screen:pg.Surface,pallet)->None:
        '''first undraw the person'''
        color = (0,0,0)
        pg.draw.rect(surface=screen,color=color,rect=pallet)


    def draw(self,screen:pg.Surface,pallet)->None:
        '''draw the person with new coordinates'''
        color = (255,0,0)
        pg.draw.rect(surface=screen,color=color,rect=pallet)
