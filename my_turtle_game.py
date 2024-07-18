import turtle
import time
import tkinter as tk  # Import tkinter to control the window
import random

WIDTH, HEIGHT = 800, 800
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'black', 'cyan', 'pink', 'brown', 'grey']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input... Try Again!")
            continue
        
        if (2 <= racers <= 10):
            return racers
        else:
            print("The number has to be between 2 - 10....Try Again!")

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)   
            racer.forward(distance)
            
            x, y = racer.pos()
            if (y >= HEIGHT // 2 - 10):
                return colors[turtles.index(racer)]
    
    
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i + 1) * spacingx, -HEIGHT //2 + 20) 
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racers")
    
    # Get the root window and lift it to the top
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

racers = get_number_of_racers()
init_turtle()
random .shuffle(COLORS)
colors = COLORS[:racers] #used the slice operator ":"
winner = race(colors)
print("The winner is the turtle with color:",winner)
time.sleep(3) 