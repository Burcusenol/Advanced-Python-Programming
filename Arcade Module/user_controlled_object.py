import arcade

#set values for the window

WINDOW_WIDTH=800
WINDOW_HEIGHT=600

#set values for the regtangle

RECTANGLE_WIDTH=50
RECTANGLE_HEIGHT=50

#set the value for the rectangle/object speed
OBJECT_SPEED=5


class Rectangle:
    def __init__(self,x,y,rect_width,rect_height,angle,color):
      
        #position
        self.x=x
        self.y=y
        
        #vector
        self.new_x=0
        self.new_y=0
        
        #rotation
        self.angle=angle
        
        #size
        self.rect_width=rect_width
        self.rect_height=rect_height
        
        #color
        self.color=color
        
    def draw(self):
        #draw our rectangle
        arcade.draw_rectangle_filled(self.x,self.y,self.rect_width,
                                     self.rect_height,self.color,self.angle)
    
    
    def move(self):
        #move our rectangle
        self.x +=self.new_x    
        
        if self.x < RECTANGLE_WIDTH // 2:
            self.x = RECTANGLE_WIDTH //2
        
        if self.x > WINDOW_WIDTH - (RECTANGLE_WIDTH // 2):
            self.x = WINDOW_WIDTH - (RECTANGLE_WIDTH //2)
            
        self.y +=self.new_y
        
        if self.y < RECTANGLE_HEIGHT//2:
            self.y=RECTANGLE_HEIGHT //2
              
        if self.y > WINDOW_HEIGHT - (RECTANGLE_HEIGHT // 2):
            self.y = WINDOW_HEIGHT - (RECTANGLE_HEIGHT //2)
            
            
class Game(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height,title="A USER CONROLLED MOVING RECTANGLE ")
        
    def setup(self):
        x=WINDOW_WIDTH // 2
        y=WINDOW_HEIGHT // 2
        self.player=Rectangle(x,y,RECTANGLE_WIDTH,RECTANGLE_HEIGHT,
                              angle=0,color=arcade.color.RED)
        
        
    def update(self, dt):
        #move each and everything
        self.player.move()
        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        
    def on_key_press(self,key,modifiers):
        if key==arcade.key.UP:
            self.player.new_y=OBJECT_SPEED
        elif key==arcade.key.DOWN:
            self.player.new_y=-OBJECT_SPEED
        elif key==arcade.key.LEFT:
            self.player.new_x=-OBJECT_SPEED
        elif key==arcade.key.RIGHT:
            self.player.new_x=OBJECT_SPEED
            
    def on_key_release(self,key,modifiers):
        if key==arcade.key.UP or key ==arcade.key.DOWN:
            self.player.new_y=0
        elif key ==arcade.key.LEFT or key==arcade.key.RIGHT:
            self.player.new_x=0
            
            
if __name__=="__main__":
    obj1=Game(WINDOW_WIDTH,WINDOW_HEIGHT)
    obj1.setup()
    arcade.run() 
                
                