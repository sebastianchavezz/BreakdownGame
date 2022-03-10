import pygame as pg
class Player:

    WIDTH: int
    HEIGHT:int
    
    moving_distance: float = 4.5
    pallet_thickness:int = 5
    moving_left : bool
    moving_right : bool

    def __init__(self,width:int,height:int,lenght_pallet:int):
        self.WIDTH = width
        self.HEIGHT = height
        self.x_begin = self.WIDTH //2
        self.y_begin = self.HEIGHT-100
        self.lenght_pallet = 70
        self.paddle = pg.Rect(self.x_begin,self.y_begin,self.lenght_pallet,self.pallet_thickness)
        
        self.topX = self.paddle.x + self.lenght_pallet
        self.topY = self.paddle.y + self.pallet_thickness

        
        
    def move_left(self)->None:
        '''changes the data'''
        if(self.check_collision_wall_left()): 
            return
        self.paddle.x -= self.moving_distance
        
    def move_right(self)->None:
        '''changes the data'''
        if(self.check_collision_wall_right()):
            return
        self.paddle.x += self.moving_distance

    def check_collision_wall_right(self)->bool:
        if self.paddle.x >= self.WIDTH-self.lenght_pallet:
            return True
    
    def check_collision_wall_left(self)->bool:
        if self.paddle.x <= 0:
            return True

    def check_collision_ball(self,ball:object):
        self.check_collision_top_of_paddle(ball)
   

    def check_collision_top_of_paddle(self,ball):
        if self.paddle.colliderect(ball.rect):
            ball.rect.y = self.paddle.y-ball.radius-ball.threshold
            if (ball.richting_x >0 and self.moving_left) or (ball.richting_x <0 and self.moving_right):
                ball.change_richting_x()
                ball.ball_boost()
            elif(ball.richting_x >0 and self.moving_right) or (ball.richting_x <0 and self.moving_left):
                ball.ball_boost()
            ball.change_richting_y()

    def get_paddle(self):
        return self.paddle