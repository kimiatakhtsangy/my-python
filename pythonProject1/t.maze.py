import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("maze")
wn.setup(700, 700)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


levels = [""]
level_1 = [

    "XXXXXXXXXXXXXXXXXXXX",
    "XXX     XX   XXX  XX",
    "XX       XXX  X X XX",
    "XX X X X XXX    X X",
    "XXX        X   X   X",
    "XX   XX  X  XXXXXXXX",
    "XX   XX  XX  XXX  XX",
    "X  XX  XX  XXXXXXXXX",
    "XXXX   XXXX      X X",
    "X               XXXX",
    "XX X XXXXX  XXXX XXX",
    "XX XX  XXX       XXX",
    "       XXXXX    XXXX",
    "XX XXXXX         XXX",
    "XXX XXX  XXX      XX",
    "XXXX  X    XX    XXX",
    "X       XXXXXXXXXXXX",
    "XXXXX    XXXXXXXXXXX",
    "XXX X    XXXXXX    X",
    "XXXXXXXXXXXXXXXXXXXX"
]
levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x*20)
            screen_y = 288 - (y*20)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()


pen = Pen()
setup_maze(levels[1])

while True:
    pass








