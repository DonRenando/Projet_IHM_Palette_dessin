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
        self.la_xy = None
        self.ca_xy = None
        self.color = None

    def new_geste(self, agent, *larg):
        print("new_geste " + str(larg))
        print("state = " + str(self.state))

        if self.state == 0:
            if larg[0] == "RECTANGLE" or larg[0] == "ROND":
                self.__reinit_timer()
                self.form = larg[0]
                self.state = 1

            elif larg[0] == "TRAIT":
                self.__reinit_timer()
                self.state = 4

            elif larg[0] == "Z":
                self.__reinit_timer()
                self.state = 7


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

        elif self.state in [4, 5, 6]:
            self.__reinit_timer()
            self.xy = (larg[0], larg[1])

        elif self.state == 8:
            self.__reinit_timer()
            self.xy = (larg[0], larg[1])
            self.__maybe_send_delete()
            self.state = 7

        print("endstate = " + str(self.state))

    def new_vocal_couleur(self, agent, *larg):
        print("new vocal couleur " + str(larg))
        print("state = " + str(self.state))

        if self.state == 1 and larg[0].split(" ")[0] in self.list_color and int(larg[0].split(",")[1][0:2]) > 85:
            print(larg[0].split(" ")[0])
            self.__reinit_timer()
            self.color = self.list_color[larg[0].split(" ")[0]]
            self.state = 3

        elif self.state == 2 and larg[0].split(" ")[0] in self.list_color and int(larg[0].split(",")[1][0:2]) > 85:
            print(larg[0].split(" ")[0])
            self.__reinit_timer()
            self.color = self.list_color[larg[0].split(" ")[0]]
            self.state = 1

        elif self.state == 5 and larg[0].split(" ")[0] in self.list_color and int(larg[0].split(",")[1][0:2]) > 85:
            print(larg[0].split(" ")[0])
            self.__reinit_timer()
            self.color = self.list_color[larg[0].split(" ")[0]]
            self.state = 5

        elif self.state == 6 and larg[0].split(" ")[0] in self.list_color and int(larg[0].split(",")[1][0:2]) > 85:
            print(larg[0].split(" ")[0])
            self.__reinit_timer()
            self.color = self.list_color[larg[0].split(" ")[0]]
            self.state = 6

        elif self.state == 7 and larg[0].split(" ")[0] in self.list_color and int(larg[0].split(",")[1][0:2]) > 85:
            print(larg[0].split(" ")[0])
            self.__reinit_timer()
            self.color = self.list_color[larg[0].split(" ")[0]]
            self.state = 7

        print("endstate = " + str(self.state))

    def new_vocal_action(self, agent, *larg):
        print("new vocal action" + str(larg))
        print("state = " + str(self.state))
        if self.state == 1 and larg[0].split(" ")[0] == "ici" and int(larg[0].split(",")[1][0:2]) > 85:
            self.__reinit_timer()
            self.__maybe_send_create()
            self.state = 1

        elif self.state == 4 and larg[0].split(" ")[0] == "là" and int(larg[0].split(",")[1][0:2]) > 85:
            self.__reinit_timer()
            self.la_xy = self.xy
            self.state = 6

        elif self.state == 4 and larg[0].split(" ")[0] == "ça" and int(larg[0].split(",")[1][0:2]) > 85:
            self.__reinit_timer()
            self.ca_xy = self.xy
            self.state = 5

        elif self.state == 5 and larg[0].split(" ")[0] == "là" and int(larg[0].split(",")[1][0:2]) > 85:
            self.__reinit_timer()
            self.la_xy = self.xy
            self.__maybe_send_deplacer()
            self.state = 4

        elif self.state == 6 and larg[0].split(" ")[0] == "ça" and int(larg[0].split(",")[1][0:2]) > 85:
            self.__reinit_timer()
            self.ca_xy = self.xy
            self.__maybe_send_deplacer()
            self.state = 4

        elif self.state == 7 and ("ce rectangle" in larg[0] or "ce rond" in larg[0]) and int(larg[0].split(",")[1][0:2]) > 85:
            self.__reinit_timer()
            if "ce rectangle" in larg[0]:
                self.form = "RECTANGLE"
            if "ce rond" in larg[0]:
                self.form = "ROND"
            print(self.form)
            self.state = 8

        print("endstate = " + str(self.state))

    def all(self, agent, *larg):
        print("all " + str(larg))

    def __timeout(self):
        print("timeout")
        print("state = " + str(self.state))
        if self.state in [1, 4, 7]:
            self.form = None
            self.state = 0

        elif self.state in [2, 3]:
            self.xy = None
            self.color = None
            self.state = 1

        elif self.state in [5, 6]:
            self.ca_xy = None
            self.la_xy = None
            self.xy = None
            self.color = None
            self.state = 4

        elif self.state == 8:
            self.form = None
            self.state = 4


        print("endstate = " + str(self.state))

    def __reinit_timer(self):
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(5, self.__timeout)
        self.timer.start()

    def __maybe_send_create(self):
        if None not in (self.form, self.xy, self.color):
            print("Send Forme")
            IvySendMsg("MULTIMODAL:creer forme={} x={} y={} couleur={}".format(self.form, self.xy[0], self.xy[1], self.color))
            self.xy = None
            self.color = None

    def __maybe_send_deplacer(self):
        if None not in (self.la_xy, self.ca_xy):
            print("Send Deplacer")
            IvySendMsg("MULTIMODAL:deplacer ca_x={} ca_y={} la_x={} la_y={} couleur={}"
                       .format(self.ca_xy[0], self.ca_xy[1], self.la_xy[0], self.la_xy[1],
                               self.color))
            self.ca_xy = None
            self.la_xy = None
            self.xy = None
            self.color = None

    def __maybe_send_delete(self):
        print(self.form)
        if None not in (self.form, self.xy):
            print("Send Delete")
            IvySendMsg("MULTIMODAL:supprimer forme={} x={} y={} couleur={}"
                       .format(self.form, self.xy[0], self.xy[1],
                               self.color))
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