import colorgram
import turtle as t
import random

def config_turtle(turtle):
    turtle.speed(0)
    turtle.pensize(3)
    turtle.setheading(0)
    turtle.ht()

def get_random_color_from_image(image_colors):
    colorIndex = random.randint(0, len(image_colors) - 1)
    currentColor = image_colors[colorIndex]
    rgb = currentColor.rgb

    #white remover
    while(rgb.r >= 220 and rgb.g >= 220 and rgb.b >= 220):
        colorIndex = random.randint(0, len(image_colors) - 1)
        currentColor = image_colors[colorIndex]
        rgb = currentColor.rgb

    #black remover
    while(rgb.r <= 35 and rgb.g <= 35 and rgb.b <= 35):
        colorIndex = random.randint(0, len(image_colors) - 1)
        currentColor = image_colors[colorIndex]
        rgb = currentColor.rgb

    r = rgb.r
    g = rgb.g
    b = rgb.b
    # print(r, g, b) #DEGBUG
    return (r, g, b)


def draw_dots(turtle, color_list):
    y_pos = -225
    for row in range(10):
        #resets x
        x_pos = -225

        #moves turtle to left side and up one row.
        turtle.penup()
        turtle.setx(x_pos)
        turtle.sety(y_pos)
        turtle.pendown()

        #draws dots for each col. Moving turtle 50 units to the right each time
        for col in range(10):
            #draws dot at pos
            turtle.begin_fill()
            turtle.dot(20, get_random_color_from_image(color_list))
            turtle.end_fill()
            
            #moves turtle to the right
            x_pos += 50
            turtle.penup()
            turtle.setx(x_pos)
            turtle.pendown()

        #moves turtle up 50 units to make a new row
        y_pos += 50
        


def main():
    screen = t.Screen()
    screen.setup(600,600)
    t.colormode(255)
    turt = t.Turtle()
    config_turtle(turt)

    color_list = colorgram.extract('100DaysOfPythonBootcamp/Day18/david_hirst_spots/image/image3.jpg', 50)

    draw_dots(turt, color_list)
    
    screen.exitonclick()
if __name__ == "__main__":
    main()