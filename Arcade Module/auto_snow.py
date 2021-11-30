import arcade
import random
import math


Window_Width=800
Window_Height=600

class Snow:
    def __init__(self):
        self.x=0
        self.y=0
        
    def reset_position(self):
        self.x=random.randrange(Window_Width)
        self.y=random.randrange(Window_Height,Window_Height+100)
        
class Game(arcade.Window):
    def __init__(self,screen_width,sceen_height):
        super().__init__(screen_width,sceen_height)
        self.snowflake_list=None
        
    def start_snowfall(self):
        self.snowflake_list=[]
        for i in range(100):
            snowflake=Snow()
            snowflake.x=random.randrange(Window_Width)
            snowflake.y=random.randrange(Window_Height+400)
        
        
            snowflake.size=random.randrange(2)
            snowflake.speed=random.randrange(20,100)
            snowflake.angle=random.uniform(math.pi,math.pi*2)
        
            self.snowflake_list.append(snowflake)
        
        arcade.set_background_color(arcade.color.BLACK)
        
    
    def on_draw(self):
        arcade.start_render()
        for snowflake in self.snowflake_list:
            arcade.draw_circle_filled(snowflake.x,snowflake.y,snowflake.size,arcade.color.WHITE)
            
            
    def update(self,new_time):
        for snowflake in self.snowflake_list:
            snowflake.y -=snowflake.speed * new_time
            if snowflake.y<0:
                snowflake.reset_position()
            
            snowflake.x +=snowflake.speed * math.cos(snowflake.angle) * new_time
            snowflake.angle += 1*new_time
            
            
            
if __name__=="__main__":
    obj1=Game(Window_Width,Window_Height)
    obj1.start_snowfall()
    arcade.run()