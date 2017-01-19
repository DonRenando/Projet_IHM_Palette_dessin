import turtle
import myIvy
from ivy.std_api import *

LIST_FORM = []


class Form:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_in(self, x, y):
        return x == self.x and y == self.y


class Circle(Form):
    def __init__(self, x, y, radius, color="red"):
        super().__init__(x, y)
        self.radius = radius
        self.color = color

    def is_in(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < self.radius ** 2


class Rectangle(Form):
    def __init__(self, x, y, vert, hor, color="red"):
        super().__init__(x, y)
        self.vert = vert
        self.hor = hor
        self.color = color

    def is_in(self, x, y):
        return 0 <= (x - self.x) <= self.hor and 0 <= (y - self.y) <= self.vert


class MyTurtle(turtle.Turtle):
    def __init__(self, color="green"):
        turtle.Turtle.__init__(self, shape="turtle")
        self.pensize(3)
        self.my_turtle_color = color
        self.color(color)

        self.screen = turtle.Screen()

        self.screen.bgcolor("#FFFFFF")
        self.screen.title("Palette")
        self.screen.setup(1000, 600, 1, -1)
        self.screen.setworldcoordinates(0, 600, 1000, 0)
        self.screen.listen()
        self.screen.onclick(self.onclick)

    def __setup_draw(self, x, y, color):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.color("black", color)
        self.begin_fill()

    def __end_draw(self):
        self.end_fill()
        self.color(self.my_turtle_color)
        self.penup()
        self.home()

    def draw_circle_here(self, color="red", radius=50):
        self.draw_circle(Circle(self.xcor(), self.ycor(), radius, color))

    def draw_circle(self, circle):
        self.__setup_draw(circle.x, circle.y, circle.color)
        self.circle(circle.radius)
        self.__end_draw()

    def draw_rectangle_here(self, vert, hor, color="red"):
        self.draw_rectangle(Rectangle(self.xcor(), self.ycor(), vert, hor, color))

    def draw_rectangle(self, rectangle):
        self.__setup_draw(rectangle.x, rectangle.y, rectangle.color)
        self.setposition(rectangle.x + rectangle.vert, rectangle.x)
        self.setposition(rectangle.x + rectangle.vert, rectangle.x + rectangle.hor)
        self.setposition(rectangle.x, rectangle.x + rectangle.hor)
        self.setposition(rectangle.x, rectangle.x)
        self.__end_draw()

    def delete_rectangle(self, rectangle):
        self.__setup_draw(rectangle.x, rectangle.y, color="#FFFFFF")

    def onclick(self, x, y):
        myturtle.goto(x, y)
        IvySendMsg("PALETTE x={} y={}".format(x,y))


class MyIvyPalette(myIvy.MyIvy):
    def _createbind(self):
        IvyBindMsg(self.create, '^MULTIMODAL forme=(.*) x=(.*) y=(.*) couleur=(.*)')

    def create(self, agent, *larg):
        print('create [%s]', larg)
        if larg[0] == "RECTANGLE":
            LIST_FORM.append(Rectangle(larg[1], larg[2], 200, 100, larg[3]))
        elif larg[0] == "ROND":
            LIST_FORM.append(Circle(larg[1], larg[2], larg[3]))


myturtle = MyTurtle()






myturtle.draw_circle(Circle(120, 180, 50))
myturtle.draw_rectangle(Rectangle(300, 300, 100, 200, color="blue"))

myturtle.setposition(500, 450)
myturtle.draw_circle_here()

my_ivy = MyIvyPalette("Palette", "172.31.190.255:2010")

myturtle.screen._root.mainloop()