import arcade

class Timer(arcade.Window):
    def __init__(self,Window_Width=300,Window_Height=150):
        super().__init__(Window_Width,Window_Height)
        self.time=0.0
        
    def init(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.time=0.0
        
    def on_draw(self):
        arcade.start_render()  
        calc_min=int(self.time)//60 
        calc_sec=int(self.time)%60
        result_time=f"Time : {calc_min} : {calc_sec}"
        arcade.draw_text(result_time,60,60,arcade.color.RED,25)
        
        
    def update(self,new_time):
        self.time +=new_time
        
        
if __name__=="__main__":
    obj1=Timer()
    obj1.init()
    arcade.run()
             