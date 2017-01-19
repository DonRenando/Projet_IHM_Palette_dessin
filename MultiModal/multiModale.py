from ivy.std_api import IvyBindMsg, IvySendMsg, IvyMainLoop

from LibCommon import myIvy
from threading import Timer


class automate:
    list_color = {'rouge': 'red', 'bleu': 'blue', 'vert': 'green', 'jaune': 'yellow'}
    state = 0
    timer = None

    def __init__(self):
        self.timer = None
        self.form = None
        self.xy = None
        self.color = None

    def new_geste(self, agent, *larg):
        print("new_geste " + str(larg))
        print("state = " + str(self.state))

        if self.state == 0:
            self.__reinit_timer()
            self.form = larg[0]
            self.state = 1

        print("endstate = " + str(self.state))

    def new_click(self, agent, *larg):
        print("new click " + str(larg))
        print("state = " + str(self.state))

        if self.state == 1:
            self.__reinit_timer()
            self.xy = (larg[0], larg[1])
            self.state = 2

        elif self.state == 3:
            self.__reinit_timer()
            self.xy = (larg[0], larg[1])
            self.state = 1

        print("endstate = " + str(self.state))

    def new_vocal_couleur(self, agent, *larg):
        print("new vocal couleur " + str(larg))
        print("state = " + str(self.state))

        if self.state == 1 and larg[0].split(" ")[0] in self.list_color and int(larg[0].split(",")[1][0:2]) > 85:
            print(larg[0].split(" ")[0])
            self.__reinit_timer()
            self.color = self.list_color[larg[0].split(" ")[0]]
            self.state = 3

        elif self.state == 2:
            self.__reinit_timer()
            self.color = larg[0]
            self.state = 1
        print("endstate = " + str(self.state))

    def new_vocal_action(self, agent, *larg):
        print("new vocal action" + str(larg))
        print("state = " + str(self.state))
        if self.state == 1 and larg[0].split(" ")[0] == "ici":
            self.__reinit_timer()
            self.__maybe_send_create()
            self.state = 1
        print("endstate = " + str(self.state))

    def all(self, agent, *larg):
        print("all " + str(larg))

    def timeout(self):
        if self.state == 1:
            self.state = 0
        if self.state in [1, 2]:
            self.state = 1

    def __reinit_timer(self):
        pass
        """if self.timer:
            self.timer.cancel()
        self.timer = Timer(5, self.timeout)
        self.timer.start()"""

    def __maybe_send_create(self):
        if None not in [self.form, self.xy, self.color]:
            print("Send Forme")
            IvySendMsg("MULTIMODAL forme={} x={} y={} couleur={}".format(self.form, self.xy[0], self.xy[1], self.color))
            self.xy = None
            self.color = None


class MyIvyMultiModale(myIvy.MyIvy):
    a = automate()

    def _createbind(self):
        IvyBindMsg(self.a.all, '(.*)')
        IvyBindMsg(self.a.new_geste, '^Geste forme=(.*)')
        IvyBindMsg(self.a.new_click, '^PALETTE x=(.*) y=(.*)')
        IvyBindMsg(self.a.new_vocal_couleur, '^sra5 Parsed=VOCAL couleur=(.*)')
        IvyBindMsg(self.a.new_vocal_action, '^sra5 Parsed=VOCAL action=(.*)')


MyIvyMultiModale("MultiModal", "127.255.255.255:2010")

IvyMainLoop()