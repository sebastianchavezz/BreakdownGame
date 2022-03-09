



class Ball:
    WIDTH: int
    HEIGHT : int
    snelheid :int = -7
    richting_x : int = snelheid
    richting_y : int  = snelheid
    radius :int = 15

    def __init__(self,width:int,height:int):
        self.WIDTH = width
        self.HEIGHT = height
        self.x = self.WIDTH//2
        self.y = self.HEIGHT//2
        
    
    def update_ball(self):
        self.x += self.richting_x
        self.y += self.richting_y
        self.check_collision_x()
        self.check_collision_y()
        self.ball_off_screen()
    def check_collision_x(self):
        '''checks collition against the vertical walls'''
        if self.x +self.radius >= self.WIDTH or self.x - self.radius <= 0:
            self.change_richting_x()

    def check_collision_y(self):
        '''checks if ball collies against the walls or the players pallet'''
        if self.y - self.radius <=0 :
            self.change_richting_y()

    def change_richting_x(self):
        self.richting_x = self.richting_x *-1

    def change_richting_y(self):
        self.richting_y = self.richting_y *-1   

    def ball_off_screen(self):
        if self.y > self.HEIGHT:
            self.x = self.WIDTH//2
            self.y = self.HEIGHT//2