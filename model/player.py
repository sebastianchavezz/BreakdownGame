




class Player:

    WIDTH: int
    HEIGHT:int
    x : int 
    y : int
    moving_distance: int = 20

    def __init__(self,width:int,height:int,lenght_pallet:int,pallet_height:int):
        self.WIDTH = width
        self.HEIGHT = height
        self.x = self.WIDTH //2
        self.y = self.HEIGHT-100
        self.lenght_pallet = lenght_pallet
        self.pallet_thickness = 5
        self.topX = self.x + self.lenght_pallet
        self.topY = self.y + self.pallet_thickness
    def move_left(self)->None:
        '''changes the data'''
        if(self.check_collision_wall_left()): 
            return
        self.x -= self.moving_distance
        
    def move_right(self)->None:
        '''changes the data'''
        if(self.check_collision_wall_right()):
            return
        self.x += self.moving_distance

    def check_collision_wall_right(self)->bool:
        if self.x >= self.WIDTH-self.lenght_pallet:
            return True
    
    def check_collision_wall_left(self)->bool:
        if self.x <= 0:
            return True

    def check_collision_ball(self,ball:object):
        #self.check_collision_sides_of_paddle(ball)
        self.check_collision_top_of_paddle(ball)
   

    def check_collision_top_of_paddle(self,ball):
        if self.x<ball.x <=self.x+self.lenght_pallet and ball.y + ball.radius - self.y ==0:
            ball.change_richting_y()
    
    def check_collision_sides_of_paddle(self,ball):
        self.check_left(ball)
        self.check_right(ball)

    def check_left(self,ball):
        if (self.y<= ball.y <= self.topY )and (ball.x + ball.radius - self.x >=0):
            ball.change_richting_x()
            

    def check_right(self,ball):
        if (self.y<= ball.y <=self.topY) and (ball.x-ball.radius-self.topX <=2):
            ball.change_richting_x()
            