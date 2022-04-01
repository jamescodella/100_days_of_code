from turtle import Turtle, Screen
import random
import turtle
import colorgram
from matplotlib.pyplot import fill

# Initialize global cvars
colors =  ['red', 'DarkRed', 'blue', 'CadetBlue', 'green', 'DarkGreen', 'violet', 'pink', 'gold', 'purple', 'coral', 'black']
direction = [0, 90, 180, 270]

# Create and setup turtle objects for use in later functions
t = Turtle()
screen = Screen()
screen.colormode(255)

# Draw a square
def draw_square():
    ''' Draws a square'''
    for i in range(0,4):
        t.forward(100)
        t.right(90)

# draw a dashed line
def draw_dotted_line():
    '''
    Draw a dashed line
    '''
    for _ in range(50):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)

def random_color():
    '''
    Generated random rgb colors and returns a tuple.
    '''
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r, b, g)

def draw_n_gons(n=11):
    '''
    Draws n-gons in random colors.
    '''
    for num_sides in range(3,n):
        c = random.choice(colors)
        t.color()
        for shape_edge in range(0,num_sides):
            t.forward(100)
            angle = 360 / num_sides
            t.right(angle)

def random_walk(num_steps, pen_size= 10):
    '''
    Draws a "random walk" at 90 degree angle in random colors.
    '''
    t.hideturtle()
    for i in range(0, num_steps):
        # c = random.choice(colors)
        d = random.choice(direction)
        t.color(random_color())
        t.speed('fastest')
        t.pen(pensize=pen_size)
        t.right(d)
        t.forward(20)

def draw_spirograph(gap_size = 10):
    '''
    Draws a spirograh in random colors.
    '''
    t.hideturtle()
    t.speed('fastest')
    for _ in range(0, 360 // gap_size):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + 10)

def extract_colors(img, num_colors):
    '''
    Extract rgb colors from an image.
    '''
    colors = colorgram.extract(img, num_colors)
    colors_rgb = []
    for i in range(len(colors)):
        r, g, b = colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b
        colors_rgb.append((r,g,b))
    return colors_rgb

def draw_hirst(num_rows=10, num_columns=10):
    '''
    Draw Hirst-style dot art.
    '''
    t.speed('fastest')
    t.penup()
    t.hideturtle()
    # center the turtle
    t.setx(- num_columns*50//2 + 50)
    t.sety(- num_rows*50//2 + 50)
    colors = extract_colors('source/Day18_Hirst_Painting_Project/image/hirst_dots.jpg', 25)
    for row in range(0,num_rows):
        for col in range(0,num_columns):
            t.color()
            t.dot(20, random.choice(colors))
            t.forward(50)
        
        if row % 2 == 0:
            t.left(90)
            t.forward(50)
            t.left(90)

        else:
            t.right(90)
            t.forward(50)
            t.right(90)
        t.forward(50)
    

if __name__ == '__main__':

    draw_hirst(10,10)
    
    screen.exitonclick()