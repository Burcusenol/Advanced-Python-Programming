import arcade

#Setting size for main winows
WINDOW_WITH=700
WINDOW_HEIGHT=700


#creating and opening the window
arcade.open_window(WINDOW_WITH,WINDOW_HEIGHT,"SAD FACE")

#setting background color
arcade.set_background_color(arcade.color.ALICE_BLUE)

#starting the render
arcade.start_render()

#Drawing starts from here


#draw te outline of face
x=350
y=350
radius=200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

#drawing the right eye
x=420
y=420
radius=25
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

#drawing the left eye
x=280
y=420
radius=25
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

#drawing the sad smile
x=340
y=240
width=220
height=80
starting_angle=0
end_angle=180
arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,starting_angle,end_angle,20)

#drawing the happy smile
# x=340
# y=310
# width=120
# height=100
# starting_angle=180
# end_angle=360
# arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,starting_angle,end_angle,10)

#finishing the render
arcade.finish_render()

#runing the code
arcade.run()