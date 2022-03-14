
import pygame as pg
import random



class Ball:
    WIDTH: int
    HEIGHT : int
    
    radius :int = 20
    is_in_boost = False
    boost :int = 2
    threshold :int =2
    ball_in_game: bool= True

    def __init__(self,width:int,height:int,screen):
        self.random_richting_y = 1 if random.random() < 0.5 else -1
        self.original_speed_y :float = self.random_richting_y* 2.5
        self.random_richting_x = 1 if random.random() < 0.5 else -1
        self.original_speed_x: float= self.random_richting_x * 1.5
        self.richting_x : float = self.original_speed_x
        self.richting_y : float  = self.original_speed_y
        self.WIDTH = width
        self.HEIGHT = height
        self.x_begin = self.WIDTH//2
        self.y_begin = self.HEIGHT//2
        self.screen = screen
        self.rect =pg.Rect(self.x_begin,self.y_begin,self.radius,self.radius)
    
    def update_ball(self):
        '''updates the ball'''

        self.check_collision_x()
        self.check_collision_y()
        self.rect.x += self.richting_x
        self.rect.y += self.richting_y
        self.check_if_zero()
        self.ball_off_screen()
        
    def check_collision_x(self):
        '''checks collition against the vertical walls'''
        if self.rect.right>= self.WIDTH:
            self.rect.x = self.WIDTH-self.radius-self.threshold
            self.change_richting_x()
            if self.is_in_boost :
                self.undo_boost()
                
                self.is_in_boost= False
                
            print(self.richting_x) 
        if self.rect.left  <= 0:
            self.rect.x = self.threshold 
            self.change_richting_x()
            if self.is_in_boost :
                self.undo_boost()
                
                self.is_in_boost= False
            print(self.richting_x) 
    
    def check_collision_y(self):
        '''checks if ball collies against the walls or the players pallet'''
        if self.rect.top <=0 :
            self.rect.y =self.threshold
            self.change_richting_y()

    def change_richting_x(self):
        self.richting_x = self.richting_x *-1
        print(self.richting_x)

    def change_richting_y(self):
        self.richting_y = self.richting_y *-1   

    def ball_off_screen(self):
        if self.rect.y > self.HEIGHT:
            self.ball_in_game =False
            

    def undo_boost(self):
        if self.richting_x>=0:
            self.richting_x = abs(self.original_speed_x)
        else:
            self.richting_x = abs(self.original_speed_x)*-1
        
    
    
    def accelerate_ball(self):
        
        accelarate = 0.5
        self.accelerate_ball_x(accelarate)
        self.accelerate_ball_y(accelarate)
        
    def accelerate_ball_y(self,a):
        self.original_speed_y = self.random_richting_y*(abs(self.original_speed_y)+a)
        if self.richting_y>=0:
            self.richting_y = abs(self.original_speed_y)
        else:
            self.richting_y = abs(self.original_speed_y)*-1

    def accelerate_ball_x(self,a):
        self.original_speed_x = self.random_richting_x*(abs(self.original_speed_x)+a)
        if self.richting_x>=0:
            self.richting_x = abs(self.original_speed_x)
        else:
            self.richting_x = abs(self.original_speed_x)*-1

    def ball_boost(self):
        
        
        self.is_in_boost = True
        if self.richting_x>=0:
            self.richting_x += self.boost
        else:
            self.richting_x -= self.boost
        

    def check_if_zero(self):
        if self.richting_x ==0.0 or self.richting_x==-0.0 :
            
            self.undo_boost()
