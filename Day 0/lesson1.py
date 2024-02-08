from turtle import * 

#we want to paint a house


#step 1: draw a square
width(7)
speed(15)

color("yellow")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof

#drawing windows

pendown()
color("yellow")
goto(200,200)
forward(50)

color("sky blue")
begin_fill()

right(60)
forward(30)
left(90)

forward(40)
left(90)

forward(30)
left(90)

forward(40)
left(90)
forward(35)

end_fill()

color("yellow")
forward(100)
color("sky blue")
begin_fill()
forward(30)
left(90)

forward(40)
left(90)

forward(30)
left(90)

forward(40)
end_fill()




exitonclick()