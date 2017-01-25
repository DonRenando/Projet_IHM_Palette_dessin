import turtle
from LibCommon import myIvy
from ivy.std_api import *




class Form:
    def __init__(self, t, x, y, color):
        self.t = t
        self.x = x
        self.y = y
        self.color = color
        self.color_default = color

    def _setup_draw(self, x, y, color):
        self.t.penup()
        self.t.setposition(x, y)
        self.t.pendown()
        self.t.color(color, color)
        self.t.begin_fill()

    def _end_draw(self):
        self.t.end_fill()
        self.t.color(self.t.my_turtle_color)
        self.t.penup()
        self.t.home()

    def is_in(self, x, y):
        return x == self.x and y == self.y

    def draw(self):
        self._setup_draw(self.x, self.y, self.color)
        self.t.dot()
        self._end_draw()

    def delete(self):
        self.color = self.t.bgcolor
        self.draw()
        self.color = self.color_default

    @staticmethod
    def aim_delete(l_form, type_form, x, y, color=""):
        for form in l_form:
            if form.__class__.__name__.upper() == type_form.upper() and form.is_in(x, y) \
                    and color in ("", form.color):
                form.delete()
                l_form.remove(form)
                break

        for form in l_form:
            if form.is_in(x, y):
                form.draw()
        return l_form

    @staticmethod
    def aim_move(l_form, x, y, tx, ty, color=""):
        for form in l_form:
            if form.is_in(x, y)\
                    and color in ("", form.color):
                form.delete()
                form.x = tx
                form.y = ty
                form.draw()
                break
        return l_form


class Rond(Form):
    def __init__(self, t, x, y, radius=50, color="red"):
        super().__init__(t, x, y, color)
        self.radius = radius

    def is_in(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < self.radius ** 2

    def draw(self):
        self._setup_draw(self.x, self.y, self.color)
        self.t.circle(self.radius)
        self._end_draw()


class Rectangle(Form):
    def __init__(self, t, x, y, vert=50, hor=80, color="red"):
        super().__init__(t, x, y, color)
        self.vert = vert
        self.hor = hor
        self.color = color

    def is_in(self, x, y):
        return 0 <= (x - self.x) <= self.hor and 0 <= (y - self.y) <= self.vert

    def draw(self):
        self._setup_draw(self.x, self.y, self.color)
        self.t.setposition(self.x + self.hor, self.y)
        self.t.setposition(self.x + self.hor, self.y + self.vert)
        self.t.setposition(self.x, self.y + self.vert)
        self.t.setposition(self.x, self.y)
        self._end_draw()


class MyTurtle(turtle.Turtle):
    def __init__(self, color="green", bgcolor="#FFFFFF"):
        turtle.Turtle.__init__(self, shape="turtle")

        self.bgcolor = bgcolor

        self.pensize(3)
        self.my_turtle_color = color
        self.color(color)

        self.screen = turtle.Screen()

        self.screen.bgcolor(bgcolor)
        self.screen.title("Palette")
        self.screen.setup(1000, 600, 1, -1)
        self.screen.setworldcoordinates(0, 600, 1000, 0)
        self.screen.listen()
        self.screen.onclick(self.onclick)

    def onclick(self, x, y, **kwargs):
        myturtle.goto(x, y)
        IvySendMsg("PALETTE x={} y={}".format(x, y))


class MyIvyPalette(myIvy.MyIvy):
    LIST_FORM = []
    def _createbind(self):
        IvyBindMsg(self.create, '^MULTIMODAL:creer forme=(.*) x=(.*) y=(.*) couleur=(.*)')
        IvyBindMsg(self.move, '^MULTIMODAL:deplacer ca_x=(.*) ca_y=(.*) la_x=(.*) la_y=(.*) couleur=(.*)')
        IvyBindMsg(self.delete, '^MULTIMODAL:supprimer forme=(.*) x=(.*) y=(.*) couleur=(.*)')

    def create(self, agent, *larg):
        if larg[0] == "RECTANGLE":
            r = Rectangle(myturtle, self.__my_int(larg[1]), self.__my_int(larg[2]), color=larg[3])
            r.draw()
            self.LIST_FORM.append(r)
        elif larg[0] == "ROND":
            c = Rond(myturtle, self.__my_int(larg[1]), self.__my_int(larg[2]), color=larg[3])
            c.draw()
            self.LIST_FORM.append(c)

    def move(self, agent, *larg):
        self.LIST_FORM = Form.aim_move(self.LIST_FORM, larg[0],
                                       self.__my_int(larg[1]), self.__my_int(larg[2]),
                                       self.__my_int(larg[3]), color=larg[4])

    def delete(self, agent, *larg):
        self.LIST_FORM = Form.aim_delete(self.LIST_FORM, larg[0],
                                         self.__my_int(larg[1]), self.__my_int(larg[2]), color=larg[3])

    def __my_int(self, str):
        return int(str.split(".")[0])


myturtle = MyTurtle()
myturtle.penup()
myturtle.color("green")

my_ivy = MyIvyPalette("Palette", "127.255.255.255:2010")

myturtle.screen._root.mainloop()

