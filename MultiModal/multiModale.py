from ivy.std_api import IvyBindMsg, IvySendMsg, IvyMainLoop

from LibCommon import myIvy
from threading import Timer


class automate:
    list_color = {'rouge': 'red', 'bleu': 'blue', 'vert': 'green', 'jaune': 'yellow'}
    state = 0
    timer = None

    def __init__(self):
        self.timer = Timer(5, self.timeout)
        self.form = None
        self.xy = None
        self.color = None

    def new_geste(self, agent, *larg):
        if self.state == 0:
            self.__reinit_timer()
            self.form = larg[0]
            self.state = 1

    def new_click(self, agent, *larg):
        if self.state == 1:
            self.__reinit_timer()
            self.xy = (larg[0], larg[1])
            self.state = 2
        elif self.state == 3:
            self.__reinit_timer()
            self.xy = (larg[0], larg[1])
            self.state = 1

    def new_vocal_couleur(self, agent, *larg):
        if self.state == 1 and larg[0] in self.list_color:
            self.__reinit_timer()
            self.color = self.list_color[larg[0]]
            self.state = 3
        elif self.state == 2:
            self.__reinit_timer()
            self.color = larg[0]
            self.state = 1

    def new_vocal_action(self, agent, *larg):
        if self.state == 1 and larg[0] == "ici":
            self.__reinit_timer()
            self.__maybe_send_create()
            self.state = 1

    def timeout(self):
        if self.state == 1:
            self.state = 0
        if self.state in [1, 2]:
            self.state = 1

    def __reinit_timer(self):
        self.timer.cancel()
        self.timer.start()

    def __maybe_send_create(self):
        if None not in [self.form, self.xy, self.color]:
            IvySendMsg("MULTIMODAL forme={} x={} y={} couleur={}".format(self.form, self.xy[0], self.xy[1], self.color))
            self.form = None
            self.xy = None
            self.color = None


class MyIvyMultiModale(myIvy.MyIvy):
    a = automate()

    def _createbind(self):
        IvyBindMsg(self.a.new_geste, '^GESTE forme=(.*)')
        IvyBindMsg(self.a.new_click, '^PALETTE x=(.*) y=(.*)')
        IvyBindMsg(self.a.new_vocal_couleur, '^VOCAL couleur=(.*)')
        IvyBindMsg(self.a.new_vocal_action, '^VOCAL action=(.*)')


MyIvyMultiModale("MultiModal", "127.255.255.255:2010")

IvyMainLoop()