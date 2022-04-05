from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_right():
    tim.right(45)

def move_left():
    tim.left(45)

def move_backward():
    # Spins the turtle around
    tim.backward(10)

def clear_screen():
    '''
    Clears the drawing and returns the turtle to the center.
    '''
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

if __name__ == '__main__':

    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key='a', fun=move_left)
    screen.onkey(key='d', fun=move_right)
    screen.onkey(key='s', fun=move_backward)
    screen.onkey(key='c', fun=clear_screen)

    screen.exitonclick()
