
import pygame as pg



class Ball:
    WIDTH: int
    HEIGHT : int
    original_speed_y :float = -2.5
    original_speed_x: float= -1.5
    richting_x : float = original_speed_x
    richting_y : float  = original_speed_y
    radius :int = 20
    is_in_boost = False
    boost :int = 2
    threshold :int =2
    ball_in_game: bool= True

    def __init__(self,width:int,height:int,screen):
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
        
        self.ball_off_screen()
        
    def check_collision_x(self):
        '''checks collition against the vertical walls'''
        if self.rect.right>= self.WIDTH:
            self.rect.x = self.WIDTH-self.radius-self.threshold
            self.change_richting_x()
            if self.is_in_boost :
                self.undo_boost()
                print(f'before: {self.is_in_boost}')
                self.is_in_boost= False
                print(f'after: {self.is_in_boost}')
            print(self.richting_x) 
        if self.rect.left  <= 0:
            self.rect.x = self.threshold 
            self.change_richting_x()
            if self.is_in_boost :
                self.undo_boost()
                print(f'before: {self.is_in_boost}')
                self.is_in_boost= False
                print(f'after: {self.is_in_boost}') 
               
            print(self.richting_x) 
    def check_collision_y(self):
        '''checks if ball collies against the walls or the players pallet'''
        if self.rect.top <=0 :
            self.rect.y =self.threshold
            self.change_richting_y()

    def change_richting_x(self):
        self.richting_x = self.richting_x *-1

    def change_richting_y(self):
        self.richting_y = self.richting_y *-1   

    def ball_off_screen(self):
        if self.rect.y > self.HEIGHT:
            self.ball_in_game =False
            

    def undo_boost(self):
        if self.richting_x>0:
            self.richting_x = -self.original_speed_x
        else:
            self.richting_x = self.original_speed_x
        
    
    
    def accelerate_ball(self):
        accelarate = 0.5
        self.accelerate_ball_x(accelarate)
        self.accelerate_ball_y(accelarate)
        
    def accelerate_ball_y(self,a):
        self.original_speed_y -=a
        if self.richting_y>0:
            self.richting_y += a
        else:
            self.richting_y -= a

    def accelerate_ball_x(self,a):
        self.original_speed_x -=a
        if self.richting_x>0:
            self.richting_x += a
        else:
            self.richting_x -= a

    def ball_boost(self):
        print('BOOOST')
        
        self.is_in_boost = True
        if self.richting_x>0:
            self.richting_x += self.boost
        else:
            self.richting_x -= self.boost
        print(self.richting_x)

   