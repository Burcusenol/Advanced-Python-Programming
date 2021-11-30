import arcade
import math

Window_width=900
Window_height=700

axis_x=Window_width //2
axis_y=Window_height//2

radians_per_tick=0.01
radar_needle_length=300

def on_draw(new_time):
    on_draw.angle +=radians_per_tick
    
    x=radar_needle_length * math.sin(on_draw.angle) + axis_x
    y=radar_needle_length * math.cos(on_draw.angle) + axis_y
    
    arcade.start_render()
    arcade.draw_line(axis_x,axis_y,x,y,arcade.color.RED,5)
    
    arcade.draw_circle_outline(axis_x,axis_y,radar_needle_length,arcade.color.DARK_BLUE,10)
    
on_draw.angle=0
    
    
    
if __name__=="__main__":
    arcade.open_window(Window_width,Window_height,"RADAR SYSTEM")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw,1/100)
    arcade.run()
        